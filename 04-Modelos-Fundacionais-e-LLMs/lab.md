# Lab — Módulo 04: Modelos Fundacionais e LLMs

## Desenhando um fluxo RAG na AWS

Consolidar visualmente o encadeamento entre dados, embeddings, retrieval e geração.

## Pré-requisitos

- Ter lido os módulos 01 a 04.
- Conhecer conceitos básicos de S3 e Bedrock.

## Passo a passo

1. Liste um conjunto pequeno de documentos que fariam sentido como base de conhecimento.
2. Defina como esses documentos seriam armazenados e versionados no S3.
3. Descreva como o texto seria dividido em chunks e convertido em embeddings.
4. Escolha onde os vetores seriam armazenados e como o retrieval ocorreria.
5. Explique como o LLM receberia a pergunta e o contexto recuperado.

## O que observar

- RAG tem duas etapas distintas: recuperação e geração.
- Sem curadoria de documentos, o LLM continua vulnerável a contexto ruim.

## Custos e limpeza

- Lab pode ser apenas de arquitetura, sem custo.
- Se você testar serviços, remova índices e bases temporárias após o uso.
