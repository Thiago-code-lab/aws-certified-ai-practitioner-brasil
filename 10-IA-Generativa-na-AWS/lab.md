# Lab — Módulo 10: IA Generativa na AWS

## Arquitetando uma aplicação GenAI serverless

Montar uma arquitetura AWS mínima viável para um assistente corporativo.

## Pré-requisitos

- Conhecer Bedrock, S3, API Gateway e Lambda em nível conceitual.

## Passo a passo

1. Desenhe o fluxo usuário -> API -> backend -> modelo -> resposta.
2. Decida onde ficam documentos, logs e política de acesso.
3. Marque quais chamadas são síncronas e quais seriam assíncronas.
4. Inclua um fallback para erro ou baixa confiança.
5. Explique como monitorar custo e latência.

## O que observar

- Uma boa arquitetura GenAI precisa de camadas além do modelo.
- Segurança e observabilidade aparecem desde o primeiro diagrama.

## Custos e limpeza

- Sem custo obrigatório se feito apenas no diagrama.
- Caso faça POC real, remova recursos não utilizados.
