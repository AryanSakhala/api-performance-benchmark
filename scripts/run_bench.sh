#!/usr/bin/env bash
# Full benchmark: start API, run custom benchmark + Locust, monitor, analyse. Works on macOS and Linux.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
WORKERS="${WORKERS:-1}"
PORT="${PORT:-8081}"
USERS="${USERS:-50}"
RUN_TIME="${RUN_TIME:-30s}"
mkdir -p results

if [ "$(uname)" = "Darwin" ]; then
  { sysctl -n machdep.cpu.brand_string; sw_vers -productVersion; sysctl -n hw.ncpu; } > results/environment.txt 2>/dev/null || true
  CAFF="caffeinate -i"
else
  { uname -a; nproc; } > results/environment.txt
  CAFF=""
fi
$PY --version >> results/environment.txt

export API_URL="http://127.0.0.1:$PORT"
$PY -m uvicorn app.main:app --host 127.0.0.1 --port "$PORT" --workers "$WORKERS" --log-level warning &
API=$!
trap 'kill $API 2>/dev/null || true' EXIT
for _ in $(seq 1 50); do curl -fs "http://127.0.0.1:$PORT/health" >/dev/null && break; sleep 0.2; done

$PY benchmarks/monitor.py --duration 60 --interval 1 --port "$PORT" &
MON=$!
$CAFF $PY benchmarks/benchmark.py --requests 100 --concurrency 2 4 8 16 --iterations 10000
$CAFF $PY -m locust -f benchmarks/locustfile.py --headless -u "$USERS" -r 10 -t "$RUN_TIME" \
  --host "http://127.0.0.1:$PORT" --csv results/locust --only-summary
wait $MON || true
$PY benchmarks/analyse.py
echo "Done. Results in results/ (workers=$WORKERS)"
