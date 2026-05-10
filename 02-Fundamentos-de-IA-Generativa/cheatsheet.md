# Cheatsheet — Módulo 02: Fundamentos de IA Generativa

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Engenharia de prompts | Melhora instruções e formatação da resposta. | Não confundir com ajuste do modelo. |
| RAG | Recupera contexto externo antes da geração. | Não é sinônimo de fine-tuning. |
| Temperatura | Controla variabilidade da saída. | Temperatura alta não significa resposta mais correta. |
| Alucinação | Conteúdo plausível, mas incorreto ou inventado. | Modelo bom ainda pode alucinar. |

## Regras práticas

- Especifique papel, objetivo, contexto e formato de saída no prompt.
- Use grounding quando a resposta depender de informações internas ou recentes.
- Prefira parâmetros mais conservadores em tarefas operacionais e estruturadas.
- Monitore latência, custo por token e qualidade percebida.

## Gatilhos de memorização

- Prompt = instrução; RAG = contexto; Guardrails = política.
- Criatividade alta custa previsibilidade.
- Documentos internos pedem grounding.

