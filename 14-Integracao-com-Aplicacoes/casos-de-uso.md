# Casos de Uso — Módulo 14: Integração com Aplicações

## Caso 1 — Classificacao de documentos em lote

**Cenário:** Uma empresa recebe PDFs em massa e aceita processamento em segundo plano.

**Arquitetura sugerida:** S3 + fila + backend de processamento + armazenamento do resultado.

**Por que essa escolha faz sentido:** Resiliência e desacoplamento são mais importantes que resposta imediata.

**Armadilha de prova associada:** Implementar tudo como chamada síncrona.

## Caso 2 — Chat de atendimento interno

**Cenário:** O usuário espera resposta em poucos segundos.

**Arquitetura sugerida:** API síncrona com backend controlado, observabilidade e fallback.

**Por que essa escolha faz sentido:** Experiência interativa pede desenho de baixa latência.

**Armadilha de prova associada:** Enviar o usuário para fluxo assíncrono sem necessidade.

