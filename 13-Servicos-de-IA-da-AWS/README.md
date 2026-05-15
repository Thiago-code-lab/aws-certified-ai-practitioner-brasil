# Módulo 13 — Serviços de IA da AWS

Este módulo faz a revisão orientada por serviço. Em vez de decorar listas, o foco é entender qual problema cada serviço resolve e como ele costuma aparecer em alternativa de prova.

## Objetivo

Consolidar os principais serviços de IA da AWS relevantes para o AIF-C01 e saber distingui-los em cenários práticos, incluindo a diferença entre serviços especializados, GenAI e plataformas de ML.

## Onde este tema aparece no AIF-C01

- Reconhecer rapidamente o serviço AWS mais alinhado ao caso de uso.
- Comparar Bedrock, SageMaker AI e serviços especializados.
- Revisar serviços em escopo do exame com olhar prático.

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
| Amazon Bedrock | GenAI e foundation models. | Centro das questões generativas. |
| Amazon Comprehend / Textract / Rekognition / Transcribe / Translate / Polly / Lex | Serviços especializados de IA. | Aparecem como respostas mais diretas em casos específicos. |
| Amazon Q Business / Q Developer | Experiências assistidas por IA para busca e produtividade. | Podem aparecer como soluções de produtividade empresarial. |
| Amazon Personalize | Recomendações personalizadas. | Importante quando o caso fala em recomendação de itens. |

## Conceitos essenciais

### Catálogo mental por tipo de problema

Se o problema é fala, pense em Transcribe ou Polly. Se é documento, pense em Textract. Se é recomendação, pense em Personalize. Se é resposta aberta ou assistente com linguagem natural mais flexível, pense em Bedrock.

### Serviços especializados ainda são muito fortes

Um erro comum em preparação para IA é esquecer que a AWS já oferece serviços de IA especializados há anos. Em muitas questões, esses serviços continuam sendo melhores respostas que arquiteturas generativas genéricas.

### Observação sobre escopo atual

A lista oficial de serviços em escopo do AIF-C01 deve ser priorizada. Um ponto importante: a documentação oficial do exame ainda cita Amazon Fraud Detector, mas a AWS deixou de aceitar novos clientes em **7 de novembro de 2025**. Para estudo de prova, vale entender o conceito; para projetos novos, a decisão arquitetural prática pode ser outra.

## Exemplo prático

### Mapa rápido por problema

Texto em áudio? Polly. Áudio em texto? Transcribe. Pergunta sobre documentos empresariais? Q Business ou Bedrock com base apropriada. Classificação ou sentimento em texto? Comprehend. Recomendação de produto? Personalize.

## Raciocínio arquitetural

### Serviço especializado para tarefa especializada

Quando a necessidade é clara e o serviço especializado existe, ele costuma ser mais barato, simples e governável. Esse padrão aparece repetidamente nas certificações AWS.

### Bedrock entra quando a flexibilidade de linguagem muda o jogo

Se o caso não é apenas classificar ou extrair, mas conversar, resumir, gerar ou responder com base em contexto, Bedrock volta a ser candidato forte — especialmente com grounding.

## Boas práticas

- Aprenda os serviços por problema de negócio, não por ordem alfabética.
- Diferencie serviços especializados de plataformas de ML e de GenAI.
- Priorize a lista oficial de serviços em escopo do exame.
- Entenda os limites conceituais de cada serviço.
- Considere sempre simplicidade, custo e governança.

## Dicas de prova

- Personalize é para recomendação; Comprehend é para NLP estruturado; Bedrock é para GenAI.
- Textract é forte em documentos; Rekognition em imagem/vídeo.
- Lex cobre bot conversacional gerenciado; Polly e Transcribe tratam voz.
- Q Business aparece em produtividade e busca empresarial assistida.

## Armadilhas comuns

- Usar LLM como resposta padrão para qualquer cenário.
- Confundir Personalize com solução de busca.
- Confundir Comprehend com Bedrock em tarefas que não exigem geração.
- Ignorar que o exame segue uma lista oficial de serviços em escopo.

## Resumo para revisão

- Serviço certo depende do problema certo.
- A AWS tem forte portfólio de IA especializada além de GenAI.
- Bedrock não substitui todos os serviços tradicionais de IA.
- Q Business, Personalize, Lex, Textract e Comprehend têm papéis claros.
- A lista oficial do AIF-C01 deve guiar sua revisão final.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 12 — Casos de Uso e Arquiteturas](../12-Casos-de-Uso-e-Arquiteturas/README.md).
- Continue para [Módulo 14 — Integração com Aplicações](../14-Integracao-com-Aplicacoes/README.md).

