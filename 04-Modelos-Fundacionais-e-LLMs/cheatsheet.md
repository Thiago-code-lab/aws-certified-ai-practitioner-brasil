# Cheatsheet — Módulo 04: Modelos Fundacionais e LLMs

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| LLM | Modelo fundacional focado em linguagem. | Nem todo FM é um LLM. |
| Embedding | Representação vetorial do significado. | Não gera resposta final ao usuário. |
| Vector database | Armazena vetores e permite busca por similaridade. | Não substitui toda a camada de dados do sistema. |
| RAG | Recupera contexto e depois gera. | Não é treinamento do modelo. |

## Regras práticas

- Use chunking coerente com a estrutura do documento.
- Armazene metadados úteis para filtrar contexto antes da recuperação.
- Reavalie a base vetorial quando os documentos forem atualizados.
- Separe claramente a função de recuperar da função de gerar.

## Gatilhos de memorização

- Representar primeiro, recuperar depois, gerar por último.
- Conhecimento dinâmico combina mais com RAG do que com fine-tuning.
- Base vetorial é apoio de retrieval, não a origem oficial do dado.
