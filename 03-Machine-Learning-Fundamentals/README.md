# Module 03 — Machine Learning Fundamentals

AIF-C01 doesn't require heavy math, but it does require you to understand how ML learns from data and why data quality, labels, and evaluation matter.

## Objective

Consolidate the ML pillars that appear in the test: supervised and unsupervised learning, overfitting, datasets, metrics and choice between ready-made service and customized model.

## How this topic appears on AIF-C01

- Differentiate between classification, regression and clustering.
- Understand training, validation and test sets.
- Relate data preparation with result quality.

## Module navigation

- [README](./README.md)
- [Cheatsheet](./cheatsheet.md)
- [Flashcards](./flashcards.md)
- [Questions](./questions.md)
- [Use cases](./use-cases.md)
- [Practical lab](./lab.md)
- [Official links](./links.md)

## Core AWS Services

| AWS Service | Role in the module | How it appears on the exam |
| --- | --- | --- |
| Amazon SageMaker AI | Training, experimentation and implementation of customized models. | It appears when the company needs to build its own ML. |
| Amazon SageMaker Canvas | Low-code/no-code experience for business users. | Shows the possibility of ML without heavy coding. |
| Amazon SageMaker Ground Truth | Data labeling for supervised training. | May appear in questions about dataset quality. |
| Amazon S3 | Common data lake for training and inference datasets. | Frequent component in ML architectures. |

## Essential concepts

### Supervised, unsupervised and reinforcement

Supervised learning uses labeled examples to predict class or value. Unsupervised learning finds unlabeled patterns such as clusters. Reinforcement learning optimizes decisions based on rewards. For AIF-C01, supervised and unsupervised are the most recurrent.

### Training, validation and testing datasets

Training fits the model. Validation helps you choose hyperparameters and compare versions. Testing measures performance on unseen data. On the exam, the central idea is to avoid illusion of quality: evaluating on the same data used for training can mask failures.

### Overfitting and underfitting

Overfitting happens when the model learns too many details from training and generalizes poorly. Underfitting occurs when it is too simple to capture the pattern. Both appear as risks linked to data, model complexity and evaluation method.

## Practical example

### Churn prediction versus customer segmentation

Predicting churn with labeled history is a case of supervised classification. Dividing customers into groups with similar behaviors without prior labeling is clustering, therefore unsupervised.

```
Historical data -> preparation -> supervised training -> churn score
Unlabeled data -> clustering -> customer segments
```

## Architectural reasoning

### Choose the type of learning from the available data

If there are past examples with correct answer, the trend is supervised. If the goal is to find hidden patterns with no ready answer, unsupervised gains traction. The exam often describes this in business language rather than academic names.

### Quality data overcomes misdirected complexity

In real architectures, preparing the data well usually has a greater impact than replacing the model with a more sophisticated one without need. In the AWS context, this connects to S3, data pipelines, and proper labeling.

## Best practices

- Confirm whether the problem is classification, regression or clustering before choosing the technique.
- Separate training, validation and testing to measure generalization.
- Take care of the quality of labels and the consistency of the dataset.
- Choose metrics consistent with the business, not just accuracy.
- Maintain traceability between data used, model trained and result obtained.

## Exam tips

- Classification predicts class; regression predicts continuous value; clustering groups without label.
- Ground Truth appears when the topic is supervised labeling.
- High accuracy alone can be misleading in unbalanced datasets.
- Custom ML tends to point to SageMaker AI.

## Common pitfalls

- Confusing clustering with classification.
- Assuming unlabeled historical data allows supervised prediction immediately.
- Interpret training performance as proof of generalization.
- Ignoring that bad data produces bad models.

## Summary for review

- Supervised learns with label; unsupervised finds unlabeled structure.
- Training, validation and testing exist to avoid self-deception.
- Overfitting and underfitting both limit generalization.
- Ground Truth helps in the labeling stage.
- SageMaker AI is the service most associated with custom ML on AWS.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 02 — Fundamentals of Generative AI](../02-Generative-AI-Fundamentals/README.md).
- Continue to [Module 04 — Foundation Models and LLMs](../04-Foundation-Models-and-LLMs/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
