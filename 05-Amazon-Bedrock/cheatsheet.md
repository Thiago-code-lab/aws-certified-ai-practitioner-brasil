# Cheatsheet — Module 05: Amazon Bedrock

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| Bedrock | Managed layer for FMs. | Not to be confused with complete customized training. |
| Knowledge Bases | Grounding/RAG managed. | It does not replace document governance. |
| Guardrails | Entry and exit policy. | It does not replace IAM. |
| Agents | Orchestrate tasks and tools. | They do not remove the need to validate workflows. |

## Practical rules

- Use Bedrock when the priority is to consume FMs quickly with managed governance.
- Apply Guardrails to reduce out-of-policy responses and undue exposure.
- Connect Knowledge Bases to controlled and updated document sources.
- Monitor cost per token, latency and error rates.

## Memory cues

- Bedrock accelerates FM usage; Guardrails discipline; KB reasons; Agents execute.
- Content governance does not eliminate access governance.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> As a practical complement to understanding data feeding AI in the cloud, see the course [Data Engineering on AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).

> **Service availability note (November 16, 2026):** The source references Amazon Bedrock Agents, now **Amazon Bedrock Agents Classic**, which is closed to new sign-ups. Existing customers can continue using it. For new agent implementations, review [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) and the [Agents availability notice](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).
