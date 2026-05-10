# Simulado Completo 1 — AIF-C01

Simulado focado em progressão de dificuldade, cobrindo fundamentos, GenAI, responsible AI e segurança.

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

**6.** Uma aplicação generativa lida com decisões sensíveis de RH. Qual prática é mais alinhada com IA responsável?

- A) Revisão humana antes da decisão final
- B) Automação total sem supervisão
- C) Sem logs nem política
- D) Temperatura máxima em produção

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Decisões sensíveis pedem supervisão humana e governança reforçada.

**Por que as demais estão incorretas:**
- **B** — É arriscado e desalinhado com responsible AI.
- **C** — Governança exige registros e política.
- **D** — Temperatura não resolve o tema de risco.

</details>

---

**7.** Qual serviço ajuda a identificar PII em dados armazenados no S3?

- A) Amazon Macie
- B) Amazon Polly
- C) Amazon MQ
- D) AWS Batch

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Macie é o serviço associado à descoberta de dados sensíveis em S3.

**Por que as demais estão incorretas:**
- **B** — Polly é texto para fala.
- **C** — MQ é mensageria.
- **D** — Batch executa jobs.

</details>

---

**8.** Qual escolha tende a ser melhor quando a empresa quer reduzir custo ocioso em inferência esporádica?

- A) Inferência serverless ou fluxo sob demanda
- B) Capacidade permanente máxima o tempo todo
- C) Aumentar o contexto sem necessidade
- D) Desligar CloudWatch

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Carga esporádica favorece abordagens mais elásticas, reduzindo custo ocioso.

**Por que as demais estão incorretas:**
- **B** — Mantém custo desnecessário.
- **C** — Mais contexto pode aumentar custo.
- **D** — Observabilidade continua necessária.

</details>

---

**9.** Qual serviço é o mais indicado para recomendação personalizada de produtos?

- A) Amazon Personalize
- B) Amazon Rekognition
- C) Amazon Textract
- D) AWS KMS

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Personalize é o serviço específico para recomendação personalizada na AWS.

**Por que as demais estão incorretas:**
- **B** — Rekognition é visão computacional.
- **C** — Textract é documentos.
- **D** — KMS é criptografia.

</details>

---

**10.** Se a pergunta fala em simplicidade operacional para usar FMs por API, qual serviço AWS costuma ser a melhor resposta?

- A) Amazon Bedrock
- B) Amazon RDS
- C) AWS Snowball
- D) Elastic Load Balancing

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Bedrock entrega consumo gerenciado de FMs por API com baixa carga operacional.

**Por que as demais estão incorretas:**
- **B** — RDS é banco relacional.
- **C** — Snowball é transferência de dados.
- **D** — ELB é balanceamento de carga.

</details>

---
