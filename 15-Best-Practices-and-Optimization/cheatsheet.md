# Cheatsheet — Module 15: Best Practices and Optimization

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| Smaller model | Prefer when it already meets the objective. | Don't assume that bigger is always better. |
| Cache | Good for repeated responses. | Do not use without thinking about the validity of the content. |
| Batch | Great when the response doesn't need to be immediate. | Don't force real time unnecessarily. |
| Budgets/Cost Explorer | Support visibility and control of spending. | Unmonitored costs can grow quickly. |

## Practical rules

- Choose the smallest model that meets the requirement.
- Limit context and response size to what is necessary.
- Use caching for repeated questions and stable answers.
- Monitor cost, latency, failures and reuse rate.

## Memory cues

- Smaller prompt + suitable model + right context = savings.
- Always measure; optimize later with real data.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
