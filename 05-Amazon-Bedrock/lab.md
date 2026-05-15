# Lab — Módulo 05: Amazon Bedrock

## Mapa de capacidade do Bedrock

Organizar mentalmente os blocos do serviço e quando cada um entra na arquitetura.

## Pré-requisitos

- Ler os módulos 02, 04 e 05.
- Opcional: acesso à console do Bedrock.

## Passo a passo

1. Liste um caso de uso de pergunta e resposta com documentos internos.
2. Mapeie onde entrariam modelo, Knowledge Base, Guardrails e logs.
3. Identifique quais permissões IAM seriam necessárias.
4. Defina quais respostas precisariam de revisão humana.
5. Anote onde o custo cresce: contexto, tokens e frequência de chamadas.

## O que observar

- Bedrock resolve a camada de FM, mas a aplicação ainda precisa arquitetura completa ao redor.
- Knowledge Bases e Guardrails respondem a problemas diferentes.

## Custos e limpeza

- Se criar recursos na conta, remova-os após o teste.
- Não use dados sensíveis sem política e aprovação adequadas.
