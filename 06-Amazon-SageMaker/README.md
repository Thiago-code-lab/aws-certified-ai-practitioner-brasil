# Module 06 — Amazon SageMaker AI

SageMaker AI appears when the problem stops being just using a ready-made model and starts requiring data preparation, training, evaluation, deployment and operation of ML at scale.

## Objective

Understand the role of SageMaker AI in the AWS ecosystem, including Studio, Canvas, JumpStart, training, inference types, and its practical differences from Bedrock.

## How this topic appears on AIF-C01

- Identify when the statement asks for customized ML or model life cycle.
- Distinguish between training, deployment and monitoring in SageMaker AI.
- Compare no-code and assisted approaches with more technical workflows.

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
| Amazon SageMaker AI | End-to-end platform for ML. | Appears when there is a need to build and operate customized models. |
| SageMaker Studio | Integrated environment for experimentation and development. | It can appear as a work interface for data scientists. |
| SageMaker Canvas | ML experience for non-code-focused analysts. | Appears in ML democratization scenarios. |
| SageMaker JumpStart | Preconfigured models and solutions. | Helps accelerate adoption without starting from scratch. |

## Essential concepts

### ML Lifecycle in SageMaker AI

SageMaker AI covers data preparation, experimentation, training, tuning, deployment, monitoring and governance. This differentiates it from point services: the proposal is to serve as an operational platform for ML workloads.

### Inference options

Inference can be real-time, serverless, asynchronous, or batch. The AIF-C01 doesn't go into deep tuning details, but it expects you to understand when an intermittent load calls for serverless and when large, time-tolerant processing calls for batch.

### SageMaker AI vs Bedrock

If the problem is using managed FMs, Bedrock is the strongest name. If the problem is building, training and operating custom models, SageMaker AI takes the lead. In many questions, the key is to read whether the company wants to consume ready-made AI or develop its own ML pipeline.

## Practical example

### Demand forecast with own historical data

A company has a detailed sales history and wants to train a specific model for its context. In this case, the need stops being just consuming an FM and starts involving data preparation, experimentation, adjustment and implementation. This is classic SageMaker AI territory.

## Architectural reasoning

### Canvas to democratize, Studio to deepen

Canvas makes sense when business users need to create predictions or rankings without intense programming. Studio makes sense for technical teams that need notebooks, pipelines, tuning and deeper integration.

### Choose the inference mode based on load behavior

If the load is sporadic and sensitive to idle cost, serverless makes sense. If continuous and stable response is required, real-time endpoint may be more suitable. If the job processes large batches offline, batching is often the natural answer.

## Best practices

- Clearly define whether the problem requires a customized model or a ready-made managed service.
- Use S3 as an organized base for datasets and artifacts.
- Choose the inference mode according to latency, cost and traffic pattern.
- Maintain traceability of experiments and model versions.
- Avoid operating permanent capacity when the load is intermittent.

## Exam tips

- Canvas appears when the company wants ML without heavy code.
- JumpStart accelerates prototyping with pretrained models and ready-made solutions.
- Batch inference is different from real-time endpoint.
- If the question is about training and operating your own ML, think about SageMaker AI.

## Common pitfalls

- Confusing the use of FM via API with a complete custom ML cycle.
- Choose real-time endpoint for fully batch load.
- Ignore costs of keeping capacity always on.
- Thinking that Canvas eliminates the need for well-prepared data.

## Summary for review

- SageMaker AI is end-to-end ML platform.
- Canvas, Studio and JumpStart meet different profiles and needs.
- Training and inference are distinct phases within the platform.
- The choice of inference mode affects cost and latency.
- Bedrock and SageMaker AI do not always compete; they often complement each other.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Additional review: [Module 05 — Amazon Bedrock](../05-Amazon-Bedrock/README.md).
- Continue to [Module 07 — Responsible AI and Governance](../07-Responsible-AI-and-Governance/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
