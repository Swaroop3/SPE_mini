# Scientific Calculator (SPE Mini Project)

This repository implements the CS 816 Software Production Engineering mini-project: a menu-driven scientific calculator delivered with a DevOps toolchain.

## Features
- Square root, factorial, natural logarithm, and exponentiation operations
- Validations for invalid inputs
- Unit tests powered by `pytest`

## Quick Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
spe-calculator
```

## Run the HTTP API
```bash
uvicorn spe_calculator.api:app --reload --port 8000
# visit http://localhost:8000/sqrt?value=9
```

## Run with Docker
```bash
docker build -t spe-calculator:latest .
docker run -p 8000:8000 spe-calculator:latest
```
