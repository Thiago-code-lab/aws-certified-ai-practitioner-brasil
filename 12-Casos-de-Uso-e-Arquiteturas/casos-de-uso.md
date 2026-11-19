# Casos de Uso — Módulo 12: Casos de Uso e Arquiteturas

## Caso 1 — Análise de contratos

**Cenário:** Um time jurídico precisa extrair campos e gerar resumo executivo.

**Arquitetura sugerida:** Textract para OCR estruturado e Bedrock para resumo textual contextualizado.

**Por que essa escolha faz sentido:** Cada parte do problema usa o serviço mais adequado.

**Armadilha de prova associada:** Escolher um único serviço para todas as etapas sem necessidade.

## Caso 2 — Moderação de imagens

**Cenário:** Uma plataforma quer bloquear conteúdo visual impróprio enviado por usuários.

**Arquitetura sugerida:** Rekognition para análise de imagem e moderação.

**Por que essa escolha faz sentido:** É um caso de visão computacional gerenciada, não de chatbot ou LLM textual.

**Armadilha de prova associada:** Usar Bedrock textual para um problema visual direto.

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---
