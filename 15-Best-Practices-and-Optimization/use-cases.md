# Use Cases — Module 15: Best Practices and Optimization

## Case 1 — Repetitive FAQ

**Scenario:** The assistant answers many of the same questions every day.

**Suggested architecture:** Caching for stable responses and reviewing the need for the more expensive model.

**Why this choice makes sense:** Not every response needs to be generated from scratch with each call.

**Associated exam trap:** Scale only by increasing capacity and cost.

## Case 2 — Nightly report

**Scenario:** The operations area generates a daily summary for managers.

**Suggested architecture:** Batch flow with processing outside critical hours.

**Why this choice makes sense:** Online latency is not a requirement; cost and predictability matter more.

**Associated exam trap:** Insisting on real time with no value for the business.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Optional in-depth: data pipelines and fundamentals in AWS appear in the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
