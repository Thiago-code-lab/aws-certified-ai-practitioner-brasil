# Module 12 — Use Cases and Architectures

Certification requires fewer formulas and more judgment: which service best addresses a given problem? This module organizes that reasoning into real-world scenarios and useful comparisons.

## Objective

Transform concepts into architectural decisions, comparing services and standards for chatbots, document extraction, recommendations, summarization, classification and assisted automation.

## How this topic appears on AIF-C01

- Map use case to the most coherent service.
- Compare ready-made services, Bedrock and custom ML.
- Practice reasoning by business requirement.

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
| Amazon Bedrock | Text generation, summary, Q&A and contextualized assistants. | Very common in GenAI scenarios. |
| Amazon Textract | Extraction of text, forms and tables from documents. | Appears in document automation. |
| Amazon Comprehend | Managed NLP for entity, sentiment and classification. | Useful compared to LLM in structured tasks. |
| Amazon Rekognition | Managed computer vision. | Appears in image and video scenarios. |

## Essential concepts

### Start with the type of expected result

If the company wants to extract fields from a PDF, perhaps Textract would be more direct than an LLM. If you want to analyze sentiment in reviews, Comprehend may be simpler. If you want to answer questions with natural language on your own, Bedrock with grounding may make more sense.

### Ready service vs generative model

Many AWS questions compare a specialized managed service with a more open foundation model-based solution. The correct answer usually favors the simplest service that is directly aligned with the problem, especially when it already exists.

### Architecture as composition

In real-world scenarios, it's common to combine multiple services: Textract for extracting, S3 for storing, Bedrock for summarizing, Lambda for orchestrating, and CloudWatch for observing. The exam values this complete solution reading.

## Practical example

### Contract automation

A pipeline might use Textract to extract information from contracts, send the structured results to storage, and then use Bedrock to generate a natural language executive summary. Each service fulfills a different role.

## Architectural reasoning

### Use the more specific service when the problem is already well known

OCR, image moderation, transcription, and sentiment analysis are examples where AWS already offers specialized managed services. On the exam, they are often preferred to more open and complex FM-based architectures when the requirement is objective.

### Use FM when the value is in language flexibility

When the problem requires contextualized summary, open-ended response, textual composition or richer conversational interaction, foundation models start to make more sense — especially combined with corporate data.

## Best practices

- Read the main verb of the case: extract, classify, generate, respond, moderate, recommend.
- Prefer the more specialized service when it meets the requirement directly.
- Combine pipeline services when the case requires more than one capacity.
- Evaluate cost, latency, governance and maintenance of the design.
- Avoid over-engineering with LLM where a ready-made service solves better.

## Exam tips

- Textract for documents; Rekognition for image/video; Comprehend for managed NLP; Bedrock for GenAI.
- A specialized managed service usually wins when the case is specific and common.
- LLM is not an automatic substitute for all specialized services.
- Always look for the dominant requirement of the scenario.

## Common pitfalls

- Use Bedrock for everything and ignore more direct specialized services.
- Do not separate structured extraction from textual generation.
- Choosing a service for its popularity rather than its fit for the requirement.
- Ignore composition of multiple services when the case is pipeline.

## Summary for review

- AI architecture starts by defining the problem correctly.
- Specialized services continue to be very relevant on AWS.
- Foundation models come in strong when language flexibility matters.
- Combined pipelines are common in real cases.
- The exam rewards solutions aligned to the dominant requirement.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 11 — Security and Compliance in AI](../11-AI-Security-and-Compliance/README.md).
- Continue to [Module 13 — AWS AI Services](../13-AWS-AI-Services/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
