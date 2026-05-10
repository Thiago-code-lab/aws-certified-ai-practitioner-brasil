# Módulo 02 — Fundamentos de IA Generativa

Aqui começa a base conceitual de IA generativa: prompt, token, contexto, temperatura, grounding e alucinação. Este é um dos pontos em que a prova exige clareza prática, não definições decoradas.

## Objetivo

Capacitar você a explicar como um foundation model gera saídas, por que respostas podem variar entre chamadas e quais controles tornam uma aplicação generativa mais previsível, segura e útil.

## Onde este tema aparece no AIF-C01

- Entender o fluxo entrada-contexto-modelo-saída.
- Diferenciar prompt engineering, grounding, fine-tuning e guardrails.
- Reconhecer risco de alucinação e como mitigá-lo.

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
| Amazon Bedrock | Execução de modelos fundacionais e ferramentas de GenAI. | Serviço central das questões de GenAI na AWS. |
| Amazon Nova | Família de modelos da AWS disponível via Bedrock. | Pode aparecer como opção nativa da AWS para texto, imagem e multimodalidade. |
| Amazon S3 | Fonte comum de documentos usados para grounding e RAG. | Aparece em fluxos com bases de conhecimento e preparação de dados. |
| Amazon CloudWatch | Observabilidade de chamadas, latência e erros em aplicações GenAI. | Importante quando o enunciado pede monitoramento operacional. |

## Conceitos essenciais

### Tokens, contexto e janela de contexto

Modelos de linguagem processam entrada e saída como tokens. Quanto maior o contexto enviado, maior tende a ser o custo e, dependendo do modelo, a latência. Em prova, isso aparece como necessidade de resumir, recuperar apenas o necessário e evitar prompts inchados.

### Temperatura, variacao e previsibilidade

Parâmetros de geração alteram o nível de criatividade e diversidade da resposta. Temperaturas mais baixas favorecem consistência; temperaturas mais altas favorecem variedade. Para tarefas operacionais, a prova tende a valorizar previsibilidade, especialmente quando há saída estruturada.

### Alucinacao e grounding

Alucinação ocorre quando o modelo produz conteúdo plausível, porém incorreto, incompleto ou inventado. Grounding reduz esse risco ao fornecer contexto confiável e atualizado, geralmente recuperado de uma base documental. RAG é uma forma prática de grounding.

## Exemplo prático

### Assistente de políticas internas

Uma empresa quer que seu assistente responda sobre férias, reembolso e viagens. Sem grounding, o modelo pode misturar políticas públicas genéricas com regras internas. Com documentos internos como contexto, a aplicação passa a responder com base em material corporativo real.

```
Pergunta do funcionario -> app -> recuperacao de documentos relevantes -> prompt com contexto -> Bedrock -> resposta
```

## Raciocínio arquitetural

### Prompt sozinho resolve o que ja esta no modelo

Se o conhecimento for genérico e estável, um bom prompt pode bastar. Mas, se o caso exige dados internos, políticas atualizadas ou documentos privados, o prompt precisa ser complementado por grounding. Essa distinção é frequente em prova.

### Nem todo problema de GenAI pede fine-tuning

Fine-tuning altera o comportamento do modelo com dados adicionais, mas nem sempre é a melhor primeira escolha. Para o AIF-C01, quando a necessidade é reduzir alucinação e responder com base em documentos do negócio, RAG costuma ser mais direto, mais barato e mais fácil de governar.

## Boas práticas

- Especifique papel, objetivo, contexto e formato de saída no prompt.
- Use grounding quando a resposta depender de informações internas ou recentes.
- Prefira parâmetros mais conservadores em tarefas operacionais e estruturadas.
- Monitore latência, custo por token e qualidade percebida.
- Adicione revisão humana quando a resposta influenciar decisões críticas.

## Dicas de prova

- Engenharia de prompts melhora instrução; RAG melhora contexto.
- Temperatura baixa favorece consistência; alta favorece criatividade.
- Alucinação não é eliminada só por usar um modelo melhor.
- Base de conhecimento não substitui segurança, curadoria e controle de acesso.

## Armadilhas comuns

- Achar que GenAI sempre retorna a mesma resposta para a mesma entrada.
- Confundir grounding com treinamento do modelo.
- Enviar contexto demais e piorar custo, latência e qualidade.
- Usar modelo generativo para uma tarefa que pede simples classificação.

## Resumo para revisão

- Tokens e janela de contexto impactam custo e latência.
- Prompt bom orienta; grounding sustenta; guardrails protegem.
- RAG é um padrão importante para reduzir alucinações com dados internos.
- Parâmetros de geração mudam criatividade e previsibilidade.
- GenAI precisa de governança, não apenas de um modelo forte.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 01 — Introdução a IA e ML](../01-Introducao-IA-e-ML/README.md).
- Continue para [Módulo 03 — Fundamentos de Machine Learning](../03-Fundamentos-de-Machine-Learning/README.md).

