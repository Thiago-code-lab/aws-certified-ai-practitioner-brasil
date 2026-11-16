# Use Cases — Module 03: Machine Learning Fundamentals

## Case 1 — Risk score

**Scenario:** A fintech wants to predict probability of default based on labeled history.

**Suggested architecture:** Supervised ML with data pipeline in S3 and training cycle in SageMaker AI.

**Why this choice makes sense:** There is a known target and a need to predict a future event.

**Associated exam trap:** Choosing clustering just because there are many customers.

## Case 2 — Profile mapping

**Scenario:** An e-commerce company wants to discover natural customer segments before launching campaigns.

**Suggested architecture:** Unsupervised learning to cluster behavior profiles.

**Why this choice makes sense:** The goal is not to predict a known class, but to reveal structure in the data.

**Associated exam trap:** Insist on classification with no label available.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Anyone who wants to reinforce the ingestion, storage and processing part of AWS can use the course [Data Engineering at AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9) as a parallel track.
