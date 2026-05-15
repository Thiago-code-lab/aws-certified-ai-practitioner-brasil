# Módulo 16 — Simulados e Questões

Este módulo concentra o treino final da certificação, com banco comentado de questões, simulados progressivos, diagnóstico por domínio, reta final e caderno de erros.

> Formato oficial do exame conferido no guia da AWS em **10 de maio de 2026**: **65 questões totais**, sendo **50 pontuadas** e **15 não pontuadas**, com **90 minutos** de prova e **score mínimo 700/1000**.

## Onde está cada conteúdo

- [`README.md`](./README.md): visão geral, estratégia de uso, formato oficial e plano de execução.
- [`questoes.md`](./questoes.md): **13 questões de aquecimento**, incluindo múltipla escolha, múltiplas respostas, ordenação e associação.
- [`simulado-completo-1.md`](./simulado-completo-1.md): **20 questões comentadas** com progressão de dificuldade.
- [`simulado-completo-2.md`](./simulado-completo-2.md): **20 questões comentadas** com foco maior em cenário, arquitetura e decisão de serviço.
- [`mini-simulado-por-dominio.md`](./mini-simulado-por-dominio.md): **15 questões** organizadas por domínio para diagnóstico rápido.
- [`reta-final-aif-c01.md`](./reta-final-aif-c01.md): planos práticos de 14 dias e 7 dias antes da prova.
- [`caderno-de-erros.md`](./caderno-de-erros.md): modelo para revisão ativa após cada tentativa.
- [`cheatsheet.md`](./cheatsheet.md): sinais rápidos de prova, heurísticas de leitura e armadilhas frequentes.
- [`flashcards.md`](./flashcards.md): revisão espaçada com os gatilhos conceituais mais cobrados.
- [`links.md`](./links.md): curadoria oficial para confirmar escopo, serviços e detalhes do exame.

## Banco disponível neste módulo

| Arquivo | Volume | Objetivo |
| --- | --- | --- |
| [Questões de aquecimento](./questoes.md) | 6 | Aquecer leitura de enunciado e tipos de questão |
| [Simulado completo 1](./simulado-completo-1.md) | 8 | Treino progressivo e fixação dos fundamentos |
| [Simulado completo 2](./simulado-completo-2.md) | 8 | Treino interpretativo e arquitetural |
| [Mini-simulado por domínio](./mini-simulado-por-dominio.md) | 8 | Diagnóstico pontual por domínio |

**Total neste módulo: 30 questões comentadas.**

## Formato oficial do exame AIF-C01

- 65 questões no total.
- 50 questões pontuadas.
- 15 questões não pontuadas.
- 90 minutos de prova.
- Pontuação de 100 a 1000, com aprovação em 700.
- Sem penalidade por chute.
- Tipos oficiais: múltipla escolha, múltiplas respostas, ordenação e associação.

## Como interpretar a distribuição por domínio

| Domínio | Peso oficial | Estimativa útil sobre 50 questões pontuadas | Onde treinar aqui |
| --- | --- | --- | --- |
| Fundamentos de IA e ML | 20% | cerca de 10 | `questoes.md`, `simulado-completo-1.md`, `mini-simulado-por-dominio.md` |
| Fundamentos de IA generativa | 24% | cerca de 12 | `questoes.md`, `simulado-completo-1.md`, `simulado-completo-2.md` |
| Aplicações de foundation models | 28% | cerca de 14 | `simulado-completo-1.md`, `simulado-completo-2.md`, `mini-simulado-por-dominio.md` |
| IA responsável | 14% | cerca de 7 | `simulado-completo-2.md`, `mini-simulado-por-dominio.md` |
| Segurança, conformidade e governança | 14% | cerca de 7 | `simulado-completo-2.md`, `mini-simulado-por-dominio.md` |

> A mistura real pode variar porque as 15 questões não pontuadas não são identificadas pela AWS.

## Como montar um espelho de 65 questões

Se você quiser reproduzir o **volume oficial** da certificação em uma sessão única, faça:

1. [`simulado-completo-1.md`](./simulado-completo-1.md) — 20 questões
2. [`simulado-completo-2.md`](./simulado-completo-2.md) — 20 questões
3. [`mini-simulado-por-dominio.md`](./mini-simulado-por-dominio.md) — 15 questões
4. [`questoes.md`](./questoes.md) — questões **1 a 10**

Total: **65 questões**.

### Configuração recomendada para essa sessão

- Reserve **90 minutos**.
- Não consulte material no meio do simulado.
- Marque perguntas duvidosas e siga adiante.
- Só abra as explicações depois de terminar.
- Registre erros no [`caderno-de-erros.md`](./caderno-de-erros.md).

## Estratégia recomendada de estudo

1. Faça o bloco de [`questoes.md`](./questoes.md) para aquecer vocabulário, tipos de pergunta e leitura de contexto.
2. Resolva o [`simulado-completo-1.md`](./simulado-completo-1.md) em tempo controlado.
3. Preencha o [`caderno-de-erros.md`](./caderno-de-erros.md) antes de revisar o gabarito.
4. Faça o [`mini-simulado-por-dominio.md`](./mini-simulado-por-dominio.md) apenas nos domínios com mais dificuldade.
5. Feche com o [`simulado-completo-2.md`](./simulado-completo-2.md), a [`cheatsheet.md`](./cheatsheet.md) e a [`reta-final-aif-c01.md`](./reta-final-aif-c01.md).

## Faixas práticas de prontidão

> Estas faixas são **heurísticas de estudo**, não equivalências oficiais do score escalado da AWS.

| Resultado bruto nos simulados | Leitura prática |
| --- | --- |
| 85% ou mais | Prontidão forte para a prova; foque em consistência e revisão fina |
| 75% a 84% | Boa base; ainda vale revisar serviço certo para caso certo e armadilhas de governança |
| 65% a 74% | Zona de risco; volte aos módulos 04, 05, 07, 11, 13 e 15 |
| Abaixo de 65% | Ainda não é hora de confiar só em simulados; recupere teoria e depois repita o treino |

## Dicas finais

- Leia o caso de uso inteiro antes de olhar as alternativas.
- Priorize a opção mais gerenciada quando duas alternativas parecem equivalentes.
- Diferencie claramente Bedrock, SageMaker AI e serviços de IA especializados.
- Quando a pergunta mencionar segurança ou governança, procure IAM, KMS, CloudTrail, Secrets Manager, Macie, Guardrails e revisão humana.
- Revise a página oficial de **serviços em escopo** antes da prova, porque a AWS pode atualizar essa lista ao longo do tempo.

## Navegação complementar

- Para revisar fundamentos de cloud antes dos simulados, veja: https://github.com/Thiago-code-lab/aws-certified-cloud-practitioner-brasil
- Estudos complementares de arquitetura podem ser aprofundados em: https://github.com/Thiago-code-lab/aws-certified-solutions-architect-associate-brasil
- Continue a jornada AWS com foco em contexto arquitetural e governança entre certificações.
