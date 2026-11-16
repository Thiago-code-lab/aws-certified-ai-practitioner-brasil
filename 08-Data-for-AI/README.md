# Module 08 — Data for AI

Models only respond well when given correct, accessible, and governed data. The exam demands exactly this reasoning: clean, updated and protected data is part of the AI architecture, not a secondary detail.

## Objective

Understand how to prepare, store, classify and protect data used in ML and GenAI, focusing on S3, metadata, labeling, chunking and information sensitivity.

## How this topic appears on AIF-C01

- Relate data quality with model quality.
- Understand document preparation for RAG.
- Recognize the role of data classification and protection.

## Module navigation

- [README](./README.md)
- [Cheatsheet](./cheatsheet.md)
- [Flashcards](./flashcards.md)
- [Questions](./questions.md)
- [Use cases](./use-cases.md)
- [Practical lab](./lab.md)
- [Official links](./links.md)

## Core AWS Services

| AWS Service | Role in the module | How it appears on the exam |
| --- | --- | --- |
| Amazon S3 | Common storage layer for datasets and documents. | It shows up all the time in AI pipelines. |
| AWS Glue | Data cataloging and transformation. | Important in preparing and organizing data. |
| AWS Lake Formation | Access governance over data in a data lake. | Appears when the case requires refined control of the data. |
| Amazon Macie | Discovery of sensitive data in S3. | Important for LGPD, PII and security. |

## Essential concepts

### Quality, freshness and relevance of data

Models do not compensate for outdated or poorly organized data. In GenAI, old documents can feed wrong answers. In supervised ML, bad labels make bad decisions. The exam usually demands this effect in business language.

### Chunking, metadata and document curation

For RAG, it's not enough to throw PDFs into a bucket. It is necessary to divide the content into useful parts, preserve context and maintain metadata such as date, area, version and sensitivity. This improves retrieval and helps control what can and cannot be used.

### Data protection and classification

Data for AI often contains PII, contracts, internal policies, or regulated data. The architecture needs to combine minimum required access, classification, encryption, versioning, and usage trail.

## Practical example

### Corporate knowledge base

An internal policy base needs versioning, organization by domain, removal of obsolete documents, and sensitivity marking. Without this, the AI starts to retrieve irrelevant, duplicate or prohibited material.

## Architectural reasoning

### S3 as origin, not as complete governance engine

S3 is great as central storage, but governance comes from the design around it: naming, lifecycle, catalog, permissions, and classification. On the exam, a common mistake is to treat buckets as a complete governance solution.

### Data preparation is part of application design

Chunking, cleaning, deduplication and versioning are not accessory tasks. These are architectural steps that define cost, retrieval quality and risk of information leakage.

## Best practices

- Version relevant documents and datasets.
- Remove or isolate content that is obsolete, duplicated, or too sensitive for the use case.
- Use metadata to facilitate filtering and governance.
- Classify data before connecting it to AI applications.
- Design update pipeline so that the base does not age silently.

## Exam tips

- More data does not mean better results if the quality is poor.
- Macie appears when the theme is PII in S3.
- Documents for RAG need preparation, not just storage.
- Lake Formation reinforces governance over data at scale.

## Common pitfalls

- Upload files without metadata and expect accurate contextual retrieval.
- Mixing valid and obsolete material on the same basis without control.
- Ignore sensitive data before exposing a document base to AI.
- Thinking that the model will correct data quality problems.

## Summary for review

- Data quality is a decisive factor in AI and GenAI.
- RAG depends on well thought out chunking and metadata.
- S3 stores; governance organizes and protects.
- Macie helps locate sensitive data on S3.
- Updated and reliable data supports better responses.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 07 — Responsible AI and Governance](../07-Responsible-AI-and-Governance/README.md).
- Continue to [Module 09 — Prompt Engineering](../09-Prompt-Engineering/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
