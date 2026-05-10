# Módulo 15 — Boas Práticas e Otimização

Depois de entender serviços e arquiteturas, falta aprender a operá-los bem. O exame cobra muito a ideia de eficiência: atingir objetivo com menor custo, menor risco e menor complexidade desnecessária.

## Objetivo

Revisar práticas de otimização para aplicações de IA na AWS, com foco em custo, latência, avaliação, observabilidade, governança e escolha consciente de modelos.

## Onde este tema aparece no AIF-C01

- Controlar custo de inferência e contexto.
- Entender escolha de modelo, cache, batch e fallback.
- Operar IA com avaliação contínua e monitoramento.

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
| Amazon CloudWatch | Observabilidade de uso, latência e falhas. | Base da operação e troubleshooting. |
| AWS Budgets | Alertas de custo e consumo. | Importante para governança financeira. |
| AWS Cost Explorer | Análise de gasto por serviço e padrão de consumo. | Ajuda em otimização financeira. |
| Amazon Bedrock / SageMaker AI | Plataformas onde as decisões de modelo e inferência impactam custo. | Aparecem em comparações de eficiência. |

## Conceitos essenciais

### Custo de IA não vem só do modelo

O custo total envolve volume de chamadas, tamanho do prompt, tamanho da resposta, frequência, armazenamento, pipelines de dados e componentes de integração. Em prova, o erro comum é olhar apenas o serviço principal.

### Latência, qualidade e custo como trade-off

Modelos mais poderosos podem custar mais e responder mais lentamente. Modelos menores ou respostas mais curtas podem reduzir custo e melhorar tempo de resposta. A melhor escolha depende da necessidade real do caso de uso.

### Avaliação contínua e observabilidade

Aplicações de IA precisam ser medidas. Não basta dizer que funcionam. Monitorar latência, falhas, custo, satisfação do usuário e padrões de erro ajuda a melhorar qualidade e evitar surpresas em produção.

## Exemplo prático

### Assistente de FAQ com custo controlado

Uma empresa pode usar contexto enxuto, prompts objetivos, respostas limitadas, cache de perguntas frequentes e fallback para busca simples quando a pergunta não exige geração rica. Isso reduz custo e melhora previsibilidade.

## Raciocínio arquitetural

### Use o menor modelo que resolva o problema

A certificação tende a valorizar escolhas eficientes. Se um modelo menor atende à qualidade requerida, ele pode ser melhor opção que um modelo maior e mais caro. Isso vale especialmente para tarefas repetitivas e padronizadas.

### Cache, batch e selecao de contexto economizam muito

Nem toda pergunta precisa gerar tudo de novo. Perguntas repetidas podem ser servidas por cache. Processos off-line podem rodar em lote. E contexto excessivo aumenta custo sem necessariamente aumentar qualidade.

## Boas práticas

- Escolha o menor modelo que atenda ao requisito.
- Limite contexto e tamanho da resposta ao necessário.
- Use cache para perguntas repetidas e respostas estáveis.
- Monitore custo, latência, falhas e taxa de reutilização.
- Crie conjunto de avaliação simples para comparar versões de prompt e arquitetura.

## Dicas de prova

- Custo de IA também vem do volume de tokens e chamadas.
- Batch pode ser melhor que tempo real quando o usuário não precisa esperar.
- Cache e grounding seletivo são alavancas clássicas de otimização.
- CloudWatch, Budgets e Cost Explorer apoiam a operação financeira e técnica.

## Armadilhas comuns

- Escolher sempre o modelo mais avançado por reflexo.
- Mandar contexto excessivo sem medir retorno de qualidade.
- Operar sem métricas mínimas de custo e latência.
- Ignorar avaliação objetiva antes de mudar prompts ou arquitetura.

## Resumo para revisão

- Otimizar IA é equilibrar custo, latência e qualidade.
- Modelo maior nem sempre é melhor decisão.
- Cache, batch e contexto enxuto economizam muito.
- Observabilidade e avaliação contínua fazem parte da maturidade operacional.
- A prova valoriza eficiência com serviços gerenciados.

## Próximos passos

- Resolva as [questões do módulo](./questoes.md) antes de seguir.
- Revise os [flashcards](./flashcards.md) como revisão espaçada.
- Consulte o [lab](./lab.md) para consolidar a parte prática.
- Revisão complementar: [Módulo 14 — Integração com Aplicações](../14-Integracao-com-Aplicacoes/README.md).
- Continue para [Módulo 16 — Simulados e Questões](../16-Simulados-e-Questoes/README.md).

