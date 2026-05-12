# Mini-Simulado por Domínio — Edição Curada

## Questão 17

**Pergunta:** Em uma questão que contrasta RAG e fine-tuning para base documental dinâmica, a melhor escolha tende a ser:

- A) Fine-tuning recorrente
- B) RAG com base vetorial
- C) Sem fonte de contexto
- D) Prompt único fixo

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
RAG favorece atualização contínua de conhecimento sem retrain frequente.

**Por que a alternativa A está errada:**
Aumenta custo e ciclo de atualização sem necessidade.

</details>

## Questão 18

**Pergunta:** Qual serviço combina melhor com análise de sentimento e entidades em texto?

- A) Comprehend
- B) Rekognition
- C) Textract
- D) Polly

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Comprehend é o serviço de NLP gerenciado da AWS para tarefas de entendimento textual.

**Por que a alternativa B está errada:**
Rekognition é focado em imagem/vídeo.

</details>

## Questão 19

**Pergunta:** Para expor segredo de API ao app com menor risco, você deve:

- A) Embutir no código
- B) Armazenar em Secrets Manager
- C) Salvar em variável local sem proteção
- D) Publicar no S3 público

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Secrets Manager centraliza controle, rotação e acesso seguro a segredos.

**Por que a alternativa A está errada:**
Hardcode de segredo compromete segurança e governança.

</details>

## Questão 20

**Pergunta:** Qual prática reduz alucinação em assistentes corporativos?

- A) Grounding com fontes confiáveis
- B) Remover contexto documental
- C) Desabilitar validação humana sempre
- D) Ignorar avaliação de saída

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Grounding em fontes verificáveis melhora factualidade e consistência.

**Por que a alternativa B está errada:**
Sem contexto, o modelo tende a responder com menor precisão.

</details>

## Questão 21

**Pergunta:** Para detectar dados sensíveis em S3 de forma gerenciada, qual serviço é esperado?

- A) Macie
- B) DynamoDB
- C) ECR
- D) SNS

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Macie automatiza descoberta/classificação de dados sensíveis em buckets.

**Por que a alternativa B está errada:**
DynamoDB é banco NoSQL, não scanner de PII em S3.

</details>

## Questão 22

**Pergunta:** Em responsabilidade de IA, o que fortalece accountability?

- A) Logs e critérios de revisão humana
- B) Exclusão de auditoria
- C) Acesso irrestrito por conveniência
- D) Sem versionamento de prompt

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Rastreabilidade e governança de decisão são pilares de responsible AI.

**Por que a alternativa C está errada:**
Acesso irrestrito viola princípio de menor privilégio.

</details>

## Questão 23

**Pergunta:** Para caso de uso de OCR em documentos financeiros, qual opção tende a ser mais direta?

- A) Textract
- B) Bedrock Guardrails
- C) Neptune
- D) CloudWatch Logs

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Textract resolve extração de campos e tabelas de documentos digitalizados.

**Por que a alternativa B está errada:**
Guardrails controla conteúdo gerado, não OCR.

</details>

## Questão 24

**Pergunta:** Em prova de AI Practitioner, quando duas opções funcionam, a melhor costuma ser:

- A) A mais gerenciada e aderente ao enunciado
- B) A mais complexa tecnicamente
- C) A mais customizada sem necessidade
- D) A de maior custo

<details><summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
A AWS tende a valorizar simplicidade operacional e ajuste claro ao requisito.

**Por que a alternativa B está errada:**
Complexidade extra não agrega quando o problema pede solução prática e gerenciada.

</details>
