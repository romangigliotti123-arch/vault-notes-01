#!/usr/bin/env sh
# Convenience wrapper for macOS/Linux (and Git Bash): ./doctor.sh [--net]
DIR="$(cd "$(dirname "$0")" && pwd)"
for PY in python3 python py; do
  if command -v "$PY" >/dev/null 2>&1 && "$PY" -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" >/dev/null 2>&1; then
    exec "$PY" "$DIR/doctor.py" "$@"
  fi
done
echo "[MISSING] python 3.8+ : macOS: brew install python | Debian/Ubuntu: sudo apt install python3 | Windows: winget install Python.Python.3.12"
exit 1
