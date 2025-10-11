#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NGROK_CONFIG="${PROJECT_ROOT}/configs/ngrok/ngrok.yml"

if ! command -v ngrok >/dev/null 2>&1; then
  echo "ngrok is not available on PATH. Install it from https://ngrok.com/download." >&2
  exit 1
fi

if [[ ! -f "${NGROK_CONFIG}" ]]; then
  echo "Expected ngrok config at ${NGROK_CONFIG} but it was not found." >&2
  exit 1
fi

ngrok start --all --config "${NGROK_CONFIG}"
