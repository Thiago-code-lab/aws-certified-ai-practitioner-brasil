# Módulo 03 — Fundamentos de Machine Learning

O AIF-C01 não exige matemática pesada, mas exige que você entenda como ML aprende com dados e por que qualidade de dados, rótulos e avaliação importam.

## Objetivo

Consolidar os pilares de ML que aparecem na prova: aprendizado supervisionado, não supervisionado, overfitting, datasets, métricas e escolha entre serviço pronto e modelo customizado.

## Onde este tema aparece no AIF-C01

- Diferenciar classificação, regressão e clustering.
- Entender conjuntos de treino, validação e teste.
- Relacionar preparo de dados com qualidade do resultado.

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
| Amazon SageMaker AI | Treinamento, experimentação e implantação de modelos customizados. | Aparece quando a empresa precisa construir ML próprio. |
| Amazon SageMaker Canvas | Experiência low-code/no-code para usuários de negócio. | Mostra a possibilidade de ML sem codificação pesada. |
| Amazon SageMaker Ground Truth | Rotulagem de dados para treinamento supervisionado. | Pode aparecer em perguntas sobre qualidade de dataset. |
| Amazon S3 | Data lake comum para datasets de treino e inferência. | Componente frequente em arquiteturas de ML. |

## Conceitos essenciais

### Supervisionado, não supervisionado e por reforço

Aprendizado supervisionado usa exemplos com rótulo para prever classe ou valor. Aprendizado não supervisionado encontra padrões sem rótulo, como agrupamentos. Aprendizado por reforço otimiza decisões com base em recompensas. Para o AIF-C01, supervisionado e não supervisionado são os mais recorrentes.

### Datasets de treino, validação e teste

Treino ajusta o modelo. Validação ajuda a escolher parâmetros e comparar versões. Teste mede desempenho em dados não vistos. Em prova, a ideia central é evitar ilusão de qualidade: avaliar no mesmo dado usado para treinar pode mascarar falhas.

### Overfitting e underfitting

Overfitting acontece quando o modelo aprende detalhes demais do treino e generaliza mal. Underfitting ocorre quando ele é simples demais para capturar o padrão. Ambos aparecem como riscos ligados a dados, complexidade do modelo e forma de avaliação.

## Exemplo prático

### Previsão de cancelamento vs segmentação de clientes

Prever cancelamento com histórico rotulado é um caso de classificação supervisionada. Já dividir clientes em grupos com comportamentos semelhantes sem rótulo prévio é clustering, portanto não supervisionado.

```
Dados historicos -> preparo -> treino supervisionado -> score de churn
Dados sem rotulo -> clustering -> segmentos de clientes
```

## Raciocínio arquitetural

### Escolha o tipo de aprendizado a partir do dado disponivel

Se existem exemplos passados com resposta correta, a tendência é supervisionado. Se o objetivo é encontrar padrões escondidos sem resposta pronta, não supervisionado ganha força. O exame frequentemente descreve isso em linguagem de negócio, e não com nomes acadêmicos.

### Dados de qualidade superam complexidade mal direcionada

Em arquiteturas reais, preparar bem os dados costuma ter impacto maior que trocar o modelo por outro mais sofisticado sem necessidade. No contexto AWS, isso se conecta a S3, pipelines de dados e rotulagem adequada.

## Boas práticas

- Confirme se o problema é classificação, regressão ou agrupamento antes de escolher a técnica.
- Separe treino, validação e teste para medir generalização.
- Cuide da qualidade de rótulos e da consistência do dataset.
- Escolha métricas coerentes com o negócio, e não apenas acurácia.
- Mantenha rastreabilidade entre dado usado, modelo treinado e resultado obtido.

## Dicas de prova

- Classificação prevê classe; regressão prevê valor contínuo; clustering agrupa sem rótulo.
- Ground Truth aparece quando o tema é rotulagem supervisionada.
- Acurácia alta sozinha pode enganar em datasets desbalanceados.
- ML customizado tende a apontar para SageMaker AI.

## Armadilhas comuns

- Confundir clustering com classificação.
- Assumir que dados históricos sem rótulo permitem previsão supervisionada imediatamente.
- Interpretar desempenho em treino como prova de generalização.
- Ignorar que dados ruins produzem modelos ruins.

## Resumo para revisão

- Supervisionado aprende com rótulo; não supervisionado encontra estrutura sem rótulo.
- Treino, validação e teste existem para evitar autoengano.
- Overfitting e underfitting são extremos de generalização.
- Ground Truth ajuda na etapa de rotulagem.
- SageMaker AI é o serviço mais associado a ML customizado na AWS.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 02 — Fundamentos de IA Generativa](../02-Fundamentos-de-IA-Generativa/README.md).
- Continue para [Módulo 04 — Modelos Fundacionais e LLMs](../04-Modelos-Fundacionais-e-LLMs/README.md).

