# Casos de Uso — Módulo 15: Boas Práticas e Otimização

## Caso 1 — FAQ repetitivo

**Cenário:** O assistente responde muitas perguntas iguais todos os dias.

**Arquitetura sugerida:** Cache para respostas estáveis e revisão da necessidade do modelo mais caro.

**Por que essa escolha faz sentido:** Nem toda resposta precisa ser gerada do zero a cada chamada.

**Armadilha de prova associada:** Escalar apenas aumentando capacidade e custo.

## Caso 2 — Relatorio noturno

**Cenário:** A área de operações gera um resumo diário para gestores.

**Arquitetura sugerida:** Fluxo batch com processamento fora do horário crítico.

**Por que essa escolha faz sentido:** A latência online não é requisito; custo e previsibilidade importam mais.

**Armadilha de prova associada:** Insistir em tempo real sem valor para o negócio.


---

## ☁️ Acompanhe a CloudStudy

Estamos construindo uma plataforma para ajudar brasileiros a estudarem AWS de forma mais prática, organizada e acessível.

Siga a CloudStudy para acompanhar novos materiais, atualizações e conteúdos sobre certificações AWS:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> Aprofundamento opcional: pipelines e fundamentos de dados na AWS aparecem no curso [Engenharia de Dados na AWS: do Zero aos Projetos Reais](https://www.udemy.com/course/engenharia-de-dados-na-aws-do-zero-aos-projetos-reais/?referralCode=E28670B9116BA68E08A9).
