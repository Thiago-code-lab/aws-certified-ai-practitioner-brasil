# Módulo 10 — IA Generativa na AWS

Neste módulo você liga os conceitos de GenAI à arquitetura de aplicação: front-end, autenticação, backend, observabilidade, bases documentais e serviços de integração na AWS.

## Objetivo

Montar o raciocínio de arquitetura para aplicações generativas na AWS, entendendo componentes típicos, integrações e decisões de custo, latência e segurança.

## Onde este tema aparece no AIF-C01

- Descrever arquiteturas GenAI orientadas a aplicações.
- Escolher componentes gerenciados na AWS para orquestração e entrega.
- Conectar modelo, dados, API, observabilidade e segurança.

## Navegação do módulo

- [README](./README.md)
- [Cheatsheet](./cheatsheet.md)
- [Flashcards](./flashcards.md)
- [Questões](./questoes.md)
- [Casos de uso](./casos-de-uso.md)
- [Lab prático](./lab.md)
- [Links oficiais](./links.md)

## Serviços AWS principais

| Serviço AWS | Papel no módulo | Como aparece na prova |
| --- | --- | --- |
| Amazon Bedrock | Camada de FM e recursos generativos. | Componente central da aplicação. |
| AWS Lambda | Backend serverless para orquestração e chamadas ao modelo. | Aparece quando o caso pede simplicidade operacional. |
| Amazon API Gateway | Exposição de APIs para front-ends e integrações. | Muito comum em arquiteturas web. |
| Amazon CloudWatch | Logs, métricas e alarmes da solução. | Importante para operação e troubleshooting. |

## Conceitos essenciais

### Fluxo típico de uma aplicação GenAI

Usuário envia a solicitação, a aplicação autentica, prepara o contexto, consulta base de conhecimento quando necessário, chama o modelo e registra logs e métricas. Em muitos casos, a melhor arquitetura é serverless e orientada a serviços gerenciados.

### Síncrono, assíncrono e em lote

Um chat em tempo real costuma pedir chamada síncrona ao modelo. Processamento de documentos grandes pode ser assíncrono ou em lote. O exame frequentemente diferencia esses modos por latência, experiência do usuário e custo.

### Fallback e observabilidade

Aplicações maduras não assumem que o modelo sempre responderá bem. Elas monitoram erro, tempo de resposta e custo, e podem adotar fallback para fluxo humano, fila ou resposta simplificada em caso de falha.

## Exemplo prático

### Portal corporativo com assistente de conhecimento

O colaborador acessa um portal web, autentica com identidade corporativa, envia perguntas via API, o backend recupera contexto relevante e chama o modelo no Bedrock. Logs e métricas vão para CloudWatch, enquanto os documentos ficam versionados no S3.

## Raciocínio arquitetural

### Serverless para acelerar entrega e reduzir operação

Para grande parte dos casos de estudo e prova, API Gateway + Lambda + Bedrock + S3 + CloudWatch oferecem excelente equilíbrio entre simplicidade, governança e velocidade de implementação.

### Escolha síncrona ou assíncrona pela experiência esperada

Se o usuário espera resposta imediata, a arquitetura precisa ser otimizada para baixa latência. Se a tarefa é analisar um lote de documentos ou gerar relatórios, assíncrono pode ser melhor. O exame gosta dessa distinção.

## Boas práticas

- Isole a chamada ao modelo em uma camada bem definida da aplicação.
- Registre logs, métricas de latência e falhas desde o primeiro deploy.
- Use API Gateway e Lambda quando a carga e o perfil favorecem serverless.
- Controle o que vai para o prompt e o que volta do modelo.
- Projete fallback para timeout, erro de modelo ou baixa confiança.

## Dicas de prova

- Arquiteturas GenAI na AWS costumam combinar Bedrock, S3, API e observabilidade.
- Síncrono serve chat e assistentes; assíncrono serve documentos grandes e workflows longos.
- Managed services tendem a ser a resposta preferida quando o requisito não pede controle profundo de infra.
- Segurança e logs continuam sendo parte da arquitetura, não anexos.

## Armadilhas comuns

- Chamar o modelo diretamente do front-end sem camada de controle.
- Não prever timeout, fila de fallback ou tratamento de erro.
- Ignorar custo por token em fluxos de alto volume.
- Misturar dados sensíveis sem política de acesso.

## Resumo para revisão

- Aplicação GenAI é sistema completo, não apenas chamada ao modelo.
- Serverless costuma ser excelente ponto de partida na AWS.
- Síncrono e assíncrono devem seguir o caso de uso.
- Observabilidade e fallback aumentam robustez.
- Documentos, identidade e logs são tão importantes quanto o modelo.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 09 — Engenharia de Prompts](../09-Engenharia-de-Prompts/README.md).
- Continue para [Módulo 11 — Segurança e Conformidade em IA](../11-Seguranca-e-Conformidade-em-IA/README.md).

