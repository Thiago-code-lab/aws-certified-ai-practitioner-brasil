# Questões — Módulo 06: Amazon SageMaker AI

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer treinar um modelo próprio com seus dados históricos e controlar o ciclo de vida de ML. Qual serviço AWS é mais alinhado?

- A) Amazon SageMaker AI
- B) Amazon Route 53
- C) AWS WAF
- D) Amazon CloudFront

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

SageMaker AI é a plataforma indicada quando a empresa precisa construir e operar ML customizado.

**Por que as demais estão incorretas:**
- **B** — Route 53 cuida de DNS.
- **C** — WAF protege aplicações web.
- **D** — CloudFront é CDN.

</details>

---

**2.** Qual opção tende a ser melhor para inferência esporádica com preocupação forte em custo ocioso?

- A) Inferência serverless
- B) Endpoint sempre ativo sem necessidade
- C) Treinamento distribuído contínuo
- D) Criar mais buckets S3

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Quando o tráfego é intermitente, serverless pode evitar custo de capacidade ociosa contínua.

**Por que as demais estão incorretas:**
- **B** — Mantém custo fixo sem necessariamente gerar valor.
- **C** — Treinamento distribuído é outra fase do ciclo.
- **D** — S3 adicional não resolve o padrão de inferência.

</details>

---

**3.** Qual recurso do SageMaker AI é mais associado a usuários de negócio que querem prever resultados sem escrever notebooks extensos?

- A) Canvas
- B) IAM Identity Center
- C) AWS Transit Gateway
- D) Amazon EBS

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Canvas é a experiência mais acessível para perfis menos técnicos dentro do ecossistema SageMaker.

**Por que as demais estão incorretas:**
- **B** — Identity Center trata acesso, não experiência de ML.
- **C** — Transit Gateway cuida de rede.
- **D** — EBS é armazenamento em bloco.

</details>

---
