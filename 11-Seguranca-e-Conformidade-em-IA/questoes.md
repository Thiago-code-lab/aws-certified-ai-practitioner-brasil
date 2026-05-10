# Questões — Módulo 11: Segurança e Conformidade em IA

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa precisa auditar quem acessou documentos usados por uma aplicação de IA. Qual serviço AWS é mais alinhado a esse objetivo de rastreabilidade?

- A) AWS CloudTrail
- B) Amazon Polly
- C) Amazon Route 53
- D) AWS Batch

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

CloudTrail é a referência principal para auditoria de ações em serviços AWS.

**Por que as demais estão incorretas:**
- **B** — Polly é TTS e não ferramenta de auditoria.
- **C** — Route 53 trata DNS.
- **D** — Batch executa jobs, não registra auditoria de uso por si só.

</details>

---

**2.** Qual opção é a melhor prática para armazenar credenciais usadas por uma aplicação de IA que chama APIs internas?

- A) Colocar em arquivo texto no repositório
- B) Usar AWS Secrets Manager
- C) Publicar em variável global da aplicação sem proteção
- D) Enviar no prompt do modelo

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Secrets Manager é a opção gerenciada e apropriada para proteger segredos de aplicação.

**Por que as demais estão incorretas:**
- **A** — Expor no repositório é prática insegura.
- **C** — Variável sem proteção adequada continua arriscada.
- **D** — Segredo nunca deve ir no prompt do modelo.

</details>

---

**3.** Qual afirmação sobre segurança em IA na AWS está correta?

- A) Usar um serviço gerenciado elimina toda a responsabilidade do cliente
- B) O cliente ainda responde por dados, identidade, integrações e políticas da aplicação
- C) Criptografia torna IAM dispensável
- D) Logs são irrelevantes quando há Guardrails

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Shared responsibility continua valendo: a AWS protege a infraestrutura do serviço, mas o cliente segue responsável por grande parte do uso da solução.

**Por que as demais estão incorretas:**
- **A** — Serviço gerenciado não remove responsabilidade do cliente.
- **C** — Criptografia e IAM se complementam.
- **D** — Logs continuam essenciais.

</details>

---

