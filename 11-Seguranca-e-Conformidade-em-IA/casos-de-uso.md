# Casos de Uso — Módulo 11: Segurança e Conformidade em IA

## Caso 1 — Dados de clientes em assistente interno

**Cenário:** A empresa quer usar um assistente com histórico de clientes e contratos.

**Arquitetura sugerida:** S3 privado, IAM mínimo necessário, KMS, logs de auditoria e revisão do escopo do dado enviado ao modelo.

**Por que essa escolha faz sentido:** A solução segura começa antes da chamada ao modelo.

**Armadilha de prova associada:** Focar só na interface e esquecer o dado.

## Caso 2 — API corporativa integrada ao bot

**Cenário:** O assistente consulta um ERP e precisa de credenciais seguras.

**Arquitetura sugerida:** Guardar segredos no Secrets Manager e controlar acesso pela role da aplicação.

**Por que essa escolha faz sentido:** Integração segura é parte da segurança de IA.

**Armadilha de prova associada:** Hardcode de token em código ou prompt.

