# Questões — Módulo 05: Amazon Bedrock

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer usar LLMs sem provisionar GPUs nem operar endpoints próprios. Qual serviço AWS atende mais diretamente esse requisito?

- A) Amazon Bedrock
- B) AWS Storage Gateway
- C) Amazon Route 53
- D) Amazon EFS

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Bedrock foi criado para consumir FMs por API com menor esforço operacional.

**Por que as demais estão incorretas:**
- **B** — Storage Gateway integra armazenamento híbrido, não modelos fundacionais.
- **C** — Route 53 é DNS.
- **D** — EFS é sistema de arquivos.

</details>

---

**2.** Qual recurso do Bedrock ajuda mais quando a aplicação precisa responder com base em documentos internos aprovados?

- A) Knowledge Bases
- B) Elastic IP
- C) AWS Transit Gateway
- D) Amazon SQS FIFO

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Knowledge Bases são o recurso gerenciado para grounding e recuperação contextual em Bedrock.

**Por que as demais estão incorretas:**
- **B** — Elastic IP não participa do grounding documental.
- **C** — Transit Gateway trata conectividade de rede.
- **D** — SQS FIFO trata mensageria com ordenação.

</details>

---

**3.** Qual afirmação sobre Guardrails está correta?

- A) Guardrails substituem criptografia e IAM
- B) Guardrails ajudam a impor políticas de conteúdo e segurança da saída
- C) Guardrails são usados para treinar um modelo do zero
- D) Guardrails existem apenas em cargas batch

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Guardrails atuam como proteção de conteúdo e política de interação, ajudando a reduzir respostas inadequadas ou sensíveis.

**Por que as demais estão incorretas:**
- **A** — IAM e criptografia continuam obrigatórios.
- **C** — Treino do zero não é papel de Guardrails.
- **D** — Podem ser usados em interações de aplicações, não apenas em batch.

</details>

---
