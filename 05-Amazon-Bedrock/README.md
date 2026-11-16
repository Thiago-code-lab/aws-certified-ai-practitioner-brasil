# Module 05 — Amazon Bedrock

Amazon Bedrock is one of the central services in this certification for generative AI on AWS. The exam tests what it solves, when to use it, and how to integrate it with security and governance.

## Objective

Master the role of Bedrock as a managed platform for foundation models, including Knowledge Bases, Guardrails, Agents and selection criteria against SageMaker AI or your own infrastructure.

## How this topic appears on AIF-C01

- Consume foundation models without managing infrastructure.
- Understand Knowledge Bases, Guardrails and Agents.
- Relate Bedrock to cost, latency, security and speed of delivery.

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
| Amazon Bedrock | Main layer for accessing foundation models via API. | GenAI blueprint core service. |
| Amazon Bedrock Knowledge Bases | Managed grounding for RAG. | Appears when the statement talks about responding based on documents. |
| Amazon Bedrock Guardrails | Security and policy controls on entry and exit. | Important in responsible AI and security scenarios. |
| Amazon Bedrock Agents | Orchestration of actions and use of tools for generative applications. | Useful when the model needs to perform steps beyond responding to text. |

## Essential concepts

### Bedrock as a managed layer

Bedrock abstracts the effort of hosting and scaling foundation models. Instead of operating clusters, endpoints and GPU capacity, the team consumes models through APIs and managed resources. This accelerates experimentation, prototyping and entry into production.

### Knowledge Bases, Guardrails and Agents

Knowledge Bases help connect documents and contextual retrieval. Guardrails can evaluate configured content filters, denied topics, and sensitive information such as PII. They reduce risk but do not guarantee policy compliance for every response. Agents allow the model to activate tools and perform actions on connected systems, expanding the application's usefulness.

### When Bedrock appears as the best answer

When the statement prioritizes operational simplicity, speed in using FMs, integration with AWS managed resources and reduction of infrastructure effort. If the question asks to train very specific models from scratch, the discussion shifts to SageMaker AI.

## Practical example

### Integrated assistant with a knowledge base and output protection

A company wants an assistant to answer questions about internal procedures, but needs to block PII leaks and keep answers within permitted topics. An architecture with Amazon Bedrock Knowledge Bases and Guardrails can support this design with low operational effort. Evaluate the filters and enforce document access permissions; these controls do not guarantee that every sensitive output is blocked.

```
User -> application -> Amazon Bedrock Guardrails -> Knowledge Base -> model -> filtered response
```

## Architectural reasoning

### Bedrock vs own infrastructure

Hosting a model directly on your own infrastructure increases control, but also increases operation, fixed costs and complexity. On the exam, if there is no explicit requirement for deep customization of the model layer, Bedrock tends to be more consistent with AWS's managed-first philosophy.

### Guardrails complement, not replace, safety

Guardrails help with generated content and application experience, but they do not replace IAM, encryption, logs, data segregation, and human review. The exam can explore this difference.

## Best practices

- Use Bedrock when the priority is to consume FMs quickly with managed governance.
- Apply Guardrails to reduce out-of-policy responses and undue exposure.
- Connect Knowledge Bases to controlled and updated document sources.
- Monitor cost per token, latency and error rates.
- Separate development, test and production permissions.

## Exam tips

- Bedrock = managed consumption of FMs; SageMaker AI = more customized ML cycle.
- Knowledge Bases appear when the problem speaks in internal documents.
- Guardrails control content, but do not do IAM or KMS.
- Agents enter when the statement requests action, flow or use of a tool.

## Common pitfalls

- Confusing Guardrails with identity access control.
- Assume that Knowledge Base replaces the curation of source documents.
- Use Amazon Bedrock Agents without thinking about observability and flow validation.
- Ignore inference cost and context size.

## Summary for review

- Bedrock delivers FMs via API with low operational overhead.
- Knowledge Bases connect grounding and retrieval.
- Guardrails help with content policy.
- Agents expand the application with actions and tools.
- The exam values Bedrock as a natural path to managed GenAI on AWS.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 04 — Foundation Models and LLMs](../04-Foundation-Models-and-LLMs/README.md).
- Continue to [Module 06 — Amazon SageMaker AI](../06-Amazon-SageMaker/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> **Service availability note (November 16, 2026):** The source references Amazon Bedrock Agents, now **Amazon Bedrock Agents Classic**, which is closed to new sign-ups. Existing customers can continue using it. For new agent implementations, review [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) and the [Agents availability notice](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).
