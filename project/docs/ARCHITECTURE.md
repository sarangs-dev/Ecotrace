# Architecture

## Tech Stack

| Layer | Technology | Why |
| :--- | :--- | :--- |
| **Language** | Python 3 | Main development language[cite: 1] |
| **Interface** | CLI initially | Simplest way to build the first working version |
| **Data** | JSON | Store emission factors and configuration[cite: 1] |
| **Calculations** | Python standard library | Keep the carbon calculation transparent[cite: 1] |
| **AI** | LLM API | Generate personalized recommendations[cite: 1] |
| **Local storage** | SQLite *(optional)* | Store footprint history later |
| **Visualization** | Matplotlib *(optional)* | Simple category charts |
| **Version control** | Git | Main Git-learning component[cite: 1] |
| **Remote repository** | GitHub | Store and manage the project[cite: 1] |
| **Environment** | venv | Isolate Python dependencies |

---

## Architectural Rules

1. **Externalized Factor Storage:** Emission factors must remain in `data/emission_factors.json` and must never be hardcoded into calculation functions[cite: 1].
2. **Transparent Deterministic Math:** The calculation engine (`src/engine.py`) must calculate all numerical values strictly using standard library formulas; the LLM API must never compute, invent, or predict emission numbers[cite: 1].
3. **Pure Business Logic:** The calculation engine must remain completely decoupled from CLI I/O (`print`, `input`) and network calls, taking structured data models and returning calculated results.
4. **Boundary Validation:** CLI inputs must pass through `validators.py` before being processed by the calculation engine; empty values, non-numeric strings, and negative values must be caught and re-prompted[cite: 1].
5. **AI Interpretation Boundary:** The AI service must receive only calculated summaries and user habit context; its single responsibility is generating practical reduction recommendations based on top emitting categories[cite: 1].
6. **Graceful Degradation:** If the LLM API call fails, times out, or lacks credentials, the application must display all calculated footprints without crashing.

---

## Execution Flow

```text
User
  │ (CLI prompts & responses)
  ▼
CLI / Input Layer (main.py / cli.py)
  │ (Validates inputs)
  ▼
Validator Module (validators.py)
  │ (Clean activity data)
  ▼
Calculation Engine (engine.py) ◄── Data Layer (data/emission_factors.json)
  │ (Computed category emissions & total kg CO₂e)
  ▼
CLI Display (Formats & presents breakdown + total estimate)
  │ (Calculated summary payload)
  ▼
AI Service (ai_service.py) ──► LLM API (Generates tailored reduction actions)
  │ (Actionable recommendations)
  ▼
CLI Output (Displays AI recommendations to user)
```[cite: 1]

---

## Folder Structure

```text
carbon-footprint-calculator/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── emission_factors.json    # JSON storage for emission factors and configuration
├── src/
│   ├── __init__.py
│   ├── main.py                  # Application entry point & orchestration
│   ├── cli.py                   # User prompts, input gathering, and terminal formatting
│   ├── engine.py                # Pure calculation logic (Activity Data × Emission Factor)
│   ├── validators.py            # Input validation rules (type checking, ranges, bounds)
│   ├── ai_service.py            # LLM API integration for tailored recommendations
│   └── models.py                # Data classes for inputs and calculation results
└── tests/
    ├── __init__.py
    ├── test_engine.py           # Unit tests for calculation correctness
    └── test_validators.py       # Unit tests for input validation