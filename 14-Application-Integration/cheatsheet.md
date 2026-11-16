# Cheatsheet — Module 14: Integration with Applications

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| API Gateway + Lambda | Controlled AI exposure via API. | Do not expose direct call to the model without mediation. |
| SQS | Queue for decoupling and background processing. | Do not use when immediate latency is a central requirement. |
| EventBridge | Event-driven integration. | Not to be confused with work queue. |
| Retry | Important in transient faults. | Without care it can duplicate the effect in non-idempotent processes. |

## Practical rules

- Use synchronous integration only when the experience really requires immediate response.
- Decouple long tasks with events and queues.
- Standardize API contracts and response formats.
- Apply retries and exception handling at predictable points.

## Memory cues

- Real time? synchronous. Long process? queue or event.
- App layer organizes and protects AI.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
