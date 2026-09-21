# Personal Carbon Footprint Calculator (SDG 13 - Climate Action)

A lightweight CLI Python application that estimates an individual's approximate monthly carbon footprint across everyday activities (Transportation, Electricity, and Food) using standard greenhouse-gas emission factors and provides personalized AI-driven reduction recommendations.

---

## 🌟 Key Features

1. **Interactive Terminal CLI:** Simple prompts with input validation for activity inputs.
2. **Deterministic Calculation Engine:** Transparent math based on `Activity Data × Emission Factor` with constants stored in `data/emission_factors.json`.
3. **Itemized Footprint Breakdown:** Shows category emissions ($kg CO_2e$), percentage share, overall monthly footprint estimate, and largest emission driver.
4. **AI-Driven Personalization:** Generates practical, context-specific reduction recommendations using the Google Gemini API (`google-genai`).
5. **Graceful Fallback:** Displays calculated numerical results safely without crashing even if network calls or API keys are missing.

---

## 📁 Project Structure

```text
Personal Carbon Footprint Calculator/
├── .env.example              # Sample environment configuration template
├── .gitignore                # Git exclusions (venv, secrets, cache)
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies (python-dotenv, google-genai, pytest)
├── Tasks.md                  # Task roadmap and progress tracking
├── project.md                # Project scope and problem statement
├── data/
│   └── emission_factors.json # Emission factor constants
├── src/
│   ├── __init__.py
│   ├── main.py               # Main CLI entry point
│   ├── cli.py                # Terminal formatting and prompt interface
│   ├── engine.py             # Deterministic carbon calculation engine
│   ├── validators.py         # Input validation guardrails
│   ├── ai_service.py         # Gemini API integration & recommendation fallback
│   └── models.py             # Strongly typed data models
└── tests/
    ├── __init__.py
    ├── test_ai_service.py    # Unit tests for AI service fallback
    ├── test_engine.py        # Unit tests for carbon calculation logic
    └── test_validators.py    # Unit tests for input boundary validation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher installed.

### 1. Clone & Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration (Optional for AI Tips)

To enable Gemini-powered personalized recommendations:
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your API key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

*Note: If no API key is provided, the application will automatically fall back to built-in expert sustainability recommendations.*

---

## 🧪 Running Unit Tests

Run the full automated test suite with `pytest`:

```bash
pytest
```

---

## 💻 Running the Application

Execute the application main script:

```bash
python src/main.py
```

Follow the interactive terminal prompts to enter your monthly travel distances, electricity usage, and diet style.

---

## 📜 License & Disclaimers

This project is an **educational estimator** developed for learning and individual awareness under SDG 13 (Climate Action). Numerical results are approximations based on generalized regional emission factors.
