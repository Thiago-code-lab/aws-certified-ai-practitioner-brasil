# English edition audit

This edition translates **all 133 Markdown documents** from Portuguese source commit `122726b73a6e805a71b711dd65d1786fcc2ba42f`, retaining all **18 modules**, 129 module documents, the main README, and three GitHub issue templates. Publication is restricted to [`aif-c01-english`](https://github.com/Thiago-code-lab/aws-certified-ai-practitioner-brasil/tree/aif-c01-english).

## Coverage and naming

- [Source inventory](source-inventory.json): one mapping and original SHA-256 digest for each of the **140 original files**. It covers Markdown, four PNG images, the MIT license, HTML portal, and deployment workflow.
- **119 original file paths renamed**, including changes to **16 module directory names** and **40 file basenames**. Seven distinct repeated Portuguese basenames were translated. Module numbering and order are preserved.
- Original images, license, `index.html`, and `.github/workflows/deploy.yml` retain their original Git blob contents. Windows checkout line endings can differ from repository blobs.
- [Editorial manifest](editorial-manifest.json): all 133 English document digests, draft method, review scope, and exceptions. English digests normalize CRLF to LF so validation works across Windows and Unix checkouts.
- [Reference editions](reference-editions.json): inspected CLF-C02 and SAA-C03 branches and exact commits. Their English paths, CloudStudy identity, GitHub navigation, inventories, and regression-check conventions informed this edition. Portal development was excluded as requested.

## Module coverage

| Modules | Coverage |
| --- | --- |
| 01–04 | AI and ML introduction, generative AI, ML fundamentals, foundation models and LLMs |
| 05–09 | Bedrock, SageMaker AI, responsible AI, governance, data for AI, prompt engineering |
| 10–15 | Generative applications, security, compliance, use cases, AWS AI services, integration, optimization |
| 16–18 | Practice exams, final review, error log, glossary, official resources |

All source lesson explanations, examples, use cases, cheatsheets, flashcards, question alternatives, answer explanations, lab steps, and learning references have English equivalents. Machine-assisted drafting was followed by editorial reading, terminology corrections, source comparison, and structural checks. No translation service or model is required to read the materials or run validation.

## Questions and source discrepancies

The [question audit](question-audit.json) records every multiple-choice question with its original and English stem, ordered alternatives, correct letter, reviewed digest, and an editorial mapping to the official exam domains.

- **30 multiple-choice occurrences**, representing **22 distinct questions**.
- **85 short-answer review prompts**, five in each of the 17 module review files outside module 16.
- **144 expandable flashcards**, eight per module.
- **17 lab documents**; module 16 contains preparation resources instead of a lab.
- **Zero answer-letter changes** and **zero contradictory answer keys found**. Answers are inline; the source has no separate answer-key files to reconcile. Each incorrect-option explanation present in the source is retained; explanations for every other distractor were not invented.

Corrections to source descriptions are explicit:

1. Module 16 advertised 13/20/20/15 questions in its introduction. Actual counts are **6/8/8/8**, matching its original inventory table.
2. The second practice exam repeats the eight questions in the first. All duplicates remain, with an explanatory note.
3. The proposed 65-question assembly plan was impossible with the available bank. Its section now explains the limitation and points to official preparation resources.
4. The bank contains single-answer multiple-choice questions. Officially permitted multiple-response, ordering, and matching formats are described without claiming they are represented in this bank.
5. The domain-practice filename did not provide named domain sections. The audit supplies a dominant-objective classification for every multiple-choice occurrence. These are editorial judgments, not AWS labels, and the bank is not weighted like the exam.
6. The original raw-percentage readiness ranges remain study heuristics, with a clearer warning about the small bank and repeated questions.

## Technical terminology and references

The [AWS reference catalog](aws-reference-catalog.json) lists the official pages consulted and the scope of each check on **November 16, 2026**. The [exam revision history](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-revisions.html) lists version **1.2**, published **October 29, 2026**. Current domain names and weights were checked against the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html).

Terminology is standardized around foundation models, LLMs, embeddings, vector databases, retrieval, RAG, fine-tuning, inference, training, prompt engineering, responsible AI, and explainability. Service names are preserved, including Macie, Personalize, Comprehend, Rekognition, IAM, and Secrets Manager. Amazon SageMaker AI is used for the ML platform; existing API namespaces remain unchanged.

Guardrails and grounding are described as risk-reduction measures rather than guarantees of correctness or perfect filtering. Source references to Amazon Q Business and Amazon Bedrock Agents are retained with availability notes: Q Business is closed to new customers, and Agents is now Agents Classic, also closed to new sign-ups. Official notices point new projects toward Quick and AgentCore respectively. The original Fraud Detector availability warning is retained and verified; the source claim that the current in-scope list still names Fraud Detector is corrected because the reviewed list no longer includes it.

## Validation

From the repository root, with Python 3.10 or later:

```sh
python -m pip install -r scripts/english-edition/requirements.txt
python scripts/english-edition/validate.py
python -m unittest discover -s scripts/english-edition -p "test_*.py"
git diff --check
```

[Validation results](validation-results.json) record source coverage, module counts, language-pattern checks, relative Markdown and HTML references, local images, heading anchors, table widths, fenced blocks, expandable answers, lab steps, protected files, question letters and option order, and issue-template metadata. Reviewed document and question digests detect unapproved content changes, including explanation loss.

[Test results](test-results.json) record 12 passing tests. Mutation tests reject a wrong answer, deleted alternative, changed alternative, missing distractor explanation, missing question, lost flashcard answer, deleted lab step, malformed table or fence, Portuguese prose, and broken links or anchors. Source-URL words are exempt from prose language checks.

## Limitations and intentional exceptions

- AWS labs received **static review only**. No AWS resources were provisioned and no console procedure or inference request was executed. The source labs are primarily conceptual exercises; its fenced examples are text architecture diagrams rather than executable AWS programs.
- Automated checks complement editorial review. They do not independently establish semantic equivalence, AWS feature behavior, exam readiness, or future availability. This release has not received independent subject-matter-expert certification.
- This is a complete translation of the source curriculum, not a newly expanded syllabus for every current exam-guide objective. Consult the official guide for newer agentic AI topics absent from the source.
- Original raster artwork may contain Portuguese. Promotional URLs, proper names, license text, and audit JSON source records are intentional exceptions. No unintended Portuguese educational prose is accepted by the language scan.
- External URLs can change. Local reference validation does not imply an exhaustive external-link crawl; the catalog identifies the official references actually reviewed.
- The existing Portuguese HTML portal and deployment configuration are deliberately untouched. Use GitHub Markdown for this English edition. No Pages setup, hosting dependency, deployment workflow, PR, or merge was created.

## Release commits and protected branches

[Release commits](release-commits.json) records the source commit, implementation commits, publication head, and the verified remote refs. Audit-only commits after the implementation head are discoverable with `git log` on the English branch; a commit cannot record its own final hash inside its content.

Protected source `main`: `122726b73a6e805a71b711dd65d1786fcc2ba42f`.

Protected `gh-pages`: `224c0a075fa702bf9912dc75b86e0012797fb191`.

All translation changes are published exclusively to `aif-c01-english`. See the final release evidence for the remote verification.

[Return to the English learning path](../../README.md)
