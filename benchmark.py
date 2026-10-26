import csv, math, time

def taylor_exp(x):
    term = total = 1.0
    for k in range(1, 7):
        term *= x / k
        total += term
    return total

def softmax(values, exp):
    top = max(values)
    parts = [exp(v - top) for v in values]
    total = sum(parts)
    return [p / total for p in parts]

sigmoid = lambda x: 1 / (1 + math.exp(-x))
fast_sigmoid = lambda x: 0.5 + x / (2 * (1 + abs(x)))

methods = [
    ("exp", "exact", math.exp, math.exp),
    ("exp", "taylor", taylor_exp, math.exp),
    ("sigmoid", "exact", sigmoid, sigmoid),
    ("sigmoid", "fast", fast_sigmoid, sigmoid),
]

rows = []
for func, method, approx, exact in methods:
    for x in (-6, -2, 0, 2, 6):
        start = time.perf_counter()
        for _ in range(100000):
            approx(x)
        ns = (time.perf_counter() - start) / 100000 * 1e9
        rows.append([func, method, x, round(ns, 1), abs(approx(x) - exact(x))])

for size in (10, 100, 1000):
    values = [(i % 13) - 6 for i in range(size)]
    reference = softmax(values, math.exp)
    for method, exp in (("exact", math.exp), ("taylor", taylor_exp)):
        start = time.perf_counter()
        for _ in range(200):
            result = softmax(values, exp)
        ns = (time.perf_counter() - start) / 200 * 1e9
        error = max(abs(a - b) for a, b in zip(result, reference))
        rows.append(["softmax", method, size, round(ns, 1), error])

with open("benchmark_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["function", "method", "input", "ns_per_call", "abs_error"])
    writer.writerows(rows)

print(len(rows), "measurements written")
