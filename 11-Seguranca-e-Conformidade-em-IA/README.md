# Módulo 11 — Segurança e Conformidade em IA

Segurança em IA não é um módulo isolado: ela atravessa dado, modelo, prompt, identidade, logs e integração. O exame gosta justamente dessa visão sistêmica.

## Objetivo

Capacitar você a identificar controles de segurança e conformidade aplicáveis a soluções de IA na AWS, com foco em acesso, criptografia, auditoria, dados sensíveis e separação de ambientes.

## Onde este tema aparece no AIF-C01

- Relacionar IAM, KMS, CloudTrail e segredos a workloads de IA.
- Entender proteção de dados em repouso, em trânsito e durante uso.
- Reconhecer quando o caso pede revisão de acesso, PII e auditoria.

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
| AWS IAM | Controle de identidade e permissão. | Base de acesso a dados, modelos e aplicações. |
| AWS KMS | Gestão de chaves e criptografia. | Importante em proteção de dados sensíveis. |
| AWS CloudTrail | Auditoria de ações e uso dos serviços. | Relevante em governança e investigação. |
| AWS Secrets Manager | Proteção de segredos usados pela aplicação. | Importante em integrações com APIs e bancos. |

## Conceitos essenciais

### Shared responsibility em IA

Mesmo usando serviços gerenciados, o cliente continua responsável por identidade, permissões, dados enviados, integrações e políticas da aplicação. Em IA generativa, isso inclui prompts, documentos conectados, segredos, logs e decisões de uso.

### Protecao de dados ao redor do modelo

Não basta criptografar o bucket. É preciso controlar quem pode ler documentos, chamar modelos, acessar logs, alterar prompts e consultar resultados. Segurança de IA é segurança da aplicação toda.

### Conformidade e evidencias

Em contextos regulados, a empresa precisa mostrar como protege dados, rastreia acessos e reage a incidentes. CloudTrail, classificação de dados, trilha de mudanças e separação de ambientes ajudam a produzir essa evidência.

## Exemplo prático

### Assistente com documentos sensiveis

Uma equipe jurídica quer usar documentos internos em um assistente. Além da parte generativa, a arquitetura precisa isolar buckets, aplicar IAM mínimo necessário, criptografia com KMS e trilha de auditoria de acesso e alteração.

## Raciocínio arquitetural

### Seguranca de IA e composicao de controles

A resposta correta raramente é um único serviço. O desenho seguro geralmente combina IAM, KMS, CloudTrail, Secrets Manager, S3 privado, política de rede e controles específicos do serviço de IA.

### Conformidade depende de rastreabilidade

Quando a pergunta fala em auditoria, investigação ou evidência de conformidade, pense em logs, trilhas, versionamento e segregação de responsabilidades. Conformidade não nasce apenas da criptografia.

## Boas práticas

- Aplique princípio do menor privilégio para modelos, dados e integrações.
- Criptografe dados sensíveis e segredos com serviços gerenciados adequados.
- Use CloudTrail para trilha de auditoria de ações relevantes.
- Separe ambientes e permissões de desenvolvimento, homologação e produção.
- Revise periodicamente quem pode acessar documentos e bases usadas pela IA.

## Dicas de prova

- IAM é a resposta forte quando o problema é autorização.
- KMS aparece quando o requisito fala em chaves e criptografia gerenciada.
- Secrets Manager protege credenciais e tokens da aplicação.
- CloudTrail ajuda quando a pergunta fala em auditoria ou investigação.

## Armadilhas comuns

- Achar que Guardrails resolvem toda a segurança da solução.
- Guardar segredos em variável de ambiente sem governança adequada.
- Misturar ambiente de teste e produção com os mesmos dados sensíveis.
- Ignorar trilha de auditoria em aplicações com IA.

## Resumo para revisão

- Segurança de IA é segurança de dados, identidade, integração e operação.
- Shared responsibility continua valendo em Bedrock e SageMaker AI.
- IAM, KMS, Secrets Manager e CloudTrail são peças frequentes no exame.
- Conformidade exige evidência e rastreabilidade.
- Aplicação generativa segura vai além do modelo.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 10 — IA Generativa na AWS](../10-IA-Generativa-na-AWS/README.md).
- Continue para [Módulo 12 — Casos de Uso e Arquiteturas](../12-Casos-de-Uso-e-Arquiteturas/README.md).

