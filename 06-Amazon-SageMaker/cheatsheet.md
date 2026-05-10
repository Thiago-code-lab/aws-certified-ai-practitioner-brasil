# Cheatsheet — Módulo 06: Amazon SageMaker AI

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Studio | Ambiente técnico para desenvolvimento e experimentação. | Não confundir com Canvas. |
| Canvas | ML low-code/no-code para analistas. | Ainda depende de dados adequados. |
| JumpStart | Acelera início com modelos e templates. | Não substitui avaliação do caso de uso. |
| Batch inference | Processamento em lote, fora do caminho crítico do usuário. | Não usar quando a pergunta pede resposta imediata. |

## Regras práticas

- Defina claramente se o problema exige modelo customizado ou serviço gerenciado pronto.
- Use S3 como base organizada para datasets e artefatos.
- Escolha o modo de inferência conforme latência, custo e padrão de tráfego.
- Mantenha rastreabilidade dos experimentos e versões do modelo.

## Gatilhos de memorização

- Bedrock consome FMs; SageMaker AI constrói e opera ML.
- Canvas democratiza; Studio aprofunda.
- Carga define o tipo de inferência.
