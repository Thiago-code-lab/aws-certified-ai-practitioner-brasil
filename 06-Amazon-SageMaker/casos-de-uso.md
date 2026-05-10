# Casos de Uso — Módulo 06: Amazon SageMaker AI

## Caso 1 — Previsao de demanda

**Cenário:** A empresa quer usar seus próprios dados históricos para gerar previsões específicas do negócio.

**Arquitetura sugerida:** Pipeline de ML com SageMaker AI e datasets versionados em S3.

**Por que essa escolha faz sentido:** Há necessidade de modelo customizado e controle do ciclo de vida.

**Armadilha de prova associada:** Escolher Bedrock apenas por ser serviço de IA.

## Caso 2 — Analistas de negócio sem time de DS maduro

**Cenário:** Uma área comercial quer testar rapidamente modelos de previsão sem começar por notebooks.

**Arquitetura sugerida:** Canvas como porta de entrada, com governança e dados organizados.

**Por que essa escolha faz sentido:** O foco aqui é velocidade com menor barreira técnica.

**Armadilha de prova associada:** Achar que no-code dispensa preparo de dados.
