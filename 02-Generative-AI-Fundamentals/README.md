# Module 02 — Fundamentals of Generative AI

This module introduces the core concepts of generative AI: prompt, token, context, temperature, grounding and hallucination. This is one of the points where the exam requires practical clarity, not memorized definitions.

## Objective

Enable you to explain how a foundation model generates outputs, why responses can vary between calls, and what controls make a generative application more predictable, safe, and useful.

## How this topic appears on AIF-C01

- Understand the input-context-model-output flow.
- Differentiate prompt engineering, grounding, fine-tuning and guardrails.
- Recognize the risk of hallucination and how to mitigate it.

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
| Amazon Bedrock | Execution of foundation models and GenAI tools. | Core service for GenAI questions on AWS. |
| Amazon Nova | AWS model family available via Bedrock. | It can appear as a native AWS option for text, image and multimodality. |
| Amazon S3 | Common source of documents used for grounding and RAG. | Appears in flows with knowledge bases and data preparation. |
| Amazon CloudWatch | Observability of calls, latency and errors in GenAI applications. | Important when the statement calls for operational monitoring. |

## Essential concepts

### Tokens, context and context window

Language models process input and output as tokens. The larger the context sent, the higher the cost and, depending on the model, the latency. On the exam, this appears as a need to summarize, retrieve only what is necessary and avoid bloated prompts.

### Temperature, variation and predictability

Generation parameters change the level of creativity and diversity of the response. Lower temperatures favor consistency; higher temperatures favor variety. For operational tasks, the exam tends to value predictability, especially when there is structured output.

### Hallucination and grounding

Hallucination occurs when the model produces plausible but incorrect, incomplete, or invented content. Grounding reduces this risk by providing reliable and up-to-date context, often retrieved from a document base. RAG is a practical form of grounding.

## Practical example

### Internal Policy Assistant

A company wants its assistant to answer about vacations, reimbursement and travel. Without grounding, the model can mix generic public policies with internal rules. With internal documents as context, the application responds based on real corporate material.

```
Employee question -> app -> retrieval of relevant documents -> prompt with context -> Bedrock -> response
```

## Architectural reasoning

### A prompt alone relies on knowledge already in the model

If the knowledge is generic and stable, a good prompt may suffice. But if the case requires internal data, updated policies, or private documents, the prompt needs to be complemented by grounding. This distinction is common on the exam.

### Not every GenAI problem requires fine-tuning

Fine-tuning changes the model's behavior with additional data, but it is not always the best first choice. For AIF-C01, when the need is to reduce hallucination and respond using business documents, RAG is often a more direct starting point with lower update overhead and clearer source governance. Validate cost and answer quality for the workload.

## Best practices

- Specify role, objective, context and output format in the prompt.
- Use grounding when the answer depends on internal or recent information.
- Prefer more conservative parameters in operational and structured tasks.
- Monitor latency, cost per token and perceived quality.
- Add human review when the response influences critical decisions.

## Exam tips

- Prompt engineering improves instruction; RAG improves context.
- Low temperature favors consistency; high favors creativity.
- Hallucination is not eliminated just by using a better model.
- Knowledge base does not replace security, curation and access control.

## Common pitfalls

- Assuming that GenAI always returns the same answer for the same input.
- Confusing grounding with model training.
- Sending too much context and worsening cost, latency and quality.
- Use a generative model for a task that requires simple classification.

## Summary for review

- Tokens and context window impact cost and latency.
- A good prompt guides; grounding supports; guardrails protect.
- RAG is an important standard for reducing hallucinations with internal data.
- Generation parameters change creativity and predictability.
- GenAI needs governance, not just a strong model.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 01 — Introduction to AI and ML](../01-Introduction-to-AI-and-ML/README.md).
- Continue to [Module 03 — Fundamentals of Machine Learning](../03-Machine-Learning-Fundamentals/README.md).


---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
