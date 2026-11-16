# Use Cases — Module 01: Introduction to AI and ML

## Case 1 — Call center

**Scenario:** An operation wants to prioritize urgent tickets and summarize the customer's history for the agent.

**Suggested architecture:** Supervised classification or NLP service for prioritization, combined with an FM for contextual summarization.

**Why this choice makes sense:** The case mixes two natures of problem: structured classification and text generation. The right architecture can use different components instead of forcing everything into a single model.

**Associated exam trap:** Wanting to solve the entire solution with just a generic chatbot.

## Case 2 — Catalog of internal documents

**Scenario:** A legal team wants to answer questions about internal policies without publicly exposing sensitive documents.

**Suggested architecture:** Application with Bedrock, document base in S3 and grounding/RAG mechanism with access control via IAM.

**Why this choice makes sense:** The main challenge is contextualized response with data governance, not model training from scratch.

**Associated exam trap:** Assuming that uploading PDFs to a bucket alone already solves intelligent search.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To deepen the database behind AI solutions on AWS, it is also worth studying the course [Data Engineering on AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
