# Cheatsheet — Módulo 15: Boas Práticas e Otimização

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Modelo menor | Prefira quando já atende ao objetivo. | Não assumir que maior sempre é melhor. |
| Cache | Bom para respostas repetidas. | Não usar sem pensar em validade do conteúdo. |
| Batch | Ótimo quando a resposta não precisa ser imediata. | Não forçar tempo real sem necessidade. |
| Budgets/Cost Explorer | Apoiam visibilidade e controle de gasto. | Custo sem monitoramento foge rápido. |

## Regras práticas

- Escolha o menor modelo que atenda ao requisito.
- Limite contexto e tamanho da resposta ao necessário.
- Use cache para perguntas repetidas e respostas estáveis.
- Monitore custo, latência, falhas e taxa de reutilização.

## Gatilhos de memorização

- Prompt menor + modelo adequado + contexto certo = economia.
- Medir sempre; otimizar depois com dado real.

