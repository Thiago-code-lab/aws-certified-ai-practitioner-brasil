# Casos de Uso — Módulo 04: Modelos Fundacionais e LLMs

## Caso 1 — Busca em políticas internas

**Cenário:** Funcionários precisam receber respostas com base em políticas atuais da empresa.

**Arquitetura sugerida:** RAG com documentos em S3, embeddings, índice vetorial e LLM para compor a resposta final.

**Por que essa escolha faz sentido:** O conhecimento é documental, dinâmico e precisa de rastreabilidade.

**Armadilha de prova associada:** Escolher somente prompt estático sem mecanismo de recuperação.

## Caso 2 — Catálogo de produtos semelhantes

**Cenário:** Um marketplace quer sugerir produtos semanticamente parecidos mesmo quando a descrição textual muda.

**Arquitetura sugerida:** Embeddings para representar descrições e mecanismo vetorial para recuperar itens similares.

**Por que essa escolha faz sentido:** A similaridade por significado é mais importante que palavras exatas.

**Armadilha de prova associada:** Depender só de busca lexical.

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
