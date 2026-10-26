import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def load(path="benchmark_results.csv"):
    with open(path, newline="") as handle:
        return list(csv.DictReader(handle))


def series(rows, function):
    grouped = defaultdict(lambda: {"x": [], "ns": [], "err": []})
    for row in rows:
        if row["function"] != function:
            continue
        bucket = grouped[row["method"]]
        bucket["x"].append(float(row["input"]))
        bucket["ns"].append(float(row["ns_per_call"]))
        bucket["err"].append(float(row["abs_error"]))
    return grouped


def plot_pair(rows, function, xlabel, path):
    data = series(rows, function)
    figure, axes = plt.subplots(1, 2, figsize=(10, 4))
    for method, values in data.items():
        order = sorted(range(len(values["x"])), key=lambda index: values["x"][index])
        inputs = [values["x"][index] for index in order]
        axes[0].plot(inputs, [values["ns"][index] for index in order], marker="o", label=method)
        axes[1].plot(inputs, [values["err"][index] for index in order], marker="o", label=method)
    axes[0].set_title(f"{function} speed")
    axes[0].set_xlabel(xlabel)
    axes[0].set_ylabel("nanoseconds per call")
    axes[0].legend()
    axes[1].set_title(f"{function} absolute error")
    axes[1].set_xlabel(xlabel)
    axes[1].set_ylabel("absolute error")
    axes[1].legend()
    figure.tight_layout()
    figure.savefig(path, dpi=140)
    plt.close(figure)
    print("saved", path)


def main():
    rows = load()
    plot_pair(rows, "exp", "input value", "exp_comparison.png")
    plot_pair(rows, "sigmoid", "input value", "sigmoid_comparison.png")
    plot_pair(rows, "softmax", "vector size", "softmax_comparison.png")


if __name__ == "__main__":
    main()
