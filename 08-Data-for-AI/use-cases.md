# Use Cases — Module 08: Data for AI

## Case 1 — Regulatory knowledge base

**Scenario:** A company needs to answer questions based on standards that change frequently.

**Suggested architecture:** Continuous curation, versioning, metadata and document base update flow in S3.

**Why this choice makes sense:** Regulatory knowledge ages quickly and needs processing, not just storage.

**Associated exam trap:** Relying on unorganized PDFs without a catalog.

## Case 2 — Sensitive documents

**Scenario:** An area wants to connect reports with PII to a generative assistant.

**Suggested architecture:** Classify data, reduce exposure, apply access control and evaluate whether all content should actually enter the database.

**Why this choice makes sense:** Not every piece of data that exists should be used by the model.

**Associated exam trap:** Opening the entire base to AI for convenience.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> As a practical complement to understanding data feeding AI in the cloud, see the course [Data Engineering on AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
