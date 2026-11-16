# Cheatsheet — Module 04: Foundation Models and LLMs

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| LLM | Foundation model focused on language. | Not every FM is an LLM. |
| Embedding | Vector representation of meaning. | It does not generate a final response to the user. |
| Vector database | Stores vectors and allows similarity search. | It does not replace the entire data layer of the system. |
| RAG | Retrieves context and then generates. | It's not model training. |

## Practical rules

- Use chunking consistent with the structure of the document.
- Store useful metadata to filter context before retrieval.
- Reevaluate the vector database when documents are updated.
- Clearly separate the retrieve function from the generate function.

## Memory cues

- Represent first, retrieve next, generate last.
- Dynamic knowledge suits RAG more than fine-tuning.
- Vector database is retrieval support, not the official origin of the data.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
