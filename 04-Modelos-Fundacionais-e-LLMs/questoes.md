# Questões — Módulo 04: Modelos Fundacionais e LLMs

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Qual componente de uma arquitetura RAG é mais diretamente responsável por busca semântica em documentos?

- A) Embedding + índice vetorial
- B) Tabela de rotas da VPC
- C) EC2 Auto Scaling
- D) CloudTrail sozinho

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

A busca semântica depende da representação vetorial dos documentos e da capacidade de consultar esse índice por similaridade.

**Por que as demais estão incorretas:**
- **B** — VPC trata rede, não retrieval semântico.
- **C** — Auto Scaling cuida de capacidade computacional, não de busca vetorial.
- **D** — CloudTrail audita eventos, mas não executa recuperação semântica.

</details>

---

**2.** Uma empresa atualiza documentos toda semana e quer respostas baseadas nesses arquivos. Qual estratégia tende a ser mais pragmática?

- A) Re-treinar o modelo sempre que um PDF mudar
- B) Usar RAG com documentos indexados
- C) Desligar controle de acesso para facilitar testes
- D) Trocar S3 por um servidor FTP

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

RAG permite usar documentos atualizados como contexto sem depender de re-treinamento frequente do modelo.

**Por que as demais estão incorretas:**
- **A** — É mais custoso e operacionalmente pesado para conhecimento documental em mudança constante.
- **C** — Isso piora segurança e governança.
- **D** — Mudar protocolo de armazenamento não resolve o problema arquitetural.

</details>

---

**3.** Qual afirmação sobre embeddings está correta?

- A) Embeddings são usados principalmente para gerar parágrafos longos
- B) Embeddings transformam conteúdo em vetores para comparação semântica
- C) Embeddings substituem IAM em aplicações de IA
- D) Embeddings eliminam a necessidade de modelo gerador

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Embeddings são representações vetoriais pensadas para captura de similaridade semântica.

**Por que as demais estão incorretas:**
- **A** — Geração textual é papel do modelo gerador, não do embedding.
- **C** — IAM continua sendo controle de acesso essencial.
- **D** — RAG normalmente usa embeddings e um modelo gerador em conjunto.

</details>

---
