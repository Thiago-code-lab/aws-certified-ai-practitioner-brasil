# Cheatsheet — Módulo 10: IA Generativa na AWS

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| API Gateway | Exposição de API para app e integrações. | Não deixar o cliente chamar o modelo diretamente sem controle. |
| Lambda | Orquestração leve e serverless. | Avaliar timeout e payload. |
| CloudWatch | Logs e métricas da aplicação. | Sem observabilidade, a operação fica cega. |
| S3 | Base documental e artefatos. | Sem curadoria e permissões, vira risco. |

## Regras práticas

- Isole a chamada ao modelo em uma camada bem definida da aplicação.
- Registre logs, métricas de latência e falhas desde o primeiro deploy.
- Use API Gateway e Lambda quando a carga e o perfil favorecem serverless.
- Controle o que vai para o prompt e o que volta do modelo.

## Gatilhos de memorização

- App GenAI = interface + API + contexto + modelo + logs.
- Serverless acelera; fallback protege.
- Latência desejada define o estilo de integração.
