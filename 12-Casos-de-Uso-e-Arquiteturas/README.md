# Módulo 12 — Casos de Uso e Arquiteturas

A certificação cobra menos fórmulas e mais julgamento: qual serviço atende melhor determinado problema? Este módulo organiza esse raciocínio em cenários reais e comparações úteis.

## Objetivo

Transformar conceitos em decisão de arquitetura, comparando serviços e padrões para chatbots, extração documental, recomendações, resumo, classificação e automação assistida.

## Onde este tema aparece no AIF-C01

- Mapear caso de uso ao serviço mais coerente.
- Comparar serviços prontos, Bedrock e ML customizado.
- Praticar raciocínio por requisito de negócio.

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
| Amazon Bedrock | Geração de texto, resumo, Q&A e assistentes contextualizados. | Muito comum em cenários GenAI. |
| Amazon Textract | Extração de texto, formulários e tabelas de documentos. | Aparece em automação documental. |
| Amazon Comprehend | NLP gerenciado para entidade, sentimento e classificação. | Útil em comparação com LLM em tarefas estruturadas. |
| Amazon Rekognition | Visão computacional gerenciada. | Aparece em cenários de imagem e vídeo. |

## Conceitos essenciais

### Comece pelo tipo de resultado esperado

Se a empresa quer extrair campos de um PDF, talvez Textract seja mais direto que um LLM. Se quer analisar sentimento em reviews, Comprehend pode ser mais simples. Se quer responder perguntas com linguagem natural sobre uma base própria, Bedrock com grounding pode fazer mais sentido.

### Servico pronto vs modelo generativo

Muitas questões da AWS comparam um serviço gerenciado especializado com uma solução mais aberta baseada em foundation model. A resposta correta costuma privilegiar o serviço mais simples e diretamente alinhado ao problema, especialmente quando ele já existe pronto.

### Arquitetura como composicao

Em cenários reais, é comum combinar múltiplos serviços: Textract para extrair, S3 para armazenar, Bedrock para resumir, Lambda para orquestrar e CloudWatch para observar. O exame valoriza essa leitura de solução completa.

## Exemplo prático

### Automacao de contratos

Um pipeline pode usar Textract para extrair informações de contratos, enviar os resultados estruturados para armazenamento e depois usar Bedrock para gerar um resumo executivo em linguagem natural. Cada serviço cumpre um papel diferente.

## Raciocínio arquitetural

### Use o serviço mais específico quando o problema já está bem conhecido

OCR, moderação de imagem, transcrição e análise de sentimento são exemplos em que a AWS já oferece serviços gerenciados especializados. Em prova, eles costumam ser preferidos a arquiteturas mais abertas e complexas baseadas em FM, quando o requisito é objetivo.

### Use FM quando o valor está na flexibilidade da linguagem

Quando o problema exige resumo contextualizado, resposta aberta, composição textual ou interação conversacional mais rica, foundation models passam a fazer mais sentido — especialmente combinados com dados corporativos.

## Boas práticas

- Leia o verbo principal do caso: extrair, classificar, gerar, responder, moderar, recomendar.
- Prefira o serviço mais especializado quando ele atende ao requisito diretamente.
- Combine serviços em pipeline quando o caso pede mais de uma capacidade.
- Avalie custo, latência, governança e manutenção do desenho.
- Evite superengenharia com LLM onde um serviço pronto resolve melhor.

## Dicas de prova

- Textract para documentos; Rekognition para imagem/vídeo; Comprehend para NLP gerenciado; Bedrock para GenAI.
- Serviço pronto costuma ganhar quando o caso é específico e comum.
- LLM não é substituto automático de todos os serviços especializados.
- Procure sempre o requisito dominante do cenário.

## Armadilhas comuns

- Usar Bedrock para tudo e ignorar serviços especializados mais diretos.
- Não separar extração estruturada de geração textual.
- Responder pela popularidade do serviço, e não pela aderência ao requisito.
- Ignorar composição de múltiplos serviços quando o caso é pipeline.

## Resumo para revisão

- Arquitetura de IA começa pelo problema certo.
- Serviços especializados seguem sendo muito relevantes na AWS.
- Foundation models entram forte quando a flexibilidade da linguagem importa.
- Pipelines combinados são comuns em casos reais.
- A prova recompensa soluções alinhadas ao requisito dominante.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 11 — Segurança e Conformidade em IA](../11-Seguranca-e-Conformidade-em-IA/README.md).
- Continue para [Módulo 13 — Serviços de IA da AWS](../13-Servicos-de-IA-da-AWS/README.md).

