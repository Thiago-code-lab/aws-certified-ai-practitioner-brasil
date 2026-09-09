# Cheatsheet — Módulo 12: Casos de Uso e Arquiteturas

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Textract | Extrai texto, tabelas e formulários. | Não é a melhor primeira resposta para gerar resumo livre. |
| Comprehend | NLP gerenciado para tarefas comuns. | Não confundir com chatbot generativo. |
| Rekognition | Visão computacional gerenciada. | Não usar para OCR documental completo quando Textract é mais apropriado. |
| Bedrock | Geração e interação flexível com FM. | Não usar como martelo universal. |

## Regras práticas

- Leia o verbo principal do caso: extrair, classificar, gerar, responder, moderar, recomendar.
- Prefira o serviço mais especializado quando ele atende ao requisito diretamente.
- Combine serviços em pipeline quando o caso pede mais de uma capacidade.
- Avalie custo, latência, governança e manutenção do desenho.

## Gatilhos de memorização

- Extrair -> Textract. Ver imagem -> Rekognition. Analisar texto -> Comprehend. Gerar/responder -> Bedrock.
- Requisito dominante decide o serviço principal.

---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Aprofundamento opcional: pipelines e fundamentos de dados na AWS aparecem no curso [Engenharia de Dados na AWS: do Zero aos Projetos Reais](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
