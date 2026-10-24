PY ?= python3
.PHONY: install test run bench locust-ui docker
install:
	$(PY) -m venv .venv && .venv/bin/pip install -q --upgrade pip --disable-pip-version-check && .venv/bin/pip install -q --disable-pip-version-check -r requirements-dev.txt
test:
	.venv/bin/pytest -q
run:
	.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8081 --workers 4
bench:
	PYTHON=.venv/bin/python WORKERS=1 ./scripts/run_bench.sh
bench-multi:
	PYTHON=.venv/bin/python WORKERS=4 ./scripts/run_bench.sh
locust-ui:
	.venv/bin/locust -f benchmarks/locustfile.py --host http://127.0.0.1:8081
docker:
	docker build -t api-performance . && docker run --rm -p 8081:8081 api-performance
