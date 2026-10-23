# API Performance Benchmark

A small FastAPI service with a production-style setup (request IDs, timing headers, structured logs, health/readiness probes, Docker, CI) and a benchmark suite that measures throughput, tail latency, and CPU/memory under load. Built to run on macOS (Apple Silicon or Intel) and Linux.

## Endpoints
| Route | Purpose |
|---|---|
| `GET /health` | liveness |
| `GET /ready` | readiness (returns worker PID) |
| `GET /compute/{iterations}` | CPU-bound workload, 1 to 1,000,000 iterations |

## Quick start (macOS)
```bash
make install
make test
make run            # 4 uvicorn workers on :8081
```

## Benchmarking
```bash
make bench          # 1 worker: custom benchmark + Locust + monitor + charts
make bench-multi    # 4 workers, compare against the run above
make locust-ui      # interactive Locust UI at http://localhost:8089 (API must be running)
```
On macOS the script records chip, macOS version and core count to `results/environment.txt` and wraps load generation in `caffeinate -i` so the Mac does not sleep mid-run. Tunables: `WORKERS`, `USERS`, `RUN_TIME`, `PORT`.

Outputs in `results/`: `benchmark_summary.csv`, `request_details.csv`, `locust_stats.csv`, `system_metrics.csv`, and charts (throughput, latency percentiles, CPU).

For the most reliable numbers on a Mac: plug in power, close other apps, and run each configuration at least three times.

## Docker
```bash
make docker
```

## Notes
- `/compute` is a sync CPU-bound handler, so it runs in a threadpool and is limited by the GIL. Adding `--workers` is the main scaling lever; compare `make bench` and `make bench-multi`.
- Only test systems you own or are authorized to test.
- Results are not committed. Run the benchmark on your own machine and record them.
