# Módulo 01 — Introdução a IA e ML

Este módulo estabelece o vocabulário base do exame. A meta é distinguir IA, machine learning, deep learning e IA generativa sem cair em definições soltas ou acadêmicas demais.

## Objetivo

Ao final deste módulo, você deve conseguir explicar o que a AWS chama de workloads de IA, diferenciar treinamento de inferência e reconhecer quando um caso de uso pede um serviço pronto, um modelo customizado ou uma arquitetura generativa.

## Onde este tema aparece no AIF-C01

- Entender a diferença entre IA tradicional, ML e IA generativa.
- Reconhecer treinamento, validação, implantação e inferência como fases distintas.
- Identificar quando a resposta correta pede um serviço gerenciado da AWS em vez de infraestrutura bruta.

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
| Amazon S3 | Armazenamento de datasets, artefatos de treinamento e documentos para RAG. | Aparece como base de dados para ML e GenAI. |
| Amazon Bedrock | Camada gerenciada para consumir foundation models por API. | Cobrado como porta de entrada para IA generativa. |
| Amazon SageMaker AI | Plataforma para preparar dados, treinar, ajustar e implantar modelos customizados. | Cobrado quando a pergunta exige ML customizado. |
| AWS IAM | Controle de acesso a dados, modelos e aplicações de IA. | Aparece em cenários de segurança desde o início do blueprint. |

## Conceitos essenciais

### IA, ML, deep learning e IA generativa

IA é o guarda-chuva mais amplo: qualquer técnica que permita ao software executar tarefas associadas a raciocínio, percepção ou tomada de decisão. Machine learning é um subconjunto da IA em que o sistema aprende padrões a partir de dados. Deep learning usa redes neurais com várias camadas. IA generativa vai além da classificação ou previsão e cria novos conteúdos, como texto, imagem, áudio ou código.

### Treinamento vs inferência

Treinamento é a fase em que um modelo aprende a partir de exemplos. Inferência é o momento em que o modelo já treinado recebe uma entrada nova e produz uma resposta. Em prova, isso aparece com frequência como comparação de custo, latência e responsabilidade operacional: treinamento costuma ser mais pesado e eventual; inferência, mais recorrente e conectada à experiência do usuário.

### Managed-first mindset na AWS

A AWS costuma recompensar, em questões de certificação, a escolha mais gerenciada que atenda aos requisitos. Se a empresa só quer usar IA generativa em produção, Bedrock tende a ser melhor resposta do que montar infraestrutura própria. Se precisa criar um modelo totalmente customizado com dados proprietários, SageMaker AI entra com mais força.

## Exemplo prático

### Triagem automática de chamados

Uma central de atendimento recebe milhares de tickets por dia. Se o objetivo é classificar chamados por prioridade e área responsável, isso já pode ser resolvido com ML supervisionado ou até com um serviço gerenciado de linguagem natural, dependendo do escopo. Se o objetivo for gerar respostas contextualizadas a partir de uma base interna, o problema muda para GenAI com grounding.

```
Chamado do cliente -> API/app interna -> modelo/serviço AWS -> classificação ou resposta -> fila/atendente
```

## Raciocínio arquitetural

### Comece pelo objetivo de negócio, não pelo modelo

No exame, perguntas bem formuladas descrevem uma necessidade operacional: reduzir tempo de atendimento, resumir documentos, detectar fraudes, organizar imagens ou melhorar busca interna. A decisão arquitetural correta nasce do resultado esperado. Se o resultado é previsão numérica, um LLM provavelmente não é a melhor opção. Se o resultado é texto contextualizado, um foundation model pode fazer sentido.

### Separar plataforma de ML de serviço de IA pronto

Serviços prontos são ideais quando o problema já está bem representado por um caso comum, como OCR, tradução ou análise de sentimento. Plataformas de ML entram quando o negócio precisa treinar, ajustar, avaliar e implantar um modelo próprio. Essa distinção é central para o AIF-C01.

## Boas práticas

- Defina a métrica de sucesso antes de escolher o serviço.
- Trate treinamento e inferência como fases com custos e riscos diferentes.
- Prefira serviços gerenciados quando a personalização pesada não for requisito.
- Mantenha dados, modelos e permissões sob governança desde o início.
- Faça revisão humana em tarefas críticas ou reguladas.

## Dicas de prova

- Se a pergunta fala em criar conteúdo novo, pense primeiro em GenAI e foundation models.
- Se fala em prever ou classificar com base em histórico rotulado, pense em ML supervisionado.
- Se a empresa não quer gerenciar infraestrutura nem treinar modelo, Bedrock costuma ganhar força.
- Se o enunciado pede controle fino do ciclo de ML, SageMaker AI tende a ser o caminho.

## Armadilhas comuns

- Confundir IA generativa com qualquer tipo de automação inteligente.
- Assumir que todo caso de uso de IA exige treinamento de modelo próprio.
- Achar que inferência e treinamento têm o mesmo perfil de custo e latência.
- Ignorar IAM e segurança por estar em um módulo introdutório.

## Resumo para revisão

- IA é o guarda-chuva; ML é um subconjunto; IA generativa cria novo conteúdo.
- Treinamento ensina; inferência responde.
- Bedrock é o ponto forte da AWS para consumir FMs por API.
- SageMaker AI é a plataforma para ML customizado e operação do ciclo de vida.
- A certificação valoriza escolhas gerenciadas e alinhadas ao caso de uso.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Continue para [Módulo 02 — Fundamentos de IA Generativa](../02-Fundamentos-de-IA-Generativa/README.md).

