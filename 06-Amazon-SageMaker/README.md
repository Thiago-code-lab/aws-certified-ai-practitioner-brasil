# Módulo 06 — Amazon SageMaker AI

SageMaker AI aparece quando o problema deixa de ser apenas usar um modelo pronto e passa a exigir preparo de dados, treinamento, avaliação, implantação e operação de ML em escala.

## Objetivo

Compreender o papel do SageMaker AI no ecossistema da AWS, incluindo Studio, Canvas, JumpStart, treinamento, tipos de inferência e diferença prática para Bedrock.

## Onde este tema aparece no AIF-C01

- Identificar quando o enunciado pede ML customizado ou ciclo de vida de modelos.
- Distinguir treinamento, deploy e monitoramento no SageMaker AI.
- Comparar no-code/no-code assistido com abordagens mais técnicas.

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
| Amazon SageMaker AI | Plataforma de ponta a ponta para ML. | Cai quando há necessidade de construir e operar modelos customizados. |
| SageMaker Studio | Ambiente integrado para experimentação e desenvolvimento. | Pode aparecer como interface de trabalho de cientistas de dados. |
| SageMaker Canvas | Experiência de ML para analistas sem foco em código. | Aparece em cenários de democratização do ML. |
| SageMaker JumpStart | Modelos e soluções pré-configurados. | Ajuda a acelerar adoção sem começar do zero. |

## Conceitos essenciais

### Ciclo de vida de ML no SageMaker AI

SageMaker AI cobre preparação de dados, experimentação, treinamento, ajustes, deploy, monitoramento e governança. Isso o diferencia de serviços pontuais: a proposta é servir como plataforma operacional para workloads de ML.

### Opções de inferência

A inferência pode ser em tempo real, serverless, assíncrona ou em lote. O AIF-C01 não entra em detalhes profundos de tuning, mas espera que você entenda quando uma carga intermitente pede serverless e quando um processamento grande e tolerante a tempo pede batch.

### SageMaker AI vs Bedrock

Se o problema é usar FMs gerenciados, Bedrock é o nome mais forte. Se o problema é construir, treinar e operar modelos customizados, SageMaker AI assume o protagonismo. Em várias questões, o segredo é ler se a empresa quer consumir IA pronta ou desenvolver seu próprio pipeline de ML.

## Exemplo prático

### Previsão de demanda com dados históricos próprios

Uma empresa possui histórico detalhado de vendas e quer treinar um modelo específico para seu contexto. Nesse caso, a necessidade deixa de ser apenas consumir um FM e passa a envolver preparo de dados, experimento, ajuste e implantação. Esse é o território clássico do SageMaker AI.

## Raciocínio arquitetural

### Canvas para democratizar, Studio para aprofundar

Canvas faz sentido quando usuários de negócio precisam criar previsões ou classificações sem programar intensamente. Studio faz sentido para times técnicos que precisam notebooks, pipelines, tuning e integração mais profunda.

### Escolha o modo de inferência pelo comportamento da carga

Se a carga é esporádica e sensível a custo ocioso, serverless faz sentido. Se exige resposta contínua e estável, endpoint de tempo real pode ser mais adequado. Se a tarefa processa grandes lotes off-line, batch costuma ser a resposta natural.

## Boas práticas

- Defina claramente se o problema exige modelo customizado ou serviço gerenciado pronto.
- Use S3 como base organizada para datasets e artefatos.
- Escolha o modo de inferência conforme latência, custo e padrão de tráfego.
- Mantenha rastreabilidade dos experimentos e versões do modelo.
- Evite operar capacidade permanente quando a carga for intermitente.

## Dicas de prova

- Canvas aparece quando a empresa quer ML sem código pesado.
- JumpStart acelera prototipagem com modelos e soluções pré-montadas.
- Batch inference é diferente de endpoint em tempo real.
- Se a pergunta é sobre treinar e operar ML próprio, pense em SageMaker AI.

## Armadilhas comuns

- Confundir uso de FM por API com ciclo completo de ML customizado.
- Escolher endpoint real-time para carga totalmente batch.
- Ignorar custos de manter capacidade sempre ligada.
- Achar que Canvas elimina necessidade de dados bem preparados.

## Resumo para revisão

- SageMaker AI é plataforma de ML de ponta a ponta.
- Canvas, Studio e JumpStart atendem perfis e necessidades diferentes.
- Treinamento e inferência são fases distintas dentro da plataforma.
- A escolha do modo de inferência afeta custo e latência.
- Bedrock e SageMaker AI não competem em tudo; muitas vezes se complementam.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 05 — Amazon Bedrock](../05-Amazon-Bedrock/README.md).
- Continue para [Módulo 07 — IA Responsável e Governança](../07-IA-Responsavel-e-Governanca/README.md).

