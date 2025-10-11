FROM python:3.13-slim AS runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

RUN useradd --create-home --shell /bin/bash appuser

COPY pyproject.toml README.md /app/
COPY spe_calculator /app/spe_calculator

RUN pip install --upgrade pip && pip install .

USER appuser

EXPOSE 8000

ENTRYPOINT ["uvicorn", "spe_calculator.api:app", "--host", "0.0.0.0", "--port", "8000"]
