# Module 13 — AWS AI Services

This module reviews AWS AI services by the problems they solve. Instead of memorizing lists, the focus is on understanding what problem each service solves and how it usually appears in exam answer choices.

## Objective

Consolidate key AWS AI services relevant to AIF-C01 and distinguish them in practical scenarios, including the difference between specialized services, GenAI, and ML platforms.

## How this topic appears on AIF-C01

- Quickly recognize the AWS service most aligned to the use case.
- Compare Bedrock, SageMaker AI and expert services.
- Review services within the scope of the exam with a practical eye.

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
| Amazon Bedrock | GenAI and foundation models. | Center of generative questions. |
| Amazon Comprehend / Textract / Rekognition / Transcribe / Translate / Polly / Lex | Specialized AI services. | They appear as more direct answers in specific cases. |
| Amazon Q Business / Q Developer | AI-assisted experiences for search and productivity. | They can appear as business productivity solutions. |
| Amazon Personalize | Personalized recommendations. | Important when the case talks about recommending items. |

## Essential concepts

### Mental catalog by type of problem

If speech is the problem, think Transcribe or Polly. If it's a document, think Textract. If it's a recommendation, think about Personalize. Whether it's open response or more flexible natural language assistant, think Bedrock.

### Specialized services are still very strong

A common mistake in preparing for AI is forgetting that AWS has been offering specialized AI services for years. On many questions, these services remain better answers than generic generative architectures.

### Note on current scope

The official list of services in scope of AIF-C01 must be prioritized. An important point: the official exam documentation still mentions Amazon Fraud Detector, but AWS stopped accepting new customers on **November 7, 2025**. For exam preparation, it is worth understanding the concept; for new projects, the practical architectural decision may be different.

## Practical example

### Quick map by problem

Text to audio? Polly. Audio to text? Transcribe. Questions about business documents? Q Business or Bedrock with an appropriate knowledge base. Classification or sentiment analysis in text? Comprehend. Product recommendation? Personalize.

## Architectural reasoning

### Specialized service for specialized task

When the need is clear and the specialized service exists, it tends to be cheaper, simpler and manageable. This pattern appears repeatedly across AWS certifications.

### Bedrock enters when language flexibility changes the game

If the case is not just classifying or extracting, but conversing, summarizing, generating or responding based on context, Bedrock is once again a strong candidate — especially with grounding.

## Best practices

- Learn services by business problem, not alphabetically.
- Differentiate specialized services from ML and GenAI platforms.
- Prioritize the official list of services within the scope of the exam.
- Understand the conceptual limits of each service.
- Always consider simplicity, cost and governance.

## Exam tips

- Personalize is for recommendation; Comprehend is for structured NLP; Bedrock is for GenAI.
- Textract is strong on documents; Rekognition in image/video.
- Lex covers managed conversational bot; Polly and Transcribe handle voice.
- Q Business appears in productivity and assisted business search.

## Common pitfalls

- Use LLM as a default response for any scenario.
- Confusing Personalize with search solution.
- Confusing Comprehend with Bedrock in tasks that do not require generation.
- Ignoring that the exam follows an official list of services in scope.

## Summary for review

- Right service depends on the right problem.
- AWS has a strong specialized AI portfolio in addition to GenAI.
- Bedrock does not replace all traditional AI services.
- Q Business, Personalize, Lex, Textract and Comprehend have clear roles.
- The official AIF-C01 list should guide your final review.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 12 — Use Cases and Architectures](../12-AI-Use-Cases-and-Architectures/README.md).
- Continue to [Module 14 — Integration with Applications](../14-Application-Integration/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
