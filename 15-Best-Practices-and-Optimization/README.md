# Module 15 — Best Practices and Optimization

After understanding services and architectures, all that remains is to learn how to operate them well. The exam focuses heavily on the idea of efficiency: achieving objectives with lower cost, lower risk and less unnecessary complexity.

## Objective

Review optimization practices for AI applications on AWS, focusing on cost, latency, evaluation, observability, governance and conscious choice of models.

## How this topic appears on AIF-C01

- Control inference cost and context.
- Understand model choice, cache, batch and fallback.
- Operate AI with continuous evaluation and monitoring.

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
| Amazon CloudWatch | Observability of usage, latency and failures. | Basis of operation and troubleshooting. |
| AWS Budgets | Cost and consumption alerts. | Important for financial governance. |
| AWS Cost Explorer | Analysis of expenditure by service and consumption pattern. | Help with financial optimization. |
| Amazon Bedrock / SageMaker AI | Platforms where model and inference decisions impact cost. | Appear in efficiency comparisons. |

## Essential concepts

### AI cost doesn’t just come from the model

The total cost involves call volume, prompt size, response size, frequency, storage, data pipelines, and integration components. On the exam, the common mistake is to only look at the main service.

### Latency, quality and cost as trade-offs

More powerful models may cost more and respond more slowly. Smaller models or shorter responses can reduce cost and improve response time. The best choice depends on the actual need of the use case.

### Continuous assessment and observability

AI applications need to be measured. It's not enough to say that they work. Monitoring latency, failures, cost, user satisfaction and error patterns helps improve quality and avoid surprises in production.

## Practical example

### Cost-controlled FAQ assistant

A company can use lean context, objective prompts, limited answers, FAQ caching, and fallback for simple search when the question does not require rich generation. This reduces cost and improves predictability.

## Architectural reasoning

### Use the smallest model that solves the problem

Certification tends to value efficient choices. If a smaller model meets the required quality, it may be a better option than a larger, more expensive model. This is especially true for repetitive and standardized tasks.

### Cache, batch and context selection save a lot

Not every question needs to generate everything again. Repeated questions may be served by caching. Partition caches by the relevant access scope, and expire cached answers when source documents or permissions change. Offline processes can run in batches. And excessive context increases cost without necessarily increasing quality.

## Best practices

- Choose the smallest model that meets the requirement.
- Limit context and response size to what is necessary.
- Use caching for repeated questions and stable answers.
- Monitor cost, latency, failures and reuse rate.
- Create simple evaluation set to compare prompt and architecture versions.

## Exam tips

- AI cost also comes from the volume of tokens and calls.
- Batch can be better than real time when the user doesn't have to wait.
- Caching and selective grounding are classic optimization levers.
- CloudWatch, Budgets and Cost Explorer support financial and technical operation.

## Common pitfalls

- Always choosing the most advanced model by reflex.
- Sending excessive context without measuring quality return.
- Operate without minimum cost and latency metrics.
- Ignoring objective evaluation before changing prompts or architecture.

## Summary for review

- Optimizing AI is about balancing cost, latency and quality.
- A bigger model is not always a better decision.
- Cache, batch and lean context save a lot.
- Observability and continuous evaluation are part of operational maturity.
- The exam values efficiency with managed services.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 14 — Integration with Applications](../14-Application-Integration/README.md).
- Continue to [Module 16 — Practice Exams and Questions](../16-Practice-Exams-and-Questions/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
