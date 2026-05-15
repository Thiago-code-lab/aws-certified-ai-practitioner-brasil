# Casos de Uso — Módulo 09: Engenharia de Prompts

## Caso 1 — Triagem em JSON

**Cenário:** Uma API precisa classificar tickets e devolver prioridade, categoria e ação em JSON.

**Arquitetura sugerida:** Prompt com schema explícito, poucos exemplos e validação de resposta na aplicação.

**Por que essa escolha faz sentido:** A integração depende mais de previsibilidade estrutural do que de criatividade.

**Armadilha de prova associada:** Pedir texto livre e tentar corrigir depois.

## Caso 2 — Assistente com tom institucional

**Cenário:** A empresa quer que o assistente responda com tom profissional e conciso.

**Arquitetura sugerida:** Prompt de papel, exemplos few-shot e limites claros de estilo.

**Por que essa escolha faz sentido:** O comportamento desejado pode ser fortemente influenciado por instrução e exemplos.

**Armadilha de prova associada:** Ir direto para fine-tuning sem testar engenharia de prompt.
