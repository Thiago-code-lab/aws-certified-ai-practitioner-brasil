# Module 10 — Generative AI on AWS

In this module you connect GenAI concepts to application architecture: front-end, authentication, backend, observability, document bases and integration services in AWS.

## Objective

Build architectural reasoning for generative applications on AWS, understanding typical components, integrations, and cost, latency, and security decisions.

## How this topic appears on AIF-C01

- Describe application-oriented GenAI architectures.
- Choose managed components on AWS for orchestration and delivery.
- Connect model, data, API, observability and security.

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
| Amazon Bedrock | FM layer and generative resources. | Central component of the application. |
| AWS Lambda | Serverless backend for orchestration and model calls. | Appears when the case calls for operational simplicity. |
| Amazon API Gateway | Exposure of APIs for front-ends and integrations. | Very common in web architectures. |
| Amazon CloudWatch | Solution logs, metrics and alarms. | Important for operation and troubleshooting. |

## Essential concepts

### Typical flow of a GenAI application

The user sends a request; the application authenticates the user, prepares the context, queries the knowledge base when necessary, calls the model and records logs and metrics. In many cases, the best architecture is serverless and managed services oriented.

### Synchronous, asynchronous and batch

A real-time chat usually requests a synchronous call to the model. Large document processing can be asynchronous or batch. The exam often differentiates these modes by latency, user experience, and cost.

### Fallback and observability

Mature applications do not assume that the model will always respond well. They monitor error, response time and cost, and can fall back to human review, a processing queue, or a simplified response in case of failure.

## Practical example

### Corporate portal with knowledge assistant

The employee accesses a web portal, authenticates with corporate identity, sends questions via API, the backend retrieves relevant context and calls the model in Bedrock. Logs and metrics go to CloudWatch, while documents are versioned in S3.

## Architectural reasoning

### Serverless to speed up delivery and reduce operations

For most study and exam scenarios, API Gateway + Lambda + Bedrock + S3 + CloudWatch offer an excellent balance between simplicity, governance and implementation speed.

### Choose synchronous or asynchronous for the expected experience

If the user expects immediate response, the architecture needs to be optimized for low latency. If the task is to analyze a batch of documents or generate reports, asynchronous may be better. The exam likes this distinction.

## Best practices

- Isolate the model call in a well-defined layer of the application.
- Record logs, latency metrics and failures from the first deployment.
- Use API Gateway and Lambda when load and profile favor serverless.
- Control what goes to the prompt and what comes back from the model.
- Design fallback for timeout, model error or low confidence.

## Exam tips

- GenAI architectures on AWS typically combine Bedrock, S3, API, and observability.
- Synchronous serves chat and assistants; Asynchronous serves large documents and long workflows.
- Managed services tend to be the preferred answer when the requirement does not call for deep infrastructure control.
- Security and logging are integral parts of the architecture.

## Common pitfalls

- Calling the model directly from the front-end without control layer.
- Failing to provide timeout, fallback queue or error handling.
- Ignoring cost per token on high volume flows.
- Mixing sensitive data without access policy.

## Summary for review

- A GenAI application is a complete system that includes much more than model calls.
- Serverless is usually an excellent starting point on AWS.
- Synchronous and asynchronous must follow the use case.
- Observability and fallback increase robustness.
- Documents, identity and logs are as important as the model.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 09 — Prompt Engineering](../09-Prompt-Engineering/README.md).
- Continue to [Module 11 — Security and Compliance in AI](../11-AI-Security-and-Compliance/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
