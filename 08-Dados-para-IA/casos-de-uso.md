# Casos de Uso — Módulo 08: Dados para IA

## Caso 1 — Base regulatória

**Cenário:** Uma empresa precisa responder perguntas com base em normas que mudam com frequência.

**Arquitetura sugerida:** Curadoria contínua, versionamento, metadados e fluxo de atualização da base de documentos em S3.

**Por que essa escolha faz sentido:** Conhecimento regulatório envelhece rápido e precisa de processo, não só de armazenamento.

**Armadilha de prova associada:** Confiar em PDFs jogados sem catálogo.

## Caso 2 — Documentos sensiveis

**Cenário:** Uma área quer conectar relatórios com PII a um assistente generativo.

**Arquitetura sugerida:** Classificar dados, reduzir exposição, aplicar controle de acesso e avaliar se todo o conteúdo realmente deve entrar na base.

**Por que essa escolha faz sentido:** Nem todo dado que existe deve ser usado pelo modelo.

**Armadilha de prova associada:** Abrir a base inteira para a IA por conveniência.
