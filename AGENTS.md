# Repository Guidelines

## Project Structure & Module Organization
- Keep runnable code in `src/`; group reusable agent logic under `src/agents/<agent_name>.py`.
- Store environment or scenario definitions in `configs/` with JSON/YAML profiles; keep secrets in `.env` files excluded from Git.
- Place notebooks, design docs, and diagrams in `docs/`; add helper scripts and one-off utilities in `scripts/`.
- Write unit and integration coverage in `tests/` mirroring the `src/` tree (`tests/agents/test_<agent_name>.py`), and include sample fixtures in `tests/fixtures/`.

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: create and enter a local virtual environment before installing packages.
- `pip install -r requirements.txt`: install runtime and tooling dependencies; update the file whenever new packages are introduced.
- `pytest`: run the full automated test suite; use `pytest -k "agent_name"` for focused runs during development.
- `ruff check src tests`: lint and static-check code; run `ruff format src tests` (or `black`) before committing.

## Coding Style & Naming Conventions
- Use Python 3.11+ syntax, 4-space indentation, and type annotations on public functions and dataclasses.
- Name modules with lowercase and underscores (`src/agents/path_planner.py`); classes in PascalCase; functions and variables in snake_case.
- Keep functions short and side-effect free; favor dependency injection over globals to simplify agent reuse.
- Export agent entry points via `__all__` in package `__init__.py` files for clarity.

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
