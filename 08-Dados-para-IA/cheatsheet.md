# Cheatsheet — Módulo 08: Dados para IA

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| S3 | Origem comum de dados e documentos. | Não é governança completa sozinho. |
| Chunking | Divide documentos em partes úteis para retrieval. | Chunks ruins reduzem precisão do RAG. |
| Macie | Descobre dados sensíveis em S3. | Não substitui políticas de acesso. |
| Lake Formation | Governança em data lake. | Não é serviço de geração de IA. |

## Regras práticas

- Versione documentos e datasets relevantes.
- Remova ou isole conteúdo obsoleto, duplicado ou sensível demais para o caso de uso.
- Use metadados para facilitar filtros e governança.
- Classifique dados antes de conectá-los a aplicações de IA.

## Gatilhos de memorização

- Base boa gera resposta melhor; base ruim gera erro mais rápido.
- Documento sem curadoria vira contexto ruim.
- S3 armazena; metadado orienta; governança protege.
