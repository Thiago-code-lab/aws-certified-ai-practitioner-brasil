# Warm Up Questions — AIF-C01

## Question 01

**Question:** In a document-based scenario that changes weekly, which approach is best suited for updated responses?

- A) RAG with context retrieval
- B) Fine-tuning with each update
- C) Removal of audit logs
- D) Replace IAM with Guardrails

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
RAG separates dynamic knowledge from model training, reducing cost and update time.

**Why option B is wrong:**
Recurrent fine-tuning for document updating tends to increase operational costs and complexity.

</details>

## Question 02

**Question:** Which AWS service is best suited for applying content policies to GenAI apps with Bedrock?

- A) AWS KMS
- B) Amazon Bedrock Guardrails
- C) Amazon Route 53
- D) Amazon CloudFront

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** B

**Explanation:**
Guardrails controls themes and content patterns in inputs and outputs of generative applications.

**Why option A is wrong:**
KMS is about key management and encryption, not semantic content policy.

</details>

## Question 03

**Question:** To identify sensitive data in S3 buckets, which service is the best fit?

- A) Amazon Macie
- B) Amazon Rekognition
- C) Amazon Polly
- D) Amazon SQS

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
Amazon Macie is designed for discovery and classification of sensitive data in S3.

**Why option B is wrong:**
Rekognition is aimed at computer vision, not classifying PII in storage.

</details>

## Question 04

**Question:** In inference with unpredictable traffic, which decision tends to reduce idle cost?

- A) Maintain fixed maximum capacity
- B) Use a larger model by default
- C) On-demand inference with elastic capacity
- D) Always increase context

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** C

**Explanation:**
Elastic capacity reduces idle capacity when traffic is intermittent.

**Why option A is wrong:**
Maximum fixed capacity increases expense in periods of low usage.

</details>

## Question 05

**Question:** Which pair of services best serves secret protection and data encryption?

- A) Secrets Manager + AWS KMS
- B) CloudFront + Route 53
- C) Textract + Comprehend
- D) Budgets + Cost Explorer

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
Secrets Manager protects credentials; KMS manages keys for data encryption.

**Why option B is wrong:**
CloudFront and Route 53 resolve delivery and DNS, not secret and key management.

</details>

## Question 06

**Question:** In responsible AI for sensitive decisions, which practice is a priority?

- A) Human review of critical decisions
- B) Unrestricted automation
- C) Disable audit trails
- D) Increase temperature to diversify answers

<details>
<summary><strong>See answer</strong></summary>

✅ **Correct answer:** A

**Explanation:**
Human-in-the-loop reduces risk in high-impact scenarios and improves governance.

**Why option B is wrong:**
Unrestricted automation in sensitive decisions violates responsible AI principles.

</details>

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
