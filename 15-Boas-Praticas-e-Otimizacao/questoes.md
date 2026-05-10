# Questões — Módulo 15: Boas Práticas e Otimização

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa usa um modelo caro para responder perguntas simples e repetitivas. Qual prática pode reduzir custo sem degradar muito a experiência?

- A) Aplicar cache e revisar se um modelo menor atende
- B) Aumentar sempre o contexto enviado
- C) Desligar monitoramento de custo
- D) Migrar tudo para fluxo manual sem avaliação

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Cache e escolha de modelo mais adequado são alavancas diretas de otimização em casos repetitivos.

**Por que as demais estão incorretas:**
- **B** — Mais contexto tende a aumentar custo.
- **C** — Sem monitoramento, a otimização fica cega.
- **D** — Remover automação sem análise não é estratégia de otimização.

</details>

---

**2.** Qual afirmação sobre otimização de IA na AWS está correta?

- A) Só o preço do modelo importa
- B) Latência, volume de chamadas, tamanho do contexto e arquitetura também afetam custo
- C) CloudWatch não ajuda em nada
- D) Batch sempre é pior que síncrono

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

O custo total da solução depende do desenho inteiro, não apenas do nome do modelo.

**Por que as demais estão incorretas:**
- **A** — Visão incompleta do custo.
- **C** — CloudWatch é essencial para operação e medição.
- **D** — Batch pode ser melhor quando o caso não exige imediatismo.

</details>

---

**3.** Qual serviço AWS ajuda a criar alertas quando o gasto de uma solução começa a sair do esperado?

- A) AWS Budgets
- B) Amazon Route 53
- C) AWS WAF
- D) Amazon EFS

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

AWS Budgets é o serviço mais associado a alertas e controle de orçamento.

**Por que as demais estão incorretas:**
- **B** — Route 53 não trata orçamento.
- **C** — WAF trata proteção web.
- **D** — EFS é sistema de arquivos.

</details>

---

