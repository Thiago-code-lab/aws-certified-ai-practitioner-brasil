# Questões — Módulo 09: Engenharia de Prompts

> **Nível predominante:** Intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma equipe quer que um modelo retorne apenas JSON válido com campos fixos para integração. Qual prática é mais adequada?

- A) Especificar explicitamente o schema e o formato esperado no prompt
- B) Aumentar a criatividade do modelo ao máximo
- C) Remover todas as restrições do prompt
- D) Desligar logs da API

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Saída estruturada precisa ser pedida explicitamente para aumentar previsibilidade e facilitar integração.

**Por que as demais estão incorretas:**
- **B** — Criatividade maior tende a aumentar variação, não estrutura.
- **C** — Sem restrições a saída fica menos previsível.
- **D** — Logs ajudam a observar erros e não atrapalham a estrutura.

</details>

---

**2.** Qual afirmação descreve melhor few-shot prompting?

- A) É um tipo de criptografia para prompts
- B) É o uso de exemplos para orientar a saída do modelo
- C) É a criação de uma base vetorial
- D) É o desligamento da moderação do modelo

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Few-shot usa alguns exemplos de referência para conduzir estilo, formato ou tipo de resposta.

**Por que as demais estão incorretas:**
- **A** — Não tem relação com criptografia.
- **C** — Base vetorial é outro componente arquitetural.
- **D** — Não envolve desativação de segurança.

</details>

---

**3.** Em qual cenário prompt engineering sozinho tende a ser insuficiente?

- A) Quando o caso depende de documentos internos atualizados
- B) Quando a tarefa é resumir um texto fornecido no próprio prompt
- C) Quando o time quer formatar a saída em tópicos
- D) Quando o usuário quer resposta curta em português

<details><summary>Resposta e explicações</summary>

**Resposta correta: A**

Quando o conhecimento vem de documentos internos atualizados, a aplicação tende a precisar de grounding ou RAG além do prompt.

**Por que as demais estão incorretas:**
- **B** — Resumo do texto presente pode ser feito apenas com bom prompt.
- **C** — Formato em tópicos é tratável no próprio prompt.
- **D** — Idioma e concisão também podem ser orientados via prompt.

</details>

---
