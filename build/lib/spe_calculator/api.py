"""FastAPI application exposing calculator operations over HTTP."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from . import calculator

app = FastAPI(
    title="Scientific Calculator API",
    version="0.1.0",
    description="HTTP interface for the SPE mini-project scientific calculator.",
)


class OperationResponse(BaseModel):
    operation: str
    result: float


def _execute(operation_name: str, func, *args) -> OperationResponse:
    """Execute a calculator function and normalize ValueError into HTTP 400."""
    try:
        result = func(*args)
    except ValueError as exc:  # surface validation errors to the client
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return OperationResponse(operation=operation_name, result=float(result))


@app.get("/", summary="Service health probe")
def read_root() -> dict[str, str]:
    return {"status": "ok", "message": "Scientific Calculator API"}


@app.get("/sqrt", summary="Compute square root", response_model=OperationResponse)
def square_root(
    value: float = Query(..., description="Non-negative operand"),
) -> OperationResponse:
    return _execute("sqrt", calculator.square_root, value)


@app.get("/factorial", summary="Compute factorial", response_model=OperationResponse)
def factorial(
    value: int = Query(..., ge=0, description="Non-negative integer operand"),
) -> OperationResponse:
    return _execute("factorial", calculator.factorial, value)


@app.get("/ln", summary="Compute natural logarithm", response_model=OperationResponse)
def natural_log(
    value: float = Query(..., gt=0, description="Positive operand"),
) -> OperationResponse:
    return _execute("ln", calculator.natural_log, value)


@app.get("/power", summary="Compute exponentiation", response_model=OperationResponse)
def power(
    base: float = Query(..., description="Base value"),
    exponent: float = Query(..., description="Exponent value"),
) -> dict[str, float]:
    return _execute("power", calculator.power, base, exponent)
