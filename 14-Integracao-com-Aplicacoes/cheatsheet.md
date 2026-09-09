# Cheatsheet — Módulo 14: Integração com Aplicações

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| API Gateway + Lambda | Exposição controlada de IA via API. | Não expor chamada direta ao modelo sem mediação. |
| SQS | Fila para desacoplamento e processamento em background. | Não usar quando a latência imediata é requisito central. |
| EventBridge | Integração orientada a eventos. | Não confundir com fila de trabalho. |
| Retry | Importante em falhas transitórias. | Sem cuidado pode duplicar efeito em processos não idempotentes. |

## Regras práticas

- Use síncrono apenas quando a experiência realmente exigir resposta imediata.
- Desacople tarefas longas com eventos e filas.
- Padronize contratos de API e formatos de resposta.
- Aplique retries e tratamento de exceção em pontos previsíveis.

## Gatilhos de memorização

- Tempo real? síncrono. Processo longo? fila ou evento.
- Camada de app organiza e protege a IA.


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
