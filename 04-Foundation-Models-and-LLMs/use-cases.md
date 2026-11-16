# Use Cases — Module 04: Foundation Models and LLMs

## Case 1 — Search in internal policies

**Scenario:** Employees need to receive responses based on current company policies.

**Suggested architecture:** RAG with documents in S3, embeddings, vector index and LLM to compose the final response.

**Why this choice makes sense:** Knowledge comes from documents, dynamic and needs traceability.

**Associated exam trap:** Choose only static prompt with no retrieval mechanism.

## Case 2 — Catalog of similar products

**Scenario:** A marketplace wants to suggest semantically similar products even when the textual description changes.

**Suggested architecture:** Embeddings to represent descriptions and vector mechanism to retrieve similar items.

**Why this choice makes sense:** Similarity by meaning is more important than exact words.

**Associated exam trap:** Relying only on lexical search.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> If this module raises questions about pipelines, data lakes and processing in AWS, use the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9) as a complement.
