# Cheatsheet — Módulo 09: Engenharia de Prompts

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Role prompt | Define o papel esperado do modelo. | Não basta sozinho sem contexto. |
| Few-shot | Usa exemplos para orientar padrão. | Não é treinamento do modelo. |
| Saída estruturada | Importante para integração com sistemas. | Texto livre dificulta automação. |
| Versionamento | Ajuda comparar e controlar mudanças. | Mudança de prompt pode alterar produção. |

## Regras práticas

- Descreva papel, objetivo, contexto, formato e limites da resposta.
- Use few-shot quando a tarefa exigir consistência de estilo ou estrutura.
- Peça formatos verificáveis, como JSON ou listas numeradas, quando a integração depender disso.
- Evite contexto excessivo e irrelevante.

## Gatilhos de memorização

- Prompt bom reduz ambiguidade.
- Exemplo ensina padrão sem re-treino.
- Formato explícito protege integrações.
