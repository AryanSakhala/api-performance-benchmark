import csv
from collections import Counter

INPUT = "input/expenses_raw.csv"
CLEAN = "expenses_clean.csv"
FLAGGED = "expenses_flagged.csv"

with open(INPUT, newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["vendor"] = row["vendor"].strip()
    row["category"] = row["category"].strip().title()
    row["date"] = row["date"].strip()

seen = set()
clean, flagged, duplicates = [], [], 0
for row in rows:
    key = (row["date"], row["vendor"], row["amount"], row["category"])
    if key in seen:
        duplicates += 1
        continue
    seen.add(key)
    (clean if row["date"] else flagged).append(row)

fields = ["date", "vendor", "amount", "category"]
for path, data in ((CLEAN, clean), (FLAGGED, flagged)):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

totals = Counter()
for row in clean:
    totals[row["category"]] += float(row["amount"])

print(f"Rows read: {len(rows)}")
print(f"Duplicates removed: {duplicates}")
print(f"Rows flagged (missing date): {len(flagged)}")
print(f"Rows kept: {len(clean)}")
print("Top categories:")
for category, total in totals.most_common(3):
    print(f"  {category}: {total:.2f}")
