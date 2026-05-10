# Questões — Módulo 03: Fundamentos de Machine Learning

> **Nível predominante:** Iniciante a intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa deseja agrupar clientes com padrões semelhantes de compra, sem rótulos prévios. Qual tipo de aprendizado está mais alinhado?

- A) Supervisionado
- B) Não supervisionado
- C) Geração de imagem
- D) Criptografia assimétrica

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Agrupar sem rótulos prévios é exatamente um cenário de aprendizado não supervisionado, normalmente com clustering.

**Por que as demais estão incorretas:**
- **A** — Supervisionado exige rótulos ou alvo conhecido.
- **C** — Geração de imagem é outra categoria de workload.
- **D** — Criptografia não responde ao problema de ML.

</details>

---

**2.** Qual serviço da AWS ajuda quando o gargalo está em obter rótulos confiáveis para o dataset?

- A) Amazon SQS
- B) Amazon SageMaker Ground Truth
- C) AWS Direct Connect
- D) Amazon Route 53

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Ground Truth foi desenhado para rotulagem e preparação supervisionada de datasets.

**Por que as demais estão incorretas:**
- **A** — SQS é mensageria, não rotulagem.
- **C** — Direct Connect é conectividade dedicada.
- **D** — Route 53 é DNS.

</details>

---

**3.** Qual cenário sinaliza overfitting?

- A) Desempenho excelente em treino e ruim em dados novos
- B) Baixo desempenho em treino e teste por simplicidade excessiva
- C) Resposta do modelo é auditada por CloudTrail
- D) Uso de S3 para armazenar o dataset

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Esse é o padrão clássico de overfitting: o modelo memoriza o treino, mas generaliza mal.

**Por que as demais estão incorretas:**
- **B** — Isso está mais próximo de underfitting.
- **C** — CloudTrail é auditoria, não sintoma de ajuste excessivo.
- **D** — S3 é armazenamento e não caracteriza comportamento do modelo.

</details>

---
