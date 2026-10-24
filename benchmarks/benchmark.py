import argparse, csv, os, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
URL = os.environ.get("API_URL", "http://127.0.0.1:8081")

def request_once(request_id, iterations, timeout):
    start = time.perf_counter()
    try:
        r = requests.get(f"{URL}/compute/{iterations}", timeout=timeout)
        return {"request_id": request_id, "status_code": r.status_code,
                "latency_ms": (time.perf_counter()-start)*1000,
                "success": r.status_code == 200, "error": ""}
    except requests.RequestException as exc:
        return {"request_id": request_id, "status_code": 0,
                "latency_ms": (time.perf_counter()-start)*1000,
                "success": False, "error": str(exc)}

def pct(values, p):
    values = sorted(values)
    return round(values[min(len(values)-1, max(0, int(len(values)*p + .999999)-1))], 3) if values else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--requests", type=int, default=100)
    ap.add_argument("--concurrency", type=int, nargs="+", default=[2,4,8,16,32])
    ap.add_argument("--iterations", type=int, default=10000)
    ap.add_argument("--timeout", type=float, default=15)
    a = ap.parse_args()
    if a.requests < 1 or a.iterations < 1 or any(c < 1 for c in a.concurrency):
        ap.error("requests, iterations, and concurrency must be positive")
    OUT.mkdir(parents=True, exist_ok=True)
    details, summary = OUT/"request_details.csv", OUT/"benchmark_summary.csv"
    fields = ["scenario","request_id","concurrency","iterations","status_code","latency_ms","success","error"]
    rows = []
    with details.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for c in a.concurrency:
            name = f"r{a.requests}_c{c}_i{a.iterations}"
            start = time.perf_counter(); results = []
            with ThreadPoolExecutor(max_workers=c) as pool:
                jobs = [pool.submit(request_once, i, a.iterations, a.timeout) for i in range(1,a.requests+1)]
                for job in as_completed(jobs):
                    r = job.result(); r.update(scenario=name, concurrency=c, iterations=a.iterations)
                    w.writerow(r); results.append(r)
            elapsed = time.perf_counter()-start
            lat = [r["latency_ms"] for r in results]; errors = sum(not r["success"] for r in results)
            row = {"scenario":name,"requests":len(results),"concurrency":c,"iterations":a.iterations,
                   "duration_seconds":round(elapsed,3),"successful_requests":len(results)-errors,
                   "errors":errors,"error_rate_pct":round(100*errors/len(results),2),
                   "throughput_rps":round((len(results)-errors)/elapsed,3),
                   "mean_latency_ms":round(sum(lat)/len(lat),3),"p50_latency_ms":pct(lat,.50),
                   "p95_latency_ms":pct(lat,.95),"p99_latency_ms":pct(lat,.99)}
            rows.append(row); print(row)
    with summary.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print("Saved:", f"results/{details.name}", f"results/{summary.name}")

if __name__ == "__main__":
    main()
