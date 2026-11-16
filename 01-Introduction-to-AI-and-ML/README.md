# Module 01 — Introduction to AI and ML

This module establishes the core vocabulary of the exam. The goal is to distinguish AI, machine learning, deep learning and generative AI without falling into loose or academic definitions.

## Objective

By the end of this module, you should be able to explain what AWS calls AI workloads, differentiate between training and inference, and recognize when a use case calls for an off-the-shelf service, a custom model, or a generative architecture.

## How this topic appears on AIF-C01

- Understand the difference between traditional AI, ML and generative AI.
- Recognize training, validation, implementation and inference as distinct phases.
- Identify when the correct answer calls for a managed AWS service rather than raw infrastructure.

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
| Amazon S3 | Storage of datasets, training artifacts and documents for RAG. | Appears as a data foundation for ML and GenAI. |
| Amazon Bedrock | Managed layer to consume foundation models via API. | Tested as a gateway to generative AI. |
| Amazon SageMaker AI | Platform to prepare data, train, tune and deploy custom models. | Tested when the question requires custom ML. |
| AWS IAM | Controlling access to data, models and AI applications. | Appears in security scenarios from the beginning of the blueprint. |

## Essential concepts

### AI, ML, deep learning and generative AI

AI is the broadest umbrella: any technique that allows software to perform tasks associated with reasoning, perception, or decision-making. Machine learning is a subset of AI in which the system learns patterns from data. Deep learning uses multi-layer neural networks. Generative AI goes beyond classification or prediction and creates new content such as text, image, audio or code.

### Training vs inference

Training is the phase in which a model learns from examples. Inference is the moment when the already trained model receives new input and produces a response. On the exam, this often appears as a comparison of cost, latency and operational responsibility: training tends to be heavier and occasional; inference, more recurring and connected to the user experience.

### Managed-first mindset on AWS

AWS typically rewards the most managed choice that meets the requirements in certification questions. If the company only wants to use generative AI in production, Bedrock tends to be a better answer than setting up its own infrastructure. If you need to create a fully customized model with proprietary data, SageMaker AI comes into its own.

## Practical example

### Automatic ticket screening

A support center receives thousands of tickets per day. If the objective is to classify tickets by priority and responsible area, this can already be solved with supervised ML or even a managed natural language service, depending on the scope. If the objective is to generate contextualized responses from an internal knowledge base, the problem changes to GenAI with grounding.

```
Client call -> Internal API/application -> AWS model/service -> classification or response -> queue/attendant
```

## Architectural reasoning

### Start with the business objective, not the model

In the exam, well-formulated questions describe an operational need: reduce service time, summarize documents, detect fraud, organize images or improve internal search. The correct architectural decision arises from the expected result. If the outcome is numerical prediction, an LLM is probably not the best option. If the result is contextualized text, a foundation model might make sense.

### Separate ML platform from ready-made AI service

Out-of-the-box services are ideal when the problem is already well represented by a common case, such as OCR, translation or sentiment analysis. ML platforms come in when the business needs to train, adjust, evaluate and deploy its own model. This distinction is central to the AIF-C01.

## Best practices

- Define the success metric before choosing the service.
- Treat training and inference as phases with different costs and risks.
- Prefer managed services when heavy customization is not a requirement.
- Keep data, models and permissions under governance from the start.
- Perform human review on critical or regulated tasks.

## Exam tips

- If the question talks about creating new content, think first about GenAI and foundation models.
- If you talk about predicting or classifying based on labeled history, think about supervised ML.
- If the company doesn't want to manage infrastructure or train models, Bedrock usually gains traction.
- If the statement calls for fine control of the ML cycle, SageMaker AI tends to be the way to go.

## Common pitfalls

- Confusing generative AI with any type of intelligent automation.
- Assuming that every AI use case requires its own model training.
- Assuming that inference and training have the same cost and latency profile.
- Ignore IAM and security by being in an introductory module.

## Summary for review

- AI is the umbrella; ML is a subset; Generative AI creates new content.
- Training teaches; inference answers.
- Bedrock is AWS' strong point for consuming FMs via API.
- SageMaker AI is the platform for custom ML and lifecycle operation.
- Certification values managed choices aligned to the use case.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Continue to [Module 02 — Fundamentals of Generative AI](../02-Generative-AI-Fundamentals/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
