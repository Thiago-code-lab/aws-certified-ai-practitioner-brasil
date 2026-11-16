# Module 11 — AI Security and Compliance

AI security is not an isolated module: it cuts across data, model, prompt, identity, logs and integration. The exam likes precisely this systemic view.

## Objective

Enable you to identify security and compliance controls applicable to AI solutions on AWS, focusing on access, encryption, auditing, sensitive data, and separation of environments.

## How this topic appears on AIF-C01

- Relate IAM, KMS, CloudTrail and secrets to AI workloads.
- Understand data protection at rest, in transit and during use.
- Recognize when the case calls for review of access, PII and auditing.

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
| AWS IAM | Identity and permission control. | Access base for data, models and applications. |
| AWS KMS | Key management and encryption. | Important in protecting sensitive data. |
| AWS CloudTrail | Audit of actions and use of services. | Relevant in governance and investigation. |
| AWS Secrets Manager | Protection of secrets used by the application. | Important in integrations with APIs and databases. |

## Essential concepts

### Shared responsibility in AI

Even using managed services, the customer remains responsible for identity, permissions, sent data, integrations and application policies. In generative AI, this includes prompts, connected documents, secrets, logs, and usage decisions.

### Data protection around the model

It's not enough to encrypt the bucket. You need to control who can read documents, call models, access logs, change prompts and query results. AI security is application-wide security.

### Compliance and evidence

In regulated contexts, the company needs to show how it protects data, tracks access and reacts to incidents. CloudTrail, data classification, change trail, and environment separation help produce this evidence.

## Practical example

### Assistant with sensitive documents

A legal team wants to use internal documents in an assistant. In addition to the generative part, the architecture needs to isolate buckets, apply least-privilege IAM permissions, encryption with KMS and access and change audit trail.

## Architectural reasoning

### AI security and control composition

The correct answer is rarely a single service. Secure design typically combines IAM, KMS, CloudTrail, Secrets Manager, private S3, network policy, and AI service-specific controls.

### Compliance depends on traceability

When the question talks about auditing, investigation or evidence of compliance, think about logs, trails, versioning and segregation of responsibilities. Compliance is not just born from encryption.

## Best practices

- Apply principle of least privilege for models, data and integrations.
- Encrypt sensitive data and secrets with appropriate managed services.
- Use CloudTrail to create an audit trail of relevant actions.
- Separate development, approval and production environments and permissions.
- Periodically review who can access documents and databases used by AI.

## Exam tips

- IAM is the strong answer when the problem is authorization.
- KMS appears when the requirement talks about keys and managed encryption.
- Secrets Manager protects application credentials and tokens.
- CloudTrail helps when the question talks about auditing or investigation.

## Common pitfalls

- Think that Guardrails solve all the security of the solution.
- Storing secrets in an environment variable without adequate governance.
- Mix test and production environments with the same sensitive data.
- Bypass audit trail in AI applications.

## Summary for review

- AI security is data, identity, integration and operation security.
- Shared responsibility continues to apply in Bedrock and SageMaker AI.
- IAM, KMS, Secrets Manager and CloudTrail are frequent parts in the exam.
- Compliance requires evidence and traceability.
- Secure generative application goes beyond the model.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Additional review: [Module 10 — Generative AI on AWS](../10-Generative-AI-on-AWS/README.md).
- Continue to [Module 12 — Use Cases and Architectures](../12-AI-Use-Cases-and-Architectures/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> As a practical complement to understanding data feeding AI in the cloud, see the course [Data Engineering on AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
