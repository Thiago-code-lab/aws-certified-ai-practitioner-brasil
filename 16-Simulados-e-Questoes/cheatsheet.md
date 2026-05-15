# Cheatsheet — Simulados e Questões

## Formato da prova

| Item | Valor |
| --- | --- |
| Questões totais | 65 |
| Questões pontuadas | 50 |
| Questões não pontuadas | 15 |
| Tempo total | 90 minutos |
| Score mínimo | 700/1000 |
| Tipos de questão | múltipla escolha, múltiplas respostas, ordenação e associação |

## Sinais rápidos de leitura

| Situação | Como agir | Sinal de prova |
| --- | --- | --- |
| Confusão entre Bedrock e SageMaker AI | Voltar aos módulos 05 e 06 | A pergunta fala em consumir FM ou em construir ML? |
| Erro em RAG | Revisar módulos 04 e 08 | A questão fala em documentos internos atualizados? |
| Erro em IA responsável | Revisar módulos 07 e 11 | Há decisão sensível, viés, auditoria ou revisão humana? |
| Erro em custo | Revisar módulo 15 | A empresa precisa eficiência operacional ou menor gasto? |
| Erro em segurança | Revisar módulo 11 | A questão fala em acesso, segredo, criptografia, PII ou rastreabilidade? |

## Heurísticas de resposta

- Serviço especializado costuma vencer LLM amplo quando o problema é objetivo.
- Bedrock costuma vencer infraestrutura própria quando a exigência é consumir FM com menor operação.
- SageMaker AI costuma vencer Bedrock quando a questão pede treino, customização profunda ou ciclo de vida de ML.
- Guardrails não substituem IAM, KMS, logs ou revisão humana.
- RAG não é sinônimo de fine-tuning.

## Armadilhas frequentes

- Escolher GenAI quando a pergunta pede OCR, recomendação ou sentimento.
- Tratar embeddings como se eles gerassem resposta final.
- Ignorar custo do contexto e do tamanho da saída.
- Achar que uma única política de conteúdo resolve governança inteira.
