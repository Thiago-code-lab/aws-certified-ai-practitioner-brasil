# Use Cases — Module 14: Integration with Applications

## Case 1 — Batch document classification

**Scenario:** A company receives PDFs in bulk and supports background processing.

**Suggested architecture:** S3 + queue + processing backend + result storage.

**Why this choice makes sense:** Resilience and decoupling are more important than immediate response.

**Associated exam trap:** Implement everything as synchronous call.

## Case 2 — Internal service chat

**Scenario:** The user expects a response in a few seconds.

**Suggested architecture:** Synchronous API with controlled backend, observability and fallback.

**Why this choice makes sense:** Interactive experience calls for low latency design.

**Associated exam trap:** Sending the user to asynchronous flow unnecessarily.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
