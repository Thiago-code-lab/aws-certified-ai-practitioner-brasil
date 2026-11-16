# Use Cases — Module 11: AI Security and Compliance

## Case 1 — Customer data in internal assistant

**Scenario:** The company wants to use an assistant with a history of clients and contracts.

**Suggested architecture:** Private S3, least-privilege IAM permissions, KMS, audit logs and scope review of data sent to the model.

**Why this choice makes sense:** The safe solution starts before the model call.

**Associated exam trap:** Focusing only on the interface and forgetting the data.

## Case 2 — Corporate API integrated into the bot

**Scenario:** The assistant queries an ERP and needs secure credentials.

**Suggested architecture:** Store secrets in Secrets Manager and control access through the application role.

**Why this choice makes sense:** Secure integration is part of AI security.

**Associated exam trap:** Token hardcode in code or prompt.


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To connect this subject with real data architectures in AWS, also consult the course [Data Engineering in AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
