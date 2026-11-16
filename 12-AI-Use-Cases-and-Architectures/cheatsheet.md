# Cheatsheet — Module 12: Use Cases and Architectures

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| Textract | Extracts text, tables and forms. | It extracts document content; use a generative model for a free-form summary. |
| Comprehend | Managed NLP for common tasks. | Not to be confused with generative chatbot. |
| Rekognition | Managed computer vision. | Do not use for full document OCR when Textract is more appropriate. |
| Bedrock | Flexible generation and interaction with FM. | Do not assume that every task requires a generative model. |

## Practical rules

- Read the main verb of the case: extract, classify, generate, respond, moderate, recommend.
- Prefer the more specialized service when it meets the requirement directly.
- Combine pipeline services when the case requires more than one capacity.
- Evaluate cost, latency, governance and maintenance of the design.

## Memory cues

- Extract -> Textract. View image -> Rekognition. Analyze text -> Comprehend. Generate/Respond -> Bedrock.
- Dominant requirement decides the main service.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Optional in-depth: data pipelines and fundamentals in AWS appear in the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
