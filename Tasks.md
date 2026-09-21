# Tasks

## Phase 1: Environment & Project Setup
- [x] **TASK-001**: Initialize local Git repository and create `.gitignore` (ignore `.env`, `venv/`, `__pycache__/`, `.pytest_cache/`).
- [x] **TASK-002**: Create virtual environment (`venv`) and set up `requirements.txt` (`python-dotenv`, `google-genai` or target LLM client, `pytest`).
- [x] **TASK-003**: Create directory structure (`data/`, `src/`, `tests/`) with package markers (`__init__.py`).
- [x] **TASK-004**: Create `.env.example` and set up local `.env` configuration for API keys.

---

## Phase 2: Data & Calculation Engine
- [x] **TASK-005**: Create `data/emission_factors.json` with baseline factors for Transportation, Electricity, and Food.
- [x] **TASK-006**: Create `src/models.py` defining data classes for user lifestyle inputs and calculation outputs.
- [x] **TASK-007**: Implement `src/engine.py` to load factors from JSON and calculate emissions per category and total footprint.
- [x] **TASK-008**: Write unit tests in `tests/test_engine.py` to verify mathematical accuracy against expected formula results.

---

## Phase 3: Input Validation & CLI Interface
- [x] **TASK-009**: Implement `src/validators.py` to validate numeric ranges, positive numbers, and menu selections.
- [x] **TASK-010**: Write unit tests in `tests/test_validators.py` covering invalid inputs (empty input, strings, negative values).
- [x] **TASK-011**: Build `src/cli.py` for terminal prompts, input collection loops, and error messages.
- [x] **TASK-012**: Implement output tables in `src/cli.py` displaying category breakdown (kg CO₂e, percentage share) and total estimate.

---

## Phase 4: AI Integration & Fallback Handling
- [x] **TASK-013**: Implement `src/ai_service.py` to initialize LLM client with environment variables.
- [x] **TASK-014**: Construct structured prompt in `src/ai_service.py` sending calculated category totals and requesting actionable reduction steps.
- [x] **TASK-015**: Add error handling and fallback logic in `src/ai_service.py` so API failures or missing keys do not crash the app.

---

## Phase 5: Application Orchestration & End-to-End Verification
- [x] **TASK-016**: Implement `src/main.py` to connect CLI inputs -> Validator -> Engine -> CLI Summary -> AI Recommendations.
- [x] **TASK-017**: Conduct end-to-end manual testing across varied lifestyle profiles.
- [x] **TASK-018**: Run full test suite with `pytest` and verify all tests pass.
- [x] **TASK-019**: Finalize `README.md` with installation, setup, and usage instructions.