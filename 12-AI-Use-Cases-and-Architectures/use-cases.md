# Use Cases — Module 12: Use Cases and Architectures

## Case 1 — Contract analysis

**Scenario:** A legal team needs to extract fields and generate an executive summary.

**Suggested architecture:** Textract for structured OCR and Bedrock for contextualized textual summarization.

**Why this choice makes sense:** Each part of the problem uses the most appropriate service.

**Associated exam trap:** Choosing a single service for all stages unnecessarily.

## Case 2 — Image moderation

**Scenario:** A platform wants to block inappropriate visual content uploaded by users.

**Suggested architecture:** Rekognition for image analysis and moderation.

**Why this choice makes sense:** It's a case of managed computer vision, not chatbot or textual LLM.

**Associated exam trap:** Using textual Bedrock for a straightforward visual problem.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
