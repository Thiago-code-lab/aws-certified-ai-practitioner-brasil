# Módulo 09 — Engenharia de Prompts

Engenharia de prompts é um dos temas mais práticos do exame. A prova quer que você entenda como instrução, contexto, formato e limites mudam o comportamento da aplicação generativa.

## Objetivo

Aprender a estruturar prompts mais úteis, previsíveis e seguros para casos reais na AWS, conectando a técnica com custo, qualidade e governança.

## Onde este tema aparece no AIF-C01

- Estruturar prompts com papel, contexto, objetivo e formato.
- Diferenciar zero-shot, few-shot e restrições de saída.
- Mitigar alucinação com engenharia de instrução e grounding.

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
| Amazon Bedrock | Ambiente natural para testar e operar prompts em aplicações com FM. | Aparece como serviço principal para orquestração de prompts. |
| Bedrock Guardrails | Complementa o prompt com políticas de conteúdo. | Importante em fluxos regulados. |
| AWS Lambda | Componente comum para aplicar templates de prompt em backend. | Aparece em integrações serverless. |
| Amazon CloudWatch | Observabilidade de chamadas e comportamento da aplicação. | Apoia testes e operação de prompt em produção. |

## Conceitos essenciais

### Estrutura de um bom prompt

Prompts melhores deixam claro o papel do modelo, o objetivo da tarefa, o contexto autorizado, o formato de saída e as restrições. Essa clareza reduz ambiguidade e ajuda a aplicação a ficar mais previsível.

### Zero-shot, few-shot e exemplos

Zero-shot é pedir a tarefa sem exemplos. Few-shot inclui alguns exemplos de entrada e saída para orientar comportamento. Em prova, few-shot costuma ser relevante quando a empresa precisa padronização maior sem partir direto para fine-tuning.

### Prompts como parte da arquitetura

Engenharia de prompts não é só texto bonito. Ele influencia custo, segurança, formato, latência e taxa de erro. Em produção, templates de prompt, versionamento e observabilidade são práticas importantes.

## Exemplo prático

### Resposta padronizada em JSON

Um assistente de suporte precisa devolver prioridade, resumo e ação recomendada em JSON. Um prompt genérico pode produzir texto livre. Um prompt com schema explícito, contexto mínimo necessário e exemplos tende a gerar saída mais previsível.

## Raciocínio arquitetural

### Prompt forte não substitui base confiável

Mesmo um prompt bem escrito não corrige falta de contexto factual. Quando o dado do negócio é essencial, prompt engineering deve caminhar com retrieval, regras de acesso e validação de saída.

### Versionamento de prompt também é governança

Quando prompts mudam comportamento da aplicação, eles passam a ser artefatos importantes. Versionar, testar e comparar prompts reduz regressões silenciosas e melhora a manutenção da solução.

## Boas práticas

- Descreva papel, objetivo, contexto, formato e limites da resposta.
- Use few-shot quando a tarefa exigir consistência de estilo ou estrutura.
- Peça formatos verificáveis, como JSON ou listas numeradas, quando a integração depender disso.
- Evite contexto excessivo e irrelevante.
- Versione prompts importantes e monitore o comportamento em produção.

## Dicas de prova

- Engenharia de prompts melhora instrução; RAG melhora factualidade baseada em fonte.
- Few-shot é útil para orientar padrão sem treinar modelo.
- Se a saída precisa ser consumida por sistema, estrutura explícita importa muito.
- Guardrails complementam prompt quando o caso exige política.

## Armadilhas comuns

- Achar que prompt sozinho resolve falta de conhecimento do negócio.
- Mandar contexto demais e degradar a resposta.
- Pedir saída livre quando a aplicação precisa estrutura rígida.
- Tratar prompt como texto descartável, sem teste e sem versionamento.

## Resumo para revisão

- Prompt é parte crítica da aplicação generativa.
- Clareza de tarefa e formato reduz variabilidade.
- Few-shot ajuda padronização.
- Prompt bom e RAG se complementam.
- Versionamento e observabilidade de prompt são práticas maduras.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 08 — Dados para IA](../08-Dados-para-IA/README.md).
- Continue para [Módulo 10 — IA Generativa na AWS](../10-IA-Generativa-na-AWS/README.md).

