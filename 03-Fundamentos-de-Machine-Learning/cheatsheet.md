# Cheatsheet — Módulo 03: Fundamentos de Machine Learning

> Revisão rápida pensada para a reta final do exame AWS Certified AI Practitioner.

## Visão rápida

| Tópico | O que lembrar | Armadilha de prova |
| --- | --- | --- |
| Classificação | Prevê uma categoria, como fraude ou não fraude. | Não confundir com cluster. |
| Regressão | Prevê valor numérico contínuo. | Não é para rótulo de classe. |
| Clustering | Agrupa padrões sem rótulo. | Não responde diretamente um alvo conhecido. |
| Ground Truth | Rotulagem de dados para treino supervisionado. | Não é serviço principal de inferência. |

## Regras práticas

- Confirme se o problema é classificação, regressão ou agrupamento antes de escolher a técnica.
- Separe treino, validação e teste para medir generalização.
- Cuide da qualidade de rótulos e da consistência do dataset.
- Escolha métricas coerentes com o negócio, e não apenas acurácia.

## Gatilhos de memorização

- Rótulo presente? pense em supervisionado.
- Sem resposta pronta? pense em descoberta de padrão.
- Treino bom não basta; teste é o filtro de realidade.
