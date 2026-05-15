# Módulo 07 — IA Responsável e Governança

O exame não trata responsible AI como tema abstrato. Ele conecta risco, revisão humana, explicabilidade, guardrails, auditoria e políticas de uso a cenários bem concretos.

## Objetivo

Entender como traduzir princípios de IA responsável e governança em decisões práticas de arquitetura, operação e políticas dentro da AWS.

## Onde este tema aparece no AIF-C01

- Compreender fairness, transparência, accountability e revisão humana.
- Relacionar governança com monitoramento, logs e políticas.
- Reconhecer quando o caso pede controles adicionais antes da automação total.

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
| Bedrock Guardrails | Controles de conteúdo e proteção em aplicações generativas. | Cai em perguntas sobre políticas de uso. |
| Amazon SageMaker Clarify | Análise de viés e explicabilidade em workflows de ML. | Conecta responsible AI com avaliação técnica. |
| Amazon Augmented AI (A2I) | Revisão humana em etapas selecionadas do fluxo. | Importante quando o enunciado pede human-in-the-loop. |
| AWS CloudTrail | Auditoria de ações e rastreabilidade operacional. | Aparece em governança e investigação. |

## Conceitos essenciais

### Responsible AI em linguagem pratica

IA responsável significa criar sistemas úteis sem abrir mão de segurança, justiça, transparência e supervisão adequada. Em uma prova da AWS, isso aparece como decisão arquitetural: quando automatizar, quando revisar, quando bloquear conteúdo e como registrar o que aconteceu.

### Viés, explicabilidade e supervisao humana

Modelos podem reproduzir vieses do dado ou do contexto. Em cenários de crédito, saúde, RH e compliance, o exame tende a valorizar revisão humana, documentação de decisão e mecanismos de explicabilidade. Nem toda tarefa deve ser totalmente automatizada.

### Governanca como processo continuo

Governança não se resume a uma política escrita. Ela envolve controle de acesso, aprovação de fontes, versionamento de prompts ou modelos, monitoramento, auditoria e correção de desvios. Na AWS, isso se apoia em múltiplos serviços e processos, não em um único botão.

## Exemplo prático

### Assistente de RH com decisao humana obrigatoria

Um assistente pode resumir candidaturas e destacar critérios, mas a decisão final de contratação não deve ser entregue integralmente ao modelo. O papel da IA é apoiar, não substituir, o processo decisório em contextos sensíveis.

## Raciocínio arquitetural

### Human-in-the-loop onde o risco e alto

Quando o impacto para o usuário é relevante, a melhor arquitetura combina automação com revisão humana. A2I e fluxos de aprovação são exemplos práticos de como implementar isso. A prova costuma sinalizar esse caminho com palavras como 'alto impacto', 'regulado', 'sensível' ou 'revisão obrigatória'.

### Politica, observabilidade e resposta a incidentes

Aplicações responsáveis precisam registrar entradas, saídas, ações disparadas e violações de política. Isso permite investigação, melhoria contínua e evidência de conformidade. Sem logs e trilhas, governança vira discurso sem execução.

## Boas práticas

- Use revisão humana em cenários de alto impacto.
- Defina políticas explícitas para dados, prompts e respostas aceitáveis.
- Monitore desvio de comportamento, segurança e reclamações de usuários.
- Avalie viés e explicabilidade quando houver decisão sensível.
- Registre eventos relevantes para auditoria e aprendizado.

## Dicas de prova

- Responsible AI quase sempre conversa com segurança, governança e revisão humana.
- Clarify e A2I são nomes fortes quando a pergunta fala em viés ou supervisão humana.
- Guardrails tratam conteúdo; CloudTrail e IAM tratam governança operacional.
- Se o caso envolve pessoas, finanças ou conformidade, desconfie de automação total.

## Armadilhas comuns

- Achar que responsible AI é apenas filtro de linguagem ofensiva.
- Ignorar revisão humana em decisões reguladas.
- Confundir explicabilidade com simples logging técnico.
- Tratar governança como tarefa única do time jurídico.

## Resumo para revisão

- IA responsável é princípio traduzido em arquitetura e operação.
- Risco alto pede human-in-the-loop.
- Viés, explicabilidade e auditoria fazem parte do pacote.
- Governança depende de processo contínuo e serviços combinados.
- A AWS oferece recursos para política, logs e revisão.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 06 — Amazon SageMaker AI](../06-Amazon-SageMaker/README.md).
- Continue para [Módulo 08 — Dados para IA](../08-Dados-para-IA/README.md).

