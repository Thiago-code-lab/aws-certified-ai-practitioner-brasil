# Módulo 14 — Integração com Aplicações

IA útil é IA integrada. Este módulo trata de como conectar serviços de IA a aplicações, APIs, eventos, filas e componentes corporativos sem perder controle da arquitetura.

## Objetivo

Entender como acoplar capacidades de IA a aplicações modernas na AWS usando padrões de integração síncrona, assíncrona e orientada a eventos.

## Onde este tema aparece no AIF-C01

- Conectar IA a APIs, filas, eventos e fluxos de negócio.
- Entender padrões de backend para consumo de modelos.
- Reconhecer implicações de latência, retries e observabilidade.

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
| AWS Lambda | Backend leve para integração e orquestração. | Muito comum em arquiteturas serverless com IA. |
| Amazon API Gateway | Camada de API para clientes e apps. | Forte em cenários web e mobile. |
| Amazon EventBridge | Eventos e automação desacoplada. | Útil em workflows assíncronos. |
| Amazon SQS | Fila para amortecer carga e desacoplar processamento. | Aparece quando a aplicação precisa resiliência e processamento em background. |

## Conceitos essenciais

### Integracao sincrona

É a escolha natural quando o usuário espera resposta imediata: chat, resumo rápido, classificação instantânea. Ela exige cuidado com timeout, taxa de chamadas, formato de saída e experiência do usuário.

### Integração assíncrona e orientada a eventos

Quando a IA participa de fluxos demorados, como processamento de documento, enriquecimento de cadastro ou análise de lote, filas e eventos reduzem acoplamento e aumentam resiliência.

### Camada de aplicação e controle

É boa prática intermediar a IA com uma camada de aplicação que aplique autenticação, observabilidade, versionamento de prompt, transformação de dados e tratamento de falha. Isso melhora governança e reduz exposição direta do modelo.

## Exemplo prático

### Classificação de e-mails em background

E-mails chegam, são colocados em fila, um backend os processa com IA, grava o resultado e envia evento para outro sistema. O usuário não precisa esperar a resposta em tempo real, então a arquitetura assíncrona traz mais robustez.

## Raciocínio arquitetural

### Fila como proteção operacional

SQS ajuda a absorver picos, desacoplar o produtor do consumidor e permitir retries controlados. Em fluxos com IA, isso é útil quando o modelo tem latência variável ou quando o processamento não precisa ser imediato.

### API bem desenhada simplifica consumo da IA

API Gateway e Lambda podem expor uma interface consistente para o front-end, escondendo detalhes do modelo, do prompt, da base de conhecimento e das políticas internas.

## Boas práticas

- Use síncrono apenas quando a experiência realmente exigir resposta imediata.
- Desacople tarefas longas com eventos e filas.
- Padronize contratos de API e formatos de resposta.
- Aplique retries e tratamento de exceção em pontos previsíveis.
- Centralize observabilidade e controle na camada de aplicação.

## Dicas de prova

- SQS e EventBridge costumam aparecer quando o enunciado fala em resiliência e processamento em background.
- API Gateway + Lambda é combinação clássica para expor IA de forma controlada.
- Integração bem feita protege o modelo e melhora governança.
- Síncrono não é obrigatório só porque existe usuário humano no fluxo.

## Armadilhas comuns

- Forçar tudo para fluxo síncrono e degradar experiência ou custo.
- Expor o modelo diretamente sem autenticação, validação e logging.
- Ignorar retries e idempotência em processos assíncronos.
- Acoplar demais a aplicação ao comportamento interno do modelo.

## Resumo para revisão

- Integração é parte central da solução de IA.
- Síncrono atende experiência imediata; assíncrono atende robustez e lote.
- Lambda, API Gateway, EventBridge e SQS são peças-chave.
- A camada de aplicação protege a solução e organiza contratos.
- Resiliência importa também em IA.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 13 — Serviços de IA da AWS](../13-Servicos-de-IA-da-AWS/README.md).
- Continue para [Módulo 15 — Boas Práticas e Otimização](../15-Boas-Praticas-e-Otimizacao/README.md).

