# Questões — Módulo 14: Integração com Aplicações

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa processa milhares de documentos por hora com IA e não precisa devolver resposta imediata ao usuário. Qual componente ajuda a desacoplar e suavizar a carga?

- A) Amazon SQS
- B) Amazon Route 53
- C) Amazon EBS
- D) AWS Artifact

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

SQS é a resposta clássica para amortecer picos e desacoplar produtor e consumidor em processamento assíncrono.

**Por que as demais estão incorretas:**
- **B** — Route 53 é DNS.
- **C** — EBS é armazenamento em bloco.
- **D** — Artifact fornece documentos de conformidade.

</details>

---

**2.** Qual padrão tende a ser melhor para um chatbot corporativo com resposta imediata?

- A) Integração síncrona via API
- B) Processamento batch noturno
- C) Entrega física por Snowball
- D) Somente logs em S3 sem backend

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Se a experiência é conversacional e imediata, a integração síncrona via API costuma ser mais adequada.

**Por que as demais estão incorretas:**
- **B** — Batch não atende conversa em tempo real.
- **C** — Snowball é transferência física de dados.
- **D** — Sem backend controlado, a solução perde governança.

</details>

---

**3.** Qual é um benefício de intermediar chamadas ao modelo por um backend próprio?

- A) Centralizar autenticação, observabilidade e controle do prompt
- B) Eliminar completamente o custo de inferência
- C) Dispensar IAM
- D) Evitar toda necessidade de logs

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

A mediação pelo backend permite aplicar políticas técnicas e de negócio antes de chamar o modelo.

**Por que as demais estão incorretas:**
- **B** — Inferência continua tendo custo.
- **C** — IAM continua necessário.
- **D** — Logs continuam essenciais.

</details>

---

