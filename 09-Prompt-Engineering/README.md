# Module 09 — Prompt Engineering

Prompt engineering is one of the most practical topics on the exam. The exam wants you to understand how instruction, context, format, and limits change the behavior of the generative application.

## Objective

Learn how to structure more useful, predictable and safe prompts for real cases on AWS, connecting technique with cost, quality and governance.

## How this topic appears on AIF-C01

- Structure prompts with role, context, objective and format.
- Differentiate zero-shot, few-shot and output restrictions.
- Mitigate hallucination with instructional engineering and grounding.

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
| Amazon Bedrock | Natural environment for testing and operating prompts in FM applications. | Appears as the main service for orchestrating prompts. |
| Amazon Bedrock Guardrails | Complements the prompt with content policies. | Important in regulated flows. |
| AWS Lambda | Common component to apply prompt templates in backend. | Appears in serverless integrations. |
| Amazon CloudWatch | Observability of calls and application behavior. | Supports testing and prompt operation in production. |

## Essential concepts

### Structure of a good prompt

Better prompts make clear the model's role, task objective, authoritative context, output format, and constraints. This clarity reduces ambiguity and helps the application become more predictable.

### Zero-shot, few-shot and examples

Zero-shot is asking the task without examples. Few-shot includes some input and output examples to guide behavior. In fact, few-shot is usually relevant when the company needs greater standardization without going straight to fine-tuning.

### Prompts as part of the architecture

Prompt engineering isn't just about pretty text. It influences cost, security, format, latency and error rate. In production, prompt templates, versioning and observability are important practices.

## Practical example

### Standardized response in JSON

A support assistant needs to return priority, summary, and recommended action in JSON. A generic prompt can produce free text. A prompt with explicit schema, minimal required context, and examples tends to generate more predictable output.

## Architectural reasoning

### A strong prompt does not replace a trusted knowledge base

Even a well-written prompt does not correct a lack of factual context. When business data is essential, prompt engineering must include retrieval, access rules and output validation.

### Prompt versioning is also governance

When prompts change application behavior, they become important artifacts. Versioning, testing, and comparing prompts reduces silent regressions and improves solution maintainability.

## Best practices

- Describe the role, objective, context, format and limits of the response.
- Use few-shot when the task requires consistency of style or structure.
- Ask for verifiable formats, such as JSON or numbered lists, when integration depends on it.
- Avoid excessive and irrelevant context.
- Version important prompts and monitor behavior in production.

## Exam tips

- Prompt engineering improves instruction; RAG improves source-based factuality.
- Few-shot examples help establish a response pattern without training the model.
- If the output needs to be consumed by the system, explicit structure matters a lot.
- Guardrails complement prompt when the case requires policy.

## Common pitfalls

- Thinking that a prompt alone solves a lack of business knowledge.
- Sending too much context and degrading the response.
- Request free output when the application requires a rigid structure.
- Treat prompt as disposable text, without testing and without versioning.

## Summary for review

- A prompt is a critical part of a generative application.
- Clarity of task and format reduces variability.
- Few-shot examples help standardize responses.
- Good prompt and RAG complement each other.
- Versioning and prompt observability are mature practices.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 08 — Data for AI](../08-Data-for-AI/README.md).
- Continue to [Module 10 — Generative AI on AWS](../10-Generative-AI-on-AWS/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
