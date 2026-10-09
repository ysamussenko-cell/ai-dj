#!/bin/bash
# Запустить шаг сборки; при ошибке — её строки в аннотации GitHub (логи отсюда не читаются).
LOG="$1"; shift
set -o pipefail
bash -e -c "$*" 2>&1 | tee "$LOG"
rc=${PIPESTATUS[0]}
if [ $rc -ne 0 ]; then python3 "$(dirname "$0")/ci_err.py" "$LOG"; fi
exit $rc
