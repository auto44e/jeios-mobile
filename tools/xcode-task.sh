#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail
cd "$(dirname "$0")/.."
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
case "${1:-}" in
  validate) exec python3 tools/validate.py ;;
  test) exec python3 -m unittest discover -s tests -v ;;
  plan) exec python3 tools/target_plan.py ;;
  *) echo "error: Unknown Xcode task: ${1:-<missing>}" >&2; exit 2 ;;
esac
