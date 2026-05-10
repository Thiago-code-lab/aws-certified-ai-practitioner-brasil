# Casos de Uso — Módulo 03: Fundamentos de Machine Learning

## Caso 1 — Score de risco

**Cenário:** Uma fintech quer prever probabilidade de inadimplência com base em histórico rotulado.

**Arquitetura sugerida:** ML supervisionado com pipeline de dados no S3 e ciclo de treino no SageMaker AI.

**Por que essa escolha faz sentido:** Existe alvo conhecido e necessidade de prever um evento futuro.

**Armadilha de prova associada:** Escolher clustering apenas porque há muitos clientes.

## Caso 2 — Mapeamento de perfis

**Cenário:** Um e-commerce quer descobrir segmentos naturais de clientes antes de lançar campanhas.

**Arquitetura sugerida:** Aprendizado não supervisionado para agrupar perfis de comportamento.

**Por que essa escolha faz sentido:** O objetivo não é prever uma classe conhecida, mas revelar estrutura nos dados.

**Armadilha de prova associada:** Insistir em classificação sem rótulo disponível.
