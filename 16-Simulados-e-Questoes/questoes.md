# Questões de Aquecimento — AIF-C01

Use estas questões antes dos simulados completos para aquecer leitura de enunciado e vocabulário do exame.

**1.** Uma empresa quer responder perguntas sobre políticas internas usando documentos atualizados com frequência. Qual solução é mais coerente?

- A) RAG com base documental controlada
- B) Re-treinar o modelo a cada novo documento
- C) Remover logs para ganhar latência
- D) Trocar IAM por Guardrails

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Quando o conhecimento muda com frequência e precisa ser fundamentado, RAG é o caminho mais prático.

**Por que as demais estão incorretas:**
- **B** — Costuma ser mais caro e menos ágil para esse cenário.
- **C** — Logs não são a raiz do problema e continuam importantes.
- **D** — Guardrails e IAM atendem problemas diferentes.

</details>

---

**2.** Qual serviço AWS é mais alinhado à construção de um modelo customizado com dados próprios?

- A) Amazon SageMaker AI
- B) Amazon Route 53
- C) Amazon Bedrock Guardrails
- D) Amazon CloudFront

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

SageMaker AI é a plataforma de ML customizado da AWS.

**Por que as demais estão incorretas:**
- **B** — DNS não resolve treino de modelo.
- **C** — Guardrails não treinam modelo.
- **D** — CloudFront é CDN.

</details>

---

**3.** Qual recurso ajuda a aplicar políticas de conteúdo em aplicações generativas no Bedrock?

- A) Guardrails
- B) Transit Gateway
- C) EBS
- D) Route Table

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Guardrails ajudam a controlar entradas e saídas em aplicações generativas.

**Por que as demais estão incorretas:**
- **B** — É conectividade de rede.
- **C** — É armazenamento.
- **D** — É roteamento de rede.

</details>

---

**4.** Em uma arquitetura RAG, qual elemento existe para recuperar contexto semântico?

- A) Embeddings e base vetorial
- B) Subnet pública
- C) NAT Gateway
- D) ACM

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

A recuperação semântica depende de embeddings e de um armazenamento/índice vetorial.

**Por que as demais estão incorretas:**
- **B** — Rede não executa retrieval semântico.
- **C** — NAT trata saída para internet.
- **D** — ACM trata certificados.

</details>

---

**5.** Qual serviço AWS é mais indicado para extrair texto, formulários e tabelas de PDFs?

- A) Amazon Textract
- B) Amazon Personalize
- C) Amazon SQS
- D) AWS Budgets

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Textract é o serviço especializado em extração documental.

**Por que as demais estão incorretas:**
- **B** — Personalize é recomendação.
- **C** — SQS é fila.
- **D** — Budgets trata custo.

</details>

---
