# Questões — Módulo 01: Introdução a IA e ML

> **Nível predominante:** Iniciante a intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer prever quais clientes têm maior chance de cancelamento com base em histórico de uso e tickets já classificados. Qual conceito está mais alinhado ao problema?

- A) Clustering não supervisionado
- B) ML supervisionado
- C) IA generativa multimodal
- D) Rede social corporativa com RAG

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

O enunciado fala em dados históricos com resultado conhecido e objetivo de prever cancelamento. Isso caracteriza ML supervisionado.

**Por que as demais estão incorretas:**
- **A** — Clustering agrupa padrões sem rótulo; aqui o problema já tem alvo claro.
- **C** — IA generativa não é a abordagem natural para prever churn.
- **D** — RAG ajuda em recuperação contextual, não em previsão supervisionada.

</details>

---

**2.** Uma startup quer adicionar geração de texto em seu aplicativo sem treinar um modelo do zero nem operar infraestrutura de GPU. Qual serviço AWS aparece como escolha mais direta?

- A) Amazon Bedrock
- B) Amazon EC2 Auto Scaling
- C) AWS Batch
- D) Amazon RDS

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Bedrock foi desenhado exatamente para consumo gerenciado de foundation models por API, reduzindo o esforço operacional.

**Por que as demais estão incorretas:**
- **B** — EC2 Auto Scaling escala compute, mas não resolve por si só o consumo gerenciado de FMs.
- **C** — AWS Batch orquestra jobs em lote, não é a resposta principal para GenAI por API.
- **D** — RDS é banco de dados relacional, não uma camada de modelos fundacionais.

</details>

---

**3.** Qual afirmação sobre inferência está correta no contexto do exame?

- A) Inferência é a fase em que o modelo aprende com o dataset
- B) Inferência costuma estar mais próxima da experiência do usuário final
- C) Inferência só existe em cargas batch
- D) Inferência elimina a necessidade de segurança e auditoria

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Inferência é a etapa de uso do modelo em produção e, por isso, costuma impactar diretamente latência, custo por chamada e experiência do usuário.

**Por que as demais estão incorretas:**
- **A** — Aprender com dataset é treinamento, não inferência.
- **C** — Inferência pode ser síncrona, assíncrona, em streaming ou em batch.
- **D** — Segurança e auditoria continuam essenciais na inferência.

</details>

---

