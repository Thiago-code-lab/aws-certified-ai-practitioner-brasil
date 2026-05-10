# Questões — Módulo 10: IA Generativa na AWS

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma equipe está desenhando um assistente corporativo e quer reduzir ao máximo a operação de infraestrutura. Qual combinação de serviços AWS é mais coerente com esse objetivo?

- A) API Gateway + Lambda + Bedrock + S3
- B) Servidores bare metal + FTP + scripts manuais
- C) EC2 fixo sem logs nem API
- D) Somente Route 53 e CloudFront

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Essa combinação usa serviços gerenciados e encaixa bem em aplicações GenAI na AWS.

**Por que as demais estão incorretas:**
- **B** — Contraria a ideia de reduzir operação.
- **C** — EC2 fixo sem observabilidade piora a operação.
- **D** — Não há camada de negócio nem modelo generativo nessa combinação.

</details>

---

**2.** Qual cenário sugere uma integração assíncrona com o modelo?

- A) Chat em tempo real para perguntas curtas
- B) Geração de análise sobre um lote grande de documentos
- C) Autenticação de usuário por senha
- D) Configuração de DNS do portal

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Processar grande volume documental tende a ser mais compatível com assíncrono ou batch.

**Por que as demais estão incorretas:**
- **A** — Chat em tempo real normalmente pede resposta síncrona.
- **C** — Autenticação não é o caso de uso principal do modelo.
- **D** — DNS não define modo de inferência.

</details>

---

**3.** Qual é um benefício direto de colocar a chamada ao modelo atrás de uma camada de backend controlada?

- A) Maior governança, controle do prompt e observabilidade
- B) Eliminação completa de risco de alucinação
- C) Fim de toda necessidade de IAM
- D) Garantia de custo zero por inferência

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

A camada backend ajuda a centralizar segurança, observabilidade, versionamento e integração com dados e políticas.

**Por que as demais estão incorretas:**
- **B** — Alucinação pode ser mitigada, mas não eliminada automaticamente.
- **C** — IAM continua essencial.
- **D** — Inferência continua tendo custo.

</details>

---
