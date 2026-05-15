# Cheatsheet — Módulo 05: Amazon Bedrock

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Bedrock | Camada gerenciada para FMs. | Não confundir com treino customizado completo. |
| Knowledge Bases | Grounding/RAG gerenciado. | Não substitui governança de documentos. |
| Guardrails | Política de entrada e saída. | Não é IAM. |
| Agents | Orquestram tarefas e ferramentas. | Não dispensam validação do fluxo. |

## Regras práticas

- Use Bedrock quando a prioridade for consumir FMs rapidamente com governança gerenciada.
- Aplique Guardrails para reduzir respostas fora de política e exposição indevida.
- Conecte Knowledge Bases a fontes documentais controladas e atualizadas.
- Monitore custo por token, latência e taxas de erro.

## Gatilhos de memorização

- Bedrock acelera uso de FM; Guardrails disciplinam; KB fundamenta; Agents executam.
- Governança de conteúdo não elimina governança de acesso.
