# Cheatsheet — Módulo 11: Segurança e Conformidade em IA

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| IAM | Menor privilégio e controle de acesso. | Não substituir por filtros de conteúdo. |
| KMS | Gestão de chaves e criptografia. | Criptografia não substitui autorização. |
| Secrets Manager | Armazena segredos com rotação e controle. | Não embutir credenciais no código. |
| CloudTrail | Trilha de auditoria. | Sem log, não há evidência. |

## Regras práticas

- Aplique princípio do menor privilégio para modelos, dados e integrações.
- Criptografe dados sensíveis e segredos com serviços gerenciados adequados.
- Use CloudTrail para trilha de auditoria de ações relevantes.
- Separe ambientes e permissões de desenvolvimento, homologação e produção.

## Gatilhos de memorização

- Modelo seguro = dados seguros + acesso seguro + operação auditável.
- Guardrails ajudam no conteúdo; IAM ajuda em quem pode fazer o quê.

