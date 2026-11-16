# Use Cases — Module 05: Amazon Bedrock

## Case 1 — Internal Support Assistant

**Scenario:** The company wants answers based on documents and a filter for prohibited topics.

**Suggested architecture:** Bedrock with Knowledge Bases and Guardrails.

**Why this choice makes sense:** Unites grounding and content policy in the same managed solution.

**Associated exam trap:** Choosing just one model without thinking about the context and controls.

## Case 2 — Automation with system calls

**Scenario:** A bot needs to check order status and open a ticket when necessary.

**Suggested architecture:** Application with Amazon Bedrock Agents or equivalent orchestration layer, connected to internal APIs.

**Why this choice makes sense:** The case requires responding to and also taking actions on external systems.

**Associated exam trap:** Assuming that textual generation alone solves the entire flow.

---

## ☁️ Follow CloudStudy

We are building a platform to help Brazilians study AWS in a more practical, organized and accessible way.

Follow CloudStudy to keep up with new materials, updates and content about AWS certifications:

- Instagram: https://www.instagram.com/cloudstudy.ai/
- LinkedIn: https://www.linkedin.com/company/cloudstudy-ai/

---

> **Service availability note (November 16, 2026):** The source references Amazon Bedrock Agents, now **Amazon Bedrock Agents Classic**, which is closed to new sign-ups. Existing customers can continue using it. For new agent implementations, review [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) and the [Agents availability notice](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).
