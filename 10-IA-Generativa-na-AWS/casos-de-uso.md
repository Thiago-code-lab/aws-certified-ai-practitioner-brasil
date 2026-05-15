# Casos de Uso — Módulo 10: IA Generativa na AWS

## Caso 1 — Portal interno de conhecimento

**Cenário:** Usuários autenticados fazem perguntas sobre políticas e processos da empresa.

**Arquitetura sugerida:** Portal web com API Gateway, Lambda, Bedrock, S3 e CloudWatch.

**Por que essa escolha faz sentido:** Arquitetura serverless reduz operação e mantém controle centralizado.

**Armadilha de prova associada:** Expor o modelo diretamente ao navegador.

## Caso 2 — Processamento de contratos

**Cenário:** Uma área jurídica precisa resumir centenas de contratos toda noite.

**Arquitetura sugerida:** Pipeline assíncrono com armazenamento em S3, orquestração e inferência fora do caminho interativo.

**Por que essa escolha faz sentido:** O usuário não espera resposta instantânea; custo e robustez importam mais que chat em tempo real.

**Armadilha de prova associada:** Desenhar tudo como requisição síncrona.
