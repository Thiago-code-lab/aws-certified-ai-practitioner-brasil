# Module 04 — Foundation Models and LLMs

This module connects theory and architecture: what foundation models are, how LLMs fit into this field and why embeddings, vectors and RAG appear together in so many solutions on AWS.

## Objective

Understand the role of foundation models in real applications, differentiate text generation from vector representation and build the correct reasoning for RAG, embeddings and vector databases.

## How this topic appears on AIF-C01

- Define foundation model, LLM, embedding and vector database.
- Differentiate between RAG and fine-tuning.
- Understand why retrieval improves context and governance.

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
| Amazon Bedrock | Provides FMs and resources such as Knowledge Bases. | Core layer for managed GenAI. |
| Amazon OpenSearch Serverless | It can act as vector storage in retrieval architectures. | Appears as a semantic search and RAG component. |
| Amazon Aurora PostgreSQL with pgvector | Alternative when the case already uses a relational database and needs vectors. | Useful in architectural comparisons. |
| Amazon S3 | Common origin of documents indexed in RAG. | Frequent component for document collections. |

## Essential concepts

### Foundation models and LLMs

Foundation models are broad models trained to serve as the basis for multiple tasks. LLMs are foundation models specialized in natural language. On the exam, the central point is to understand that an FM can be text, image or multimodal; an LLM is an important type within this field.

### Embeddings and semantic similarity

Embeddings transform text, images, or other content into numeric vectors that preserve semantic meaning. This allows you to compare proximity between documents or questions, basing retrieval on meaning and not just identical words.

### Vector databases and RAG

A vector database stores embeddings and allows similarity searching. In RAG, the user's question also becomes embedding, the semantically closest items are retrieved and then sent as context to the generating model. This pattern helps reduce hallucinations and keep responses aligned with company data.

## Practical example

### RAG Compliance Assistant

The compliance area needs to answer questions based on updated policies, contracts and standards. Instead of training a new model every time documents change, the company can index the texts and retrieve the relevant snippets at the time of the question.

```
Documents in S3 -> chunking and embeddings -> vector index -> user question -> retrieval -> LLM -> response
```

## Architectural reasoning

### When RAG usually beats fine-tuning

When the priority is to use updated internal knowledge, control the origin of the response and reduce adaptation costs. Fine-tuning can be useful for style or behavior, but RAG tends to be the more pragmatic response to changing document-based knowledge.

### Embeddings do not generate text

Embeddings represent content. The generator model generates the final answer. This distinction is important because several exam questions attempt to confuse the role of the vector database with the role of the LLM.

## Best practices

- Use chunking consistent with the structure of the document.
- Store useful metadata to filter context before retrieval.
- Reevaluate the vector database when documents are updated.
- Clearly separate the retrieve function from the generate function.
- Validate whether the application needs RAG or whether a simple prompt is enough.

## Exam tips

- Embedding represents; LLM generates.
- RAG retrieves external context before responding.
- Vector database does not replace the source repository or the access policy.
- If knowledge changes frequently, RAG is usually better than re-training.

## Common pitfalls

- Thinking that embeddings and text generation are the same thing.
- Confusing vector database with data lake or general transactional database.
- Use fine-tuning when the problem is updating knowledge.
- Ignore metadata and send irrelevant context to the model.

## Summary for review

- Foundation models can serve multiple tasks; LLM is a language-focused FM.
- Embeddings support semantic search.
- RAG combines retrieval and generation to substantiate responses.
- Vector database accelerates similarity retrieval.
- The choice between RAG and fine-tuning depends on the type of adaptation required.

## Next steps

- Solve the [module questions](./questions.md) before continuing.
- Review [flashcards](./flashcards.md) as spaced review.
- Consult [lab](./lab.md) to consolidate the practical part.
- Complementary review: [Module 03 — Fundamentals of Machine Learning](../03-Machine-Learning-Fundamentals/README.md).
- Continue to [Module 05 — Amazon Bedrock](../05-Amazon-Bedrock/README.md).

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> To deepen the database behind AI solutions on AWS, it is also worth studying the course [Data Engineering on AWS: from Zero to Real Projects](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
