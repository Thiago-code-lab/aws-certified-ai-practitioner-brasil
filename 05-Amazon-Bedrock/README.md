# Módulo 05 — Amazon Bedrock

Amazon Bedrock é o eixo mais importante da certificação para IA generativa na AWS. O exame cobra o que ele resolve, quando usá-lo e como integrá-lo com segurança e governança.

## Objetivo

Dominar o papel do Bedrock como plataforma gerenciada para foundation models, incluindo Knowledge Bases, Guardrails, Agents e critérios de escolha frente a SageMaker AI ou infraestrutura própria.

## Onde este tema aparece no AIF-C01

- Consumir modelos fundacionais sem gerenciar infraestrutura.
- Entender Knowledge Bases, Guardrails e Agents.
- Relacionar Bedrock com custo, latência, segurança e rapidez de entrega.

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
| Amazon Bedrock | Camada principal de acesso a modelos fundacionais por API. | Serviço central do blueprint de GenAI. |
| Bedrock Knowledge Bases | Grounding gerenciado para RAG. | Aparece quando o enunciado fala em responder com base em documentos. |
| Bedrock Guardrails | Controles de segurança e política sobre entrada e saída. | Importante em cenários de responsible AI e segurança. |
| Bedrock Agents | Orquestração de ações e uso de ferramentas por aplicações generativas. | Útil quando o modelo precisa executar etapas além de responder texto. |

## Conceitos essenciais

### Bedrock como camada gerenciada

Bedrock abstrai o esforço de hospedar e escalar foundation models. Em vez de operar clusters, endpoints e capacidade de GPU, o time consome modelos por APIs e recursos gerenciados. Isso acelera experimentação, prototipagem e entrada em produção.

### Knowledge Bases, Guardrails e Agents

Knowledge Bases ajudam a conectar documentos e recuperação contextual. Guardrails aplicam políticas sobre conteúdo, tópicos proibidos, linguagem sensível e PII. Agents permitem que o modelo acione ferramentas e execute ações em sistemas conectados, ampliando a utilidade da aplicação.

### Quando Bedrock aparece como melhor resposta

Quando o enunciado prioriza simplicidade operacional, rapidez para usar FMs, integração com recursos gerenciados da AWS e redução do esforço de infraestrutura. Se a pergunta pede treinar modelos muito específicos do zero, a discussão muda para SageMaker AI.

## Exemplo prático

### Assistente interno com base de conhecimento e proteção de saída

Uma empresa quer um assistente para responder perguntas sobre procedimentos internos, mas precisa bloquear vazamento de PII e manter as respostas dentro de tópicos permitidos. Uma arquitetura com Bedrock Knowledge Bases e Guardrails atende esse desenho com baixo esforço operacional.

```
Usuário -> aplicação -> Bedrock Guardrails -> Knowledge Base -> modelo -> resposta filtrada
```

## Raciocínio arquitetural

### Bedrock vs infraestrutura própria

Hospedar um modelo diretamente em infraestrutura própria aumenta controle, mas também aumenta operação, custo fixo e complexidade. Em prova, se não houver exigência explícita de customização profunda da camada de modelo, Bedrock tende a ser mais consistente com a filosofia managed-first da AWS.

### Guardrails complementam, não substituem, segurança

Guardrails ajudam no conteúdo gerado e na experiência da aplicação, mas não substituem IAM, criptografia, logs, segregação de dados e revisão humana. O exame pode explorar essa diferença.

## Boas práticas

- Use Bedrock quando a prioridade for consumir FMs rapidamente com governança gerenciada.
- Aplique Guardrails para reduzir respostas fora de política e exposição indevida.
- Conecte Knowledge Bases a fontes documentais controladas e atualizadas.
- Monitore custo por token, latência e taxas de erro.
- Separe permissões de desenvolvimento, teste e produção.

## Dicas de prova

- Bedrock = consumo gerenciado de FMs; SageMaker AI = ciclo de ML mais customizado.
- Knowledge Bases aparecem quando o problema fala em documentos internos.
- Guardrails controlam conteúdo, mas não fazem IAM nem KMS.
- Agents entram quando o enunciado pede ação, fluxo ou uso de ferramenta.

## Armadilhas comuns

- Confundir Guardrails com controle de acesso de identidade.
- Assumir que Knowledge Base substitui a curadoria dos documentos fonte.
- Usar Bedrock Agents sem pensar em observabilidade e validação do fluxo.
- Ignorar custo de inferência e tamanho de contexto.

## Resumo para revisão

- Bedrock entrega FMs por API com baixa carga operacional.
- Knowledge Bases conectam grounding e recuperação.
- Guardrails ajudam na política de conteúdo.
- Agents ampliam a aplicação com ações e ferramentas.
- O exame valoriza Bedrock como caminho natural para GenAI gerenciada na AWS.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 04 — Modelos Fundacionais e LLMs](../04-Modelos-Fundacionais-e-LLMs/README.md).
- Continue para [Módulo 06 — Amazon SageMaker AI](../06-Amazon-SageMaker/README.md).

