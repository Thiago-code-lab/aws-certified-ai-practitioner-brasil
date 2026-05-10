# Módulo 04 — Modelos Fundacionais e LLMs

Este módulo conecta teoria e arquitetura: o que são foundation models, como LLMs se encaixam nesse universo e por que embeddings, vetores e RAG aparecem juntos em tantas soluções na AWS.

## Objetivo

Entender o papel dos modelos fundacionais em aplicações reais, diferenciar geração de texto de representação vetorial e construir o raciocínio correto para RAG, embeddings e bases vetoriais.

## Onde este tema aparece no AIF-C01

- Definir foundation model, LLM, embedding e vector database.
- Diferenciar RAG de fine-tuning.
- Entender por que retrieval melhora contexto e governança.

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
| Amazon Bedrock | Disponibiliza FMs e recursos como Knowledge Bases. | Camada principal para GenAI gerenciada. |
| Amazon OpenSearch Serverless | Pode atuar como armazenamento vetorial em arquiteturas de recuperação. | Aparece como componente de busca semântica e RAG. |
| Amazon Aurora PostgreSQL com pgvector | Alternativa quando o caso já usa banco relacional e precisa vetores. | Útil em comparações arquiteturais. |
| Amazon S3 | Origem comum dos documentos indexados em RAG. | Componente frequente para bases documentais. |

## Conceitos essenciais

### Foundation models e LLMs

Foundation models são modelos amplos treinados para servir como base de múltiplas tarefas. LLMs são foundation models especializados em linguagem natural. Em prova, o ponto central é perceber que um FM pode ser texto, imagem ou multimodal; LLM é um caso importante dentro desse universo.

### Embeddings e similaridade semantica

Embeddings transformam texto, imagem ou outro conteúdo em vetores numéricos que preservam significado semântico. Isso permite comparar proximidade entre documentos ou perguntas, baseando a recuperação em sentido e não apenas em palavras idênticas.

### Vector databases e RAG

Uma base vetorial armazena embeddings e permite busca por similaridade. Em RAG, a pergunta do usuário também vira embedding, os itens semanticamente mais próximos são recuperados e então enviados como contexto ao modelo gerador. Esse padrão ajuda a reduzir alucinações e manter respostas alinhadas aos dados da empresa.

## Exemplo prático

### Assistente de compliance com RAG

A área de compliance precisa responder dúvidas com base em políticas, contratos e normas atualizadas. Em vez de treinar um novo modelo sempre que os documentos mudarem, a empresa pode indexar os textos e recuperar os trechos relevantes no momento da pergunta.

```
Documentos em S3 -> chunking e embeddings -> indice vetorial -> pergunta do usuario -> retrieval -> LLM -> resposta
```

## Raciocínio arquitetural

### Quando RAG costuma vencer fine-tuning

Quando a prioridade é usar conhecimento interno atualizado, controlar a origem da resposta e reduzir custo de adaptação. Fine-tuning pode ser útil para estilo ou comportamento, mas RAG tende a ser a resposta mais pragmática para conhecimento documental mutável.

### Embeddings não geram texto

Embeddings representam conteúdo. Quem gera a resposta final é o modelo gerador. Essa distinção é importante porque várias questões de prova tentam confundir o papel da base vetorial com o papel do LLM.

## Boas práticas

- Use chunking coerente com a estrutura do documento.
- Armazene metadados úteis para filtrar contexto antes da recuperação.
- Reavalie a base vetorial quando os documentos forem atualizados.
- Separe claramente a função de recuperar da função de gerar.
- Valide se a aplicação precisa de RAG ou se um prompt simples já basta.

## Dicas de prova

- Embedding representa; LLM gera.
- RAG recupera contexto externo antes da resposta.
- Base vetorial não substitui o repositório fonte nem a política de acesso.
- Se o conhecimento muda com frequência, RAG costuma ser melhor que re-treino.

## Armadilhas comuns

- Achar que embeddings e geração de texto são a mesma coisa.
- Confundir base vetorial com data lake ou banco transacional geral.
- Usar fine-tuning quando o problema é atualização de conhecimento.
- Ignorar metadados e mandar contexto irrelevante para o modelo.

## Resumo para revisão

- Foundation models podem atender várias tarefas; LLM é um FM focado em linguagem.
- Embeddings sustentam busca semântica.
- RAG une retrieval e geração para fundamentar respostas.
- Vector database acelera recuperação por similaridade.
- A escolha entre RAG e fine-tuning depende do tipo de adaptação necessária.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 03 — Fundamentos de Machine Learning](../03-Fundamentos-de-Machine-Learning/README.md).
- Continue para [Módulo 05 — Amazon Bedrock](../05-Amazon-Bedrock/README.md).
