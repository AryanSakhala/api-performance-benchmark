from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "results"
p = OUT/"benchmark_summary.csv"
if not p.exists():
    raise SystemExit("Run benchmark.py first; summary CSV is missing.")
d = pd.read_csv(p)
if d.empty:
    raise SystemExit("Summary CSV is empty.")
plt.figure(figsize=(8,5))
plt.plot(d.concurrency,d.throughput_rps,marker="o")
plt.xlabel("Concurrency (workers)"); plt.ylabel("Successful requests/second")
plt.title("API Throughput vs Concurrency"); plt.grid(True,alpha=.3); plt.tight_layout()
plt.savefig(OUT/"throughput_vs_concurrency.png",dpi=160); plt.close()
plt.figure(figsize=(8,5))
for col,label in [("mean_latency_ms","Mean"),("p95_latency_ms","P95"),("p99_latency_ms","P99")]:
    plt.plot(d.concurrency,d[col],marker="o",label=label)
plt.xlabel("Concurrency (workers)"); plt.ylabel("Latency (ms)")
plt.title("Latency Percentiles vs Concurrency"); plt.legend(); plt.grid(True,alpha=.3); plt.tight_layout()
plt.savefig(OUT/"latency_percentiles_vs_concurrency.png",dpi=160); plt.close()
mp = OUT/"system_metrics.csv"
if mp.exists():
    m = pd.read_csv(mp)
    if not m.empty:
        plt.figure(figsize=(8,5)); plt.plot(m.index,m.system_cpu_pct,label="System CPU %")
        plt.xlabel("Sample"); plt.ylabel("CPU (%)"); plt.title("macOS System CPU Samples")
        plt.grid(True,alpha=.3); plt.tight_layout(); plt.savefig(OUT/"system_cpu.png",dpi=160); plt.close()
print(d.to_string(index=False))
print("Charts saved in results/")
