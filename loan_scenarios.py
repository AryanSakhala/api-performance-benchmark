import csv

principal = 250000
rows = []

for years in (10, 15, 20, 30):
    for rate in (4.5, 5.5, 6.5, 7.5):
        r = rate / 1200
        n = years * 12
        payment = principal * r / (1 - (1 + r) ** -n)
        rows.append([years, rate, round(payment, 2), round(payment * n - principal, 2)])

with open("loan_scenarios.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["years", "rate_percent", "monthly_payment", "total_interest"])
    writer.writerows(rows)

print(len(rows), "scenarios written")
