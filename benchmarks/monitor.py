import argparse, csv, subprocess, time
from datetime import datetime, timezone
from pathlib import Path
import psutil

OUT = Path(__file__).resolve().parents[1] / "results"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--duration", type=int, default=90)
    p.add_argument("--interval", type=float, default=1)
    p.add_argument("--port", type=int, default=8081)
    a = p.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(["lsof","-ti",f"tcp:{a.port}"], capture_output=True, text=True)
        pids = [int(x) for x in result.stdout.split() if x.isdigit()]
        proc = psutil.Process(pids[0]) if pids else None
    except (OSError, ValueError, psutil.Error):
        proc = None
    path = OUT/"system_metrics.csv"
    psutil.cpu_percent(None)
    with path.open("w", newline="") as f:
        fields = ["timestamp_utc","system_cpu_pct","available_memory_mb","api_pid","api_cpu_pct","api_rss_mb"]
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        end = time.monotonic()+a.duration
        while time.monotonic() < end:
            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory()
            pcpu, rss = "", ""
            if proc:
                try:
                    pcpu = proc.cpu_percent(None)
                    rss = round(proc.memory_info().rss/1048576, 2)
                except psutil.Error:
                    proc = None
            w.writerow({"timestamp_utc":datetime.now(timezone.utc).isoformat(),
                        "system_cpu_pct":cpu,"available_memory_mb":round(mem.available/1048576,2),
                        "api_pid":proc.pid if proc else "", "api_cpu_pct":pcpu,"api_rss_mb":rss})
            f.flush(); time.sleep(a.interval)
    print("Saved", path, "- run while Uvicorn is active for API process metrics")

if __name__ == "__main__":
    main()
