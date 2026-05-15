# Questões de Aquecimento — AIF-C01

## Questão 01

**Pergunta:** Em um cenário com base documental que muda semanalmente, qual abordagem é mais adequada para respostas atualizadas?

- A) RAG com recuperação de contexto
- B) Fine-tuning a cada atualização
- C) Remoção de logs de auditoria
- D) Substituir IAM por Guardrails

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
RAG separa conhecimento dinâmico do treinamento do modelo, reduzindo custo e tempo de atualização.

**Por que a alternativa B está errada:**
Fine-tuning recorrente para atualização documental tende a elevar custo e complexidade operacional.

</details>

## Questão 02

**Pergunta:** Qual serviço AWS é mais indicado para aplicar políticas de conteúdo em apps GenAI com Bedrock?

- A) AWS KMS
- B) Amazon Bedrock Guardrails
- C) Amazon Route 53
- D) Amazon CloudFront

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** B

**Explicação:**
Guardrails controla temas e padrões de conteúdo em entradas e saídas de aplicações generativas.

**Por que a alternativa A está errada:**
KMS trata gestão de chaves e criptografia, não política semântica de conteúdo.

</details>

## Questão 03

**Pergunta:** Para identificar dados sensíveis em buckets S3, qual serviço é o mais aderente?

- A) Amazon Macie
- B) Amazon Rekognition
- C) Amazon Polly
- D) Amazon SQS

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Amazon Macie foi desenhado para descoberta e classificação de dados sensíveis no S3.

**Por que a alternativa B está errada:**
Rekognition é voltado para visão computacional, não classificação de PII em armazenamento.

</details>

## Questão 04

**Pergunta:** Em inferência com tráfego imprevisível, qual decisão tende a reduzir custo ocioso?

- A) Manter capacidade máxima fixa
- B) Usar modelo maior por padrão
- C) Inferência elástica sob demanda
- D) Aumentar contexto sempre

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** C

**Explicação:**
Capacidade elástica evita custo parado quando a carga é intermitente.

**Por que a alternativa A está errada:**
Capacidade fixa máxima aumenta gasto em períodos de baixa utilização.

</details>

## Questão 05

**Pergunta:** Qual par de serviços atende melhor à proteção de segredos e criptografia de dados?

- A) Secrets Manager + AWS KMS
- B) CloudFront + Route 53
- C) Textract + Comprehend
- D) Budgets + Cost Explorer

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Secrets Manager protege credenciais; KMS gerencia chaves para criptografia de dados.

**Por que a alternativa B está errada:**
CloudFront e Route 53 resolvem entrega e DNS, não gestão de segredo e chave.

</details>

## Questão 06

**Pergunta:** Em IA responsável para decisões sensíveis, qual prática é prioritária?

- A) Revisão humana em decisões críticas
- B) Automação irrestrita
- C) Desativar trilhas de auditoria
- D) Aumentar temperatura para diversificar respostas

<details>
<summary><strong>Ver resposta</strong></summary>

✅ **Resposta correta:** A

**Explicação:**
Human-in-the-loop reduz risco em cenários de alto impacto e melhora governança.

**Por que a alternativa B está errada:**
Automação irrestrita em decisões sensíveis fere princípios de responsible AI.

</details>
