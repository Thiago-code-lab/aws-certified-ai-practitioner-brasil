# Cheatsheet — Module 02: Generative AI Fundamentals

> Quick review designed for the final review of the AWS Certified AI Practitioner exam.

## At a glance

| Topic | What to remember | Exam trap |
| --- | --- | --- |
| Prompt engineering | Improves instructions and formatting of the response. | Not to be confused with model adjustment. |
| RAG | Retrieves external context before generation. | It is not synonymous with fine-tuning. |
| Temperature | Controls output variability. | Higher temperature does not mean more correct answer. |
| Hallucination | Plausible content, but incorrect or invented. | A good model can still hallucinate. |

## Practical rules

- Specify role, objective, context and output format in the prompt.
- Use grounding when the answer depends on internal or recent information.
- Prefer more conservative parameters in operational and structured tasks.
- Monitor latency, cost per token and perceived quality.

## Memory cues

- Prompt = instruction; RAG = context; Guardrails = policy.
- High creativity comes at the cost of predictability.
- Internal documents require grounding.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect this subject with real data architectures in AWS, also consult the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
