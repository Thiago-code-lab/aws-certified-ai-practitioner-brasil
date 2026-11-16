"""Mutation tests for educational loss and broken navigation."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import validate

SOURCE = '''## Questão 01
**Pergunta:** Qual serviço?
- A) Amazon Macie
- B) Amazon Polly
- C) Amazon SQS
- D) Amazon S3
<details><summary><strong>Ver resposta</strong></summary>
✅ **Resposta correta:** A
**Explicação:** Descoberta de dados sensíveis.
**Por que a alternativa B está errada:** É síntese de voz.
</details>
'''
TARGET = '''## Question 01
**Question:** Which service?
- A) Amazon Macie
- B) Amazon Polly
- C) Amazon SQS
- D) Amazon S3
<details><summary><strong>See answer</strong></summary>
✅ **Correct answer:** A
**Explanation:** Sensitive data discovery.
**Why option B is wrong:** It provides speech synthesis.
</details>
'''


class RegressionTests(unittest.TestCase):
    def errors(self, changed: str) -> list[str]:
        approved = [{'target_sha256': validate.questions(TARGET)[0]['sha256']}]
        return validate.question_errors(SOURCE, changed, approved)

    def test_approved_translation_passes(self) -> None:
        self.assertEqual(self.errors(TARGET), [])

    def test_wrong_answer_rejected(self) -> None:
        self.assertTrue(self.errors(TARGET.replace('answer:** A', 'answer:** B')))

    def test_missing_alternative_rejected(self) -> None:
        self.assertTrue(self.errors(TARGET.replace('- D) Amazon S3\n', '')))

    def test_option_reordering_rejected(self) -> None:
        self.assertTrue(self.errors(TARGET.replace('- A) Amazon Macie', '- A) Amazon Polly')))

    def test_missing_distractor_explanation_rejected(self) -> None:
        self.assertTrue(self.errors(TARGET.replace('It provides speech synthesis.', '')))

    def test_missing_question_rejected(self) -> None:
        self.assertTrue(self.errors(''))

    def test_flashcard_answer_loss_rejected(self) -> None:
        self.assertTrue(validate.structural_errors('<details>**Resposta:** Data</details>',
                                                  '<details></details>', 'flashcards.md'))

    def test_lab_step_loss_rejected(self) -> None:
        self.assertTrue(validate.structural_errors('1. Read\n2. Compare', '1. Read', 'lab.md'))

    def test_bad_table_and_fence_rejected(self) -> None:
        self.assertTrue(validate.markdown_errors('| A | B |\n| --- | --- |\n| one |\n```\nx'))

    def test_portuguese_prose_rejected(self) -> None:
        self.assertTrue(validate.language_errors('A resposta exige dados de treinamento.'))

    def test_source_urls_exempt_from_language_scan(self) -> None:
        self.assertFalse(validate.language_errors('See https://example.com/questoes/dados.'))

    def test_links_images_and_anchors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'README.md'
            path.write_text('# Good title\n# Good title\n', encoding='utf-8')
            self.assertFalse(validate.link_errors(path, '[OK](#good-title-1)', root)[0])
            self.assertTrue(validate.link_errors(path, '[Bad](#missing)', root)[0])
            self.assertTrue(validate.link_errors(path, '![Bad](missing.png)', root)[0])
            self.assertTrue(validate.link_errors(path, '<img src="missing.png">', root)[0])
            self.assertTrue(validate.link_errors(path, '[Bad](../outside.md)', root)[0])


if __name__ == '__main__':
    unittest.main()
