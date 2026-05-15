# Casos de Uso — Módulo 01: Introdução a IA e ML

## Caso 1 — Central de atendimento

**Cenário:** Uma operação quer priorizar tickets urgentes e resumir o histórico do cliente para o atendente.

**Arquitetura sugerida:** Classificação supervisionada ou serviço de NLP para priorização, combinados com um FM para sumarização contextual.

**Por que essa escolha faz sentido:** O caso mistura duas naturezas de problema: classificação estruturada e geração de texto. A arquitetura correta pode usar componentes diferentes em vez de forçar tudo para um único modelo.

**Armadilha de prova associada:** Querer resolver toda a solução apenas com um chatbot genérico.

## Caso 2 — Catálogo de documentos internos

**Cenário:** Um time jurídico quer responder perguntas sobre políticas internas sem expor documentos sensíveis publicamente.

**Arquitetura sugerida:** Aplicação com Bedrock, base de documentos em S3 e mecanismo de grounding/RAG com controle de acesso por IAM.

**Por que essa escolha faz sentido:** O desafio principal é resposta contextualizada com governança de dados, não treinamento de modelo do zero.

**Armadilha de prova associada:** Assumir que subir PDFs em um bucket sozinho já resolve busca inteligente.

