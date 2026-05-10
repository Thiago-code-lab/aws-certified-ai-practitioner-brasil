# Questões — Módulo 08: Dados para IA

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer usar documentos internos em RAG, mas muitos arquivos estão duplicados, antigos e sem classificação. Qual ação traz maior benefício inicial?

- A) Fazer curadoria e preparar a base documental
- B) Aumentar a temperatura do modelo
- C) Criar um bucket adicional sem organizar os arquivos
- D) Remover os logs da aplicação

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Sem base confiável, o RAG recupera contexto fraco. Curadoria e preparo documental atacam a causa do problema.

**Por que as demais estão incorretas:**
- **B** — Temperatura não corrige baixa qualidade do contexto.
- **C** — Mais buckets sem organização não resolvem a raiz.
- **D** — Logs são importantes para governança e análise.

</details>

---

**2.** Qual serviço AWS ajuda especificamente a identificar dados sensíveis em objetos S3?

- A) Amazon Macie
- B) Amazon DynamoDB
- C) Amazon SQS
- D) AWS Fargate

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Macie é o serviço mais associado à descoberta de PII e dados sensíveis em S3.

**Por que as demais estão incorretas:**
- **B** — DynamoDB é banco NoSQL, não scanner de sensibilidade em S3.
- **C** — SQS é fila.
- **D** — Fargate executa containers.

</details>

---

**3.** Em uma arquitetura RAG, qual elemento aumenta a precisão da recuperação além do próprio texto do chunk?

- A) Metadados relevantes
- B) Desligar IAM
- C) Trocar HTTPS por HTTP
- D) Remover versionamento

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Metadados permitem filtrar e contextualizar a recuperação, melhorando a qualidade do contexto enviado ao modelo.

**Por que as demais estão incorretas:**
- **B** — Desligar IAM piora a segurança.
- **C** — HTTP piora a proteção em trânsito.
- **D** — Sem versionamento, a rastreabilidade do dado piora.

</details>

---
