# Cheatsheet — Module 10: Generative AI on AWS

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| API Gateway | API exposure for app and integrations. | Do not let the client call the model directly without control. |
| Lambda | Lightweight, serverless orchestration. | Evaluate timeout and payload. |
| CloudWatch | Application logs and metrics. | Without observability, the operation is blind. |
| S3 | Document collection and artifacts. | Without curation and permissions, it becomes a risk. |

## Practical rules

- Isolate the model call in a well-defined layer of the application.
- Record logs, latency metrics and failures from the first deployment.
- Use API Gateway and Lambda when load and profile favor serverless.
- Control what goes to the prompt and what comes back from the model.

## Memory cues

- GenAI App = interface + API + context + model + logs.
- Serverless speeds up; fallback protects.
- Desired latency defines the integration style.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
