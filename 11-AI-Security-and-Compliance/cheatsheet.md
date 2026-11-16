# Cheatsheet — Module 11: AI Security and Compliance

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| IAM | Least privilege and access control. | Do not replace with content filters. |
| KMS | Key management and encryption. | Encryption does not replace authorization. |
| Secrets Manager | Stores secrets with rotation and control. | Do not hard-code credentials. |
| CloudTrail | Audit trail. | Without appropriate logs, important audit evidence can be missing. |

## Practical rules

- Apply the principle of least privilege for models, data and integrations.
- Encrypt sensitive data and secrets with appropriate managed services.
- Use CloudTrail to create an audit trail of relevant actions.
- Separate development, approval and production environments and permissions.

## Memory cues

- Secure model = secure data + secure access + auditable operation.
- Guardrails help with content; IAM helps with who can do what.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
