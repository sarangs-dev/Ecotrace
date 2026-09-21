# Development Rules

## General
- Use Python 3.10+ standard idioms and type annotations[cite: 1].
- Keep functions modular, focused, and single-purpose.
- Do not duplicate calculation or validation logic.
- Avoid modifying unrelated files during targeted feature updates.
- Keep external runtime dependencies strictly minimal[cite: 1].

## Before Coding
- Read `PRD.md` and `ARCHITECTURE.md` before adding or modifying functionality.
- Check `data/emission_factors.json` before altering calculation logic[cite: 1].
- Verify that proposed changes adhere to the defined MVP scope[cite: 1].
- Plan changes step-by-step before implementing new modules.

## Architecture & Data
- Keep emission factors strictly in `data/emission_factors.json`; never hardcode them into functions[cite: 1].
- All carbon calculations must be deterministic and transparent using standard mathematical formulas (`Activity Data × Emission Factor`)[cite: 1].
- The calculation engine (`src/engine.py`) must have zero direct dependencies on CLI I/O (`print`, `input`) or network services.
- Data structures passed between layers must use Python dataclasses or explicit typing (`src/models.py`).

## CLI & Output
- Format all terminal displays with clear ASCII section dividers and headers.
- Display category-wise breakdowns alongside total emissions in `kg CO₂e`[cite: 1].
- Explicitly display a disclaimer indicating that results are educational monthly estimates[cite: 1].
- Include loading/progress indicators while awaiting calculations or external API calls.

## AI Integration Rules
- Never use the LLM to invent, predict, or calculate raw carbon emission numbers[cite: 1].
- Pass only verified numerical results and category rankings into the AI prompt[cite: 1].
- Frame AI outputs purely around practical interpretation and targeted lifestyle recommendations[cite: 1].
- Enforce graceful degradation: if the LLM API fails, times out, or lacks a key, print the deterministic results safely without crashing.

## Input Validation & Robustness
- Sanitize and validate every user input at the CLI boundary before processing[cite: 1].
- Reject and re-prompt on empty strings, non-numeric values, negative numbers, or invalid menu choices[cite: 1].
- Catch missing or malformed JSON files gracefully on startup.

## Security & Environment
- Never hardcode API keys, secrets, or credentials in source code.
- Store secrets exclusively in a local `.env` file and keep `.env` listed in `.gitignore`.
- Provide an up-to-date `.env.example` showing required variable templates.

## Testing & Verification
- Write unit tests in `tests/test_engine.py` for all formula calculations and edge values.
- Write unit tests in `tests/test_validators.py` for user input boundaries.
- Ensure all tests pass before committing or merging new features.

## Git & Version Control
- Write clear, concise, and descriptive commit messages following standard conventions (e.g., `feat:`, `fix:`, `refactor:`, `docs:`).
- Commit code in small, logical increments rather than large batch commits.
- Ensure no generated files, cache artifacts (`__pycache__/`), or `.env` files are tracked by Git.