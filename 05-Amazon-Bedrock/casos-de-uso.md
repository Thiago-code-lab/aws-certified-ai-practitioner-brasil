# Casos de Uso — Módulo 05: Amazon Bedrock

## Caso 1 — Assistente de suporte interno

**Cenário:** A empresa quer respostas com base em base documental e filtro de temas proibidos.

**Arquitetura sugerida:** Bedrock com Knowledge Bases e Guardrails.

**Por que essa escolha faz sentido:** Une grounding e política de conteúdo na mesma solução gerenciada.

**Armadilha de prova associada:** Escolher somente um modelo sem pensar no contexto e nos controles.

## Caso 2 — Automação com chamadas de sistema

**Cenário:** Um bot precisa consultar status de pedido e abrir chamado quando necessário.

**Arquitetura sugerida:** Aplicação com Bedrock Agents ou camada de orquestração equivalente, conectada a APIs internas.

**Por que essa escolha faz sentido:** O caso exige responder e também executar ações em sistemas externos.

**Armadilha de prova associada:** Assumir que geração textual sozinha resolve todo o fluxo.
