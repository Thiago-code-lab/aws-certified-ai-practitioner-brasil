# Use Cases — Module 10: Generative AI on AWS

## Case 1 — Internal knowledge portal

**Scenario:** Authenticated users ask questions about company policies and processes.

**Suggested architecture:** Web portal with API Gateway, Lambda, Bedrock, S3 and CloudWatch.

**Why this choice makes sense:** Serverless architecture reduces operations and maintains centralized control.

**Associated exam trap:** Expose the model directly to the browser.

## Case 2 — Contract processing

**Scenario:** A legal department needs to summarize hundreds of contracts every night.

**Suggested architecture:** Asynchronous pipeline with S3 storage, orchestration and inference outside the interactive path.

**Why this choice makes sense:** The user does not expect an instant response; cost and robustness matter more than real-time chat.

**Associated exam trap:** Design everything as synchronous request.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> If this module raises questions about pipelines, data lakes and processing in AWS, use the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9) as a complement.
