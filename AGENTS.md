# Repository Guidelines

## Project Structure & Module Organization
- Core calculator package lives in `spe_calculator/` with modules such as `calculator.py` and CLI entry `main.py`.
- Store automation assets in `configs/` (`ansible/`, `ngrok/`) and helper shell scripts in `scripts/`.
- Keep documentation (e.g., this guide, project report drafts) at the repository root; add supplementary docs under `docs/` if needed.
- Place unit tests in `tests/`, mirroring package structure (e.g., `tests/test_calculator.py` validates `spe_calculator/calculator.py`).

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: create and enter a local virtual environment before installing packages.
- `pip install -r requirements.txt`: install the editable package along with dev tools (`pytest`, `ruff`).
- `pytest`: run the full automated test suite; use `pytest -k "<pattern>"` for targeted runs.
- `ruff check spe_calculator tests`: lint the source and tests; run `ruff format spe_calculator tests` (or `ruff format --check`) before committing.
- `docker build -t spe-calculator:latest .` / `docker run -p 8000:8000 spe-calculator:latest`: verify the container image locally.

## Coding Style & Naming Conventions
- Target Python 3.11+, 4-space indentation, and add type hints for public-facing functions.
- Name modules with lowercase_and_underscores (e.g., `spe_calculator/calculator.py`); use PascalCase for classes, snake_case for functions/variables.
- Keep functions small and deterministic; guard input validation early to simplify CLI UX and testing.
- Export reusable objects through `spe_calculator/__init__.py` so downstream users can import cleanly.

## Testing Guidelines
- Write tests with `pytest`; group by feature and mirror the module path.
- Name test files `test_<module>.py` and test functions `test_<behavior>`.
- Target high coverage for core decision logic; add regression tests whenever a bug is fixed.
- Use `pytest --lf --maxfail=1` locally to iterate quickly, and capture seed values when testing stochastic policies.

## Commit & Pull Request Guidelines
- Adopt Conventional Commits (`feat:`, `fix:`, `chore:`) to keep the history searchable as the project grows.
- Scope each PR to a coherent change set, reference tracking issues in the description, and note configuration updates or migrations.
- Include test evidence (`pytest` output snippet or CI link) and screenshots/terminal captures when behavior changes are visible.
- Request review once checks pass; label breaking changes explicitly and provide rollback instructions in the PR body.
