#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ANSIBLE_DIR="${PROJECT_ROOT}/configs/ansible"

if [[ -z "${DOCKER_HOST:-}" && -n "${XDG_RUNTIME_DIR:-}" ]]; then
  export DOCKER_HOST="unix://${XDG_RUNTIME_DIR}/docker.sock"
fi

if ! command -v ansible-playbook >/dev/null 2>&1; then
  echo "ansible-playbook is not available on PATH." >&2
  echo "Install Ansible with pipx, pip, or your package manager before running this helper." >&2
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not available on PATH. Install Docker Engine before deploying the container." >&2
  exit 1
fi

ANSIBLE_CONFIG="${ANSIBLE_DIR}/ansible.cfg" \
  ansible-galaxy collection install -r "${ANSIBLE_DIR}/requirements.yml" >/dev/null

ANSIBLE_CONFIG="${ANSIBLE_DIR}/ansible.cfg" \
  ansible-playbook \
    -i "${ANSIBLE_DIR}/inventory.ini" \
    "${ANSIBLE_DIR}/playbooks/deploy_calculator.yml" \
    "$@"
