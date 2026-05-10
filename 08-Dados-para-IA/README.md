# Módulo 08 — Dados para IA

Modelos só respondem bem quando recebem dados corretos, acessíveis e governados. O exame cobra exatamente esse raciocínio: dado limpo, atualizado e protegido é parte da arquitetura de IA, não detalhe secundário.

## Objetivo

Entender como preparar, armazenar, classificar e proteger dados usados em ML e GenAI, com foco em S3, metadados, rotulagem, chunking e sensibilidade da informação.

## Onde este tema aparece no AIF-C01

- Relacionar qualidade de dados com qualidade do modelo.
- Entender preparação documental para RAG.
- Reconhecer o papel de classificação e proteção de dados.

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
| Amazon S3 | Camada comum de armazenamento para datasets e documentos. | Aparece o tempo todo em pipelines de IA. |
| AWS Glue | Catalogação e transformação de dados. | Importante em preparo e organização de dados. |
| AWS Lake Formation | Governança de acesso sobre dados em lago. | Aparece quando o caso exige controle refinado do dado. |
| Amazon Macie | Descoberta de dados sensíveis em S3. | Importante para LGPD, PII e segurança. |

## Conceitos essenciais

### Qualidade, frescor e relevancia do dado

Modelos não compensam dados desatualizados ou mal organizados. Em GenAI, documentos antigos podem alimentar respostas erradas. Em ML supervisionado, rótulos ruins geram decisões ruins. O exame costuma cobrar esse efeito em linguagem de negócio.

### Chunking, metadados e curadoria documental

Para RAG, não basta jogar PDFs em um bucket. É preciso dividir o conteúdo em partes úteis, preservar contexto e manter metadados como data, área, versão e sensibilidade. Isso melhora recuperação e ajuda a controlar o que pode ou não ser usado.

### Protecao e classificacao de dados

Dados para IA frequentemente contêm PII, contratos, políticas internas ou dados regulados. A arquitetura precisa combinar acesso mínimo necessário, classificação, criptografia, versionamento e trilha de uso.

## Exemplo prático

### Base de conhecimento corporativa

Uma base de políticas internas precisa de versionamento, organização por domínio, remoção de documentos obsoletos e marcação de sensibilidade. Sem isso, a IA passa a recuperar material irrelevante, duplicado ou proibido.

## Raciocínio arquitetural

### S3 como origem, não como governance engine completa

S3 é excelente como armazenamento central, mas a governança vem do desenho ao redor: nomenclatura, ciclo de vida, catálogo, permissões e classificação. Em prova, o erro comum é tratar bucket como solução completa de governança.

### Preparação de dados é parte do design da aplicação

Chunking, limpeza, deduplicação e versionamento não são tarefas acessórias. São etapas arquiteturais que definem custo, qualidade de recuperação e risco de vazamento de informação.

## Boas práticas

- Versione documentos e datasets relevantes.
- Remova ou isole conteúdo obsoleto, duplicado ou sensível demais para o caso de uso.
- Use metadados para facilitar filtros e governança.
- Classifique dados antes de conectá-los a aplicações de IA.
- Projete pipeline de atualização para que a base não envelheça silenciosamente.

## Dicas de prova

- Mais dados não significa melhor resultado se a qualidade for ruim.
- Macie aparece quando o tema é PII em S3.
- Documentos para RAG precisam de preparo, não só armazenamento.
- Lake Formation reforça governança sobre dados em escala.

## Armadilhas comuns

- Subir arquivos sem metadados e esperar recuperação contextual precisa.
- Misturar material válido e obsoleto na mesma base sem controle.
- Ignorar dados sensíveis antes de expor uma base documental à IA.
- Achar que o modelo corrigirá problemas de qualidade do dado.

## Resumo para revisão

- Qualidade de dado é fator decisivo em IA e GenAI.
- RAG depende de chunking e metadados bem pensados.
- S3 guarda; governança organiza e protege.
- Macie ajuda a localizar dados sensíveis em S3.
- Dados atualizados e confiáveis sustentam respostas melhores.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 07 — IA Responsável e Governança](../07-IA-Responsavel-e-Governanca/README.md).
- Continue para [Módulo 09 — Engenharia de Prompts](../09-Engenharia-de-Prompts/README.md).

