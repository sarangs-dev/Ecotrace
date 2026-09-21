# Architecture Decision Records (ADR)

## ADR-001: Pure Standard Library Calculations Over External Data Frameworks
### Decision:
Use pure Python standard library types and mathematical operations for calculating emissions rather than data analysis frameworks like Pandas or NumPy.
### Reason:
The calculation scope involves a straightforward formula (`Activity Data × Emission Factor`) across three fixed categories for a single user session[cite: 1]. Introducing large numerical libraries would add heavy dependencies without adding performance or architectural value for an MVP[cite: 1].

---

## ADR-002: External JSON Storage for Emission Factors
### Decision:
Store all emission factors and calculation coefficients in a separate `data/emission_factors.json` file rather than hardcoding constants in Python source files.
### Reason:
GHG emission factors frequently change across regions and update over time[cite: 1]. Isolating them in an external JSON file allows adjustments, versioning, and region updates without touching or breaking application business logic[cite: 1].

---

## ADR-003: Deterministic Calculations Preceding AI Execution
### Decision:
Calculate all category footprints and totals deterministically via Python code before invoking any LLM API[cite: 1].
### Reason:
Large Language Models are prone to arithmetic errors and hallucinating facts when generating numbers. Restricting the LLM to interpreting pre-calculated totals ensures numerical transparency, auditability, and accurate recommendations[cite: 1].

---

## ADR-004: Terminal CLI as the Initial User Interface
### Decision:
Implement the initial MVP as a terminal Command Line Interface (CLI) instead of a web or desktop GUI[cite: 1].
### Reason:
A CLI allows immediate focus on data modeling, validation, clean modular design, and Git workflows without frontend overhead, styling complexity, or build tool management[cite: 1].

---

## ADR-005: Decoupled Single-Call LLM Integration with Graceful Fallback
### Decision:
Interact with the AI provider through a dedicated, isolated service (`src/ai_service.py`) using a single prompt invocation rather than an interactive chat agent or multi-turn conversational loop[cite: 1].
### Reason:
The application requirements call for structured recommendations based on summary data[cite: 1]. A single targeted call minimizes API latency and token cost while ensuring that if network access fails, the CLI can still present calculations without interrupting core functionality.

---

## ADR-006: In-Memory Processing for MVP Milestone
### Decision:
Run the application using in-memory state during execution, postponing database integration (such as SQLite) to post-MVP iterations[cite: 1].
### Reason:
The primary deliverable is an educational, on-the-spot estimation session[cite: 1]. Omitting persistence at this phase avoids unnecessary schema migrations and database setup while fulfilling all core MVP user flows[cite: 1].