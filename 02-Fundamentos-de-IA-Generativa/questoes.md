# Questões — Módulo 02: Fundamentos de IA Generativa

> **Nível predominante:** Iniciante a intermediário
> **Objetivo:** treinar vocabulário de prova e raciocínio arquitetural em contexto AWS.

**1.** Uma empresa quer respostas sobre manuais internos atualizados diariamente. Qual técnica reduz mais diretamente o risco de respostas desatualizadas?

- A) Aumentar somente a temperatura do modelo
- B) Usar grounding/RAG com documentos atuais
- C) Substituir S3 por instâncias EC2
- D) Desabilitar logs da aplicação

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Quando o problema é atualização e fidelidade ao conteúdo interno, grounding/RAG é o mecanismo natural para inserir contexto recente na resposta.

**Por que as demais estão incorretas:**
- **A** — Temperatura afeta variação, não atualização factual.
- **C** — Trocar armazenamento não resolve o problema sem mecanismo de recuperação.
- **D** — Desabilitar logs reduz observabilidade e piora a governança.

</details>

---

**2.** Qual afirmação descreve melhor prompt engineering?

- A) É o processo de treinar novamente o modelo com dados da empresa
- B) É a prática de estruturar instruções, contexto e formato para orientar a resposta
- C) É a criação de uma VPC dedicada para o modelo
- D) É a técnica de desativar parâmetros de segurança

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Engenharia de prompts trabalha o texto da instrução, o contexto e as restrições esperadas para conduzir a geração.

**Por que as demais estão incorretas:**
- **A** — Treinar novamente é outra etapa, não prompt engineering.
- **C** — VPC é recurso de rede e não define a técnica de prompt.
- **D** — Desativar segurança não é prática recomendada nem definição do termo.

</details>

---

**3.** Em uma tarefa de geração de resposta padronizada para e-mail corporativo, qual escolha tende a ser mais adequada?

- A) Temperatura alta para maximizar criatividade
- B) Temperatura baixa e formato de saída explícito
- C) Sem contexto, para o modelo improvisar
- D) Sem logs, para reduzir custo

<details><summary>Resposta e explicações</summary>

**Resposta correta: B**

Em fluxos operacionais e padronizados, o objetivo é consistência. Temperatura baixa e instrução clara ajudam nisso.

**Por que as demais estão incorretas:**
- **A** — Criatividade maior aumenta variação e tende a piorar padronização.
- **C** — Falta de contexto reduz confiabilidade.
- **D** — Logs são importantes para governança e depuração.

</details>

---

