import logging
import os
import time
import uuid

from fastapi import FastAPI, Path, Request

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("api")

app = FastAPI(title="Local API Performance Test", version="1.1.0")


@app.middleware("http")
async def observability(request: Request, call_next):
    request_id = request.headers.get("x-request-id") or uuid.uuid4().hex
    start = time.perf_counter()
    response = await call_next(request)
    elapsed_ms = (time.perf_counter() - start) * 1000
    response.headers["x-request-id"] = request_id
    response.headers["x-process-time-ms"] = f"{elapsed_ms:.3f}"
    if request.url.path != "/health":
        log.info("%s %s %s %.1fms id=%s", request.method, request.url.path, response.status_code, elapsed_ms, request_id)
    return response


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready", "pid": os.getpid()}


@app.get("/compute/{iterations}")
def compute(iterations: int = Path(ge=1, le=1_000_000)):
    value = 0
    for i in range(iterations):
        value = (value + i * 7) % 1_000_003
    return {"iterations": iterations, "result": value}
