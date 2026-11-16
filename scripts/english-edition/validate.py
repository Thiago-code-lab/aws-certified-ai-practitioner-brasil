"""Validate English coverage and reviewed educational contracts without AWS access."""
from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / 'docs/english-edition'
PARSER = MarkdownIt('commonmark').enable('table')
PORTUGUESE = re.compile(
    r'\b(?:questões|questoes|pergunta|resposta|gabarito|módulo|modulo|'
    r'cenário|cenarios|treinamento|governança|segurança|não|nao|'
    r'conceitos|aprendizado|simulado|simulados|revisão|revisao|'
    r'prático|pratico|serviços|servicos|dados|conformidade|'
    r'fundamentos|introdução|introducao|acompanhe|estamos|você|voce)\b', re.I)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(name: str) -> Any:
    return json.loads((AUDIT / name).read_text(encoding='utf-8'))


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def source_tree(commit: str) -> dict[str, bytes]:
    archive = subprocess.check_output(['git', '-c', 'core.autocrlf=false', 'archive', commit], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
        return {item.name: tree.extractfile(item).read() for item in tree if item.isfile()}


def questions(text: str) -> list[dict[str, Any]]:
    blocks = re.split(r'(?m)^## (?:Questão|Question) (\d+)\s*$', text)[1:]
    result = []
    for number, body in zip(blocks[::2], blocks[1::2]):
        body = body.split('\n---')[0].strip()
        answer = re.search(r'\*\*(?:Resposta correta|Correct answer):\*\*\s*([A-D])', body)
        options = re.findall(r'(?m)^- ([A-D])\) (.+)$', body)
        stem = re.search(r'\*\*(?:Pergunta|Question):\*\* (.+)', body)
        result.append(dict(number=number, stem=stem[1] if stem else '', options=options,
                           answer=answer[1] if answer else '', sha256=digest(body.encode())))
    return result


def question_errors(source: str, target: str, approved: list[dict[str, Any]]) -> list[str]:
    original, translated = questions(source), questions(target)
    errors = []
    if len(original) != len(translated) or len(translated) != len(approved):
        return ['Question count changed']
    for before, after, record in zip(original, translated, approved):
        if before['number'] != after['number'] or before['answer'] != after['answer']:
            errors.append(f"Question {before['number']}: numbering or answer changed")
        if [x[0] for x in before['options']] != [x[0] for x in after['options']]:
            errors.append(f"Question {before['number']}: alternatives lost or reordered")
        if not after['stem'] or any(not value.strip() for _, value in after['options']):
            errors.append(f"Question {before['number']}: empty stem or option")
        if after['sha256'] != record['target_sha256']:
            errors.append(f"Question {before['number']}: unreviewed content or explanation change")
    return errors


def structural_errors(source: str, target: str, path: str) -> list[str]:
    errors = []
    for tag in ('details', 'summary'):
        for closing in ('', '/'):
            marker = f'<{closing}{tag}>'
            if source.count(marker) != target.count(marker):
                errors.append(f'{path}: {marker} count changed')
    if len(re.findall(r'(?m)^\s*\d+\. ', source)) != len(re.findall(r'(?m)^\s*\d+\. ', target)):
        errors.append(f'{path}: numbered steps changed')
    if len(re.findall(r'\*\*Pergunta rapida:', source)) != len(re.findall(r'\*\*Quick question:', target)):
        errors.append(f'{path}: short review prompts changed')
    if len(re.findall(r'(?m)^## Card \d+', source)) != len(re.findall(r'(?m)^## Card \d+', target)):
        errors.append(f'{path}: flashcard count changed')
    for before, after in (('**Pergunta:**', '**Question:**'), ('**Resposta:**', '**Answer:**'),
                          ('**Resposta curta:**', '**Short answer:**')):
        if source.count(before) != target.count(after):
            errors.append(f'{path}: question/answer structure changed')
    if sum(line.startswith('|') for line in source.splitlines()) != sum(line.startswith('|') for line in target.splitlines()):
        errors.append(f'{path}: table rows lost or added')
    source_fences = [token for token in PARSER.parse(source) if token.type == 'fence']
    target_fences = [token for token in PARSER.parse(target) if token.type == 'fence']
    if len(source_fences) != len(target_fences):
        errors.append(f'{path}: fenced examples changed')
    for before, after in zip(source_fences, target_fences):
        if before.info and (before.info != after.info or before.content != after.content):
            errors.append(f'{path}: executable example changed')
    return errors


class HTMLReferences(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.references.extend(value for name, value in attrs if name in ('src', 'href') and value)


def references(text: str) -> list[str]:
    found = []
    for token in PARSER.parse(text):
        for child in token.children or []:
            if child.type in ('link_open', 'image'):
                found.append(child.attrGet('href' if child.type == 'link_open' else 'src'))
    html = HTMLReferences()
    html.feed(text)
    return found + html.references


def anchors(text: str) -> set[str]:
    used: Counter[str] = Counter()
    result = set()
    tokens = PARSER.parse(text)
    for index, token in enumerate(tokens):
        if token.type != 'heading_open':
            continue
        title = tokens[index + 1].content
        title = re.sub(r'<[^>]*>|[*`]', '', title).lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        result.add(slug + (f'-{used[slug]}' if used[slug] else ''))
        used[slug] += 1
    result.update(re.findall(r'\bid=["\']([^"\']+)', text))
    return result


def link_errors(path: Path, text: str, root: Path = ROOT) -> tuple[list[str], int]:
    errors, count = [], 0
    for reference in references(text):
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        count += 1
        target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/')
                  else path.parent / unquote(url.path)) if url.path else path
        if not target.resolve().is_relative_to(root.resolve()) or not target.exists():
            errors.append(f'{path.relative_to(root)}: missing local target {reference}')
        elif url.fragment and target.suffix == '.md':
            if unquote(url.fragment) not in anchors(target.read_text(encoding='utf-8')):
                errors.append(f'{path.relative_to(root)}: missing anchor {reference}')
    return errors, count


def markdown_errors(text: str) -> list[str]:
    errors = []
    fences = re.findall(r'(?m)^\s*(`{3,}|~{3,})', text)
    if len(fences) % 2:
        errors.append('Unclosed fenced block')
    for tag in ('details', 'summary'):
        if text.count(f'<{tag}>') != text.count(f'</{tag}>'):
            errors.append(f'Unbalanced {tag}')
    widths = []
    for line in text.splitlines() + ['']:
        if line.startswith('|') and line.endswith('|'):
            widths.append(len(re.split(r'(?<!\\)\|', line)))
        else:
            if widths and len(set(widths)) != 1:
                errors.append('Inconsistent Markdown table width')
            widths = []
    return errors


def language_errors(text: str) -> list[str]:
    prose = re.sub(r'https?://[^\s<>]+|`[^`]+`', '', text)
    return sorted({match[0] for match in PORTUGUESE.finditer(prose)})


def validate_files(inventory: dict[str, Any], source: dict[str, bytes]) -> tuple[list[str], Counter[str]]:
    errors, counts = [], Counter()
    editorial = {item['target']: item for item in read_json('editorial-manifest.json')['files']}
    for entry in inventory['files']:
        target = ROOT / entry['target']
        if entry['source'] not in source or digest(source[entry['source']]) != entry['source_sha256']:
            errors.append(f"Source digest mismatch: {entry['source']}")
        if not target.is_file():
            errors.append(f"Missing target: {entry['target']}")
            continue
        if not entry['markdown']:
            current = target.read_bytes()
            if target.suffix != '.png':
                current = current.replace(b'\r\n', b'\n')
            if current != source[entry['source']]:
                errors.append(f"Protected asset/configuration changed: {entry['target']}")
            continue
        counts['source_markdown_equivalents'] += 1
        original, translated = source[entry['source']].decode('utf-8-sig'), target.read_text(encoding='utf-8')
        if digest(target.read_bytes().replace(b'\r\n', b'\n')) != editorial[entry['target']]['target_sha256']:
            errors.append(f"Unreviewed document change: {entry['target']}")
        if entry['source'] not in ('README.md', '16-Simulados-e-Questoes/README.md'):
            errors.extend(structural_errors(original, translated, entry['target']))
        counts['flashcards'] += len(re.findall(r'(?m)^## Card \d+', translated))
        counts['short_review_prompts'] += translated.count('**Quick question:**')
        counts['labs'] += target.name == 'lab.md'
        if entry['source'] != entry['target'] and (ROOT / entry['source']).exists():
            errors.append(f"Obsolete source path remains: {entry['source']}")
    return errors, counts


def validate_questions(source: dict[str, bytes]) -> list[str]:
    audit = read_json('question-audit.json')
    errors = []
    for group in audit['multiple_choice_files']:
        errors.extend(question_errors(source[group['source']].decode('utf-8-sig'),
                                      (ROOT / group['target']).read_text(encoding='utf-8'), group['questions']))
    return errors


def validate_repository() -> dict[str, Any]:
    inventory = read_json('source-inventory.json')
    source = source_tree(inventory['source_commit'])
    errors, counts = validate_files(inventory, source)
    if {item['source'] for item in inventory['files']} != set(source):
        errors.append('Source inventory does not match the complete source tree')
    counts['modules'] = len(list(ROOT.glob('[0-9][0-9]-*/README.md')))
    if counts['modules'] != 18:
        errors.append('Expected all 18 modules')
    for path in sorted(ROOT.rglob('*.md')):
        text = path.read_text(encoding='utf-8')
        found, checked = link_errors(path, text)
        errors.extend(found + [f'{path.relative_to(ROOT)}: {error}' for error in markdown_errors(text)])
        counts['local_references_checked'] += checked
        errors.extend(f'{path.relative_to(ROOT)}: Portuguese prose: {word}' for word in language_errors(text))
    errors.extend(validate_questions(source))
    for path in ROOT.glob('.github/ISSUE_TEMPLATE/*.md'):
        metadata = yaml.safe_load(path.read_text(encoding='utf-8').split('---')[1])
        if not all(metadata.get(key) for key in ('name', 'about', 'title', 'labels')):
            errors.append(f'Invalid issue template metadata: {path.name}')
    if git('rev-parse', '--abbrev-ref', 'HEAD') != inventory['target_branch']:
        errors.append('Validation must run on the English branch')
    for ref in ('main', 'origin/main', 'origin/gh-pages'):
        expected = inventory['protected_gh_pages'] if ref.endswith('gh-pages') else inventory['source_commit']
        if git('rev-parse', ref) != expected:
            errors.append(f'Protected ref changed: {ref}')
    return dict(passed=not errors, counts=dict(counts), errors=errors,
                lab_execution='Static review only; no AWS resources provisioned',
                semantic_limit='Structural, language-pattern, and reviewed-digest checks complement editorial review.')


def main() -> None:
    result = validate_repository()
    (AUDIT / 'validation-results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
