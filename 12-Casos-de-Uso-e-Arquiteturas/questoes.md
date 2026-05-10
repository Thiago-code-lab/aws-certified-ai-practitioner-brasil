# Questões — Módulo 12: Casos de Uso e Arquiteturas

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer extrair campos de formulários digitalizados e tabelas de PDFs. Qual serviço AWS é mais direto para esse requisito?

- A) Amazon Textract
- B) Amazon Bedrock sozinho
- C) Amazon Route 53
- D) AWS Global Accelerator

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Textract é o serviço especializado da AWS para extração de texto, formulários e tabelas em documentos.

**Por que as demais estão incorretas:**
- **B** — Um LLM pode até ajudar em etapas posteriores, mas não é a resposta mais direta para extração estrutural.
- **C** — Route 53 é DNS.
- **D** — Global Accelerator trata roteamento de rede.

</details>

---

**2.** Qual serviço AWS tende a ser mais adequado para análise de sentimento de reviews sem equipe de ML especializada?

- A) Amazon Comprehend
- B) Amazon EBS
- C) AWS Snowcone
- D) Amazon VPC

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Comprehend é a opção gerenciada natural para NLP como sentimento, entidade e classificação de texto.

**Por que as demais estão incorretas:**
- **B** — EBS é armazenamento em bloco.
- **C** — Snowcone é transferência/edge de dados.
- **D** — VPC é rede.

</details>

---

**3.** Uma empresa deseja resumir contratos depois de extrair seus campos. Qual combinação faz mais sentido?

- A) Textract para extrair e Bedrock para resumir
- B) Route 53 para extrair e SQS para resumir
- C) CloudFront para OCR e DynamoDB para geração
- D) KMS para resumo e IAM para OCR

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Textract cobre a extração estruturada e Bedrock cobre a geração de resumo em linguagem natural.

**Por que as demais estão incorretas:**
- **B** — Esses serviços não cumprem essas funções.
- **C** — CloudFront e DynamoDB não são os serviços corretos para OCR e resumo generativo.
- **D** — KMS e IAM tratam segurança e acesso.

</details>

---
