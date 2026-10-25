import csv

rows = list(csv.DictReader(open("input/expenses_raw.csv")))
seen, clean, flagged = set(), [], []

for row in rows:
    row["category"] = row["category"].strip().title()
    key = tuple(row.values())
    if key in seen:
        continue
    seen.add(key)
    if row["date"]:
        clean.append(row)
    else:
        flagged.append(row)

writer = csv.DictWriter(open("expenses_clean.csv", "w", newline=""), rows[0].keys())
writer.writeheader()
writer.writerows(clean)

print("Rows in:", len(rows))
print("Duplicates removed:", len(rows) - len(clean) - len(flagged))
print("Rows flagged (missing date):", len(flagged))
