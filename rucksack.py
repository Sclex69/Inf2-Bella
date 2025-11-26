# Full list of denominations (Euro)
bills = [500, 200, 100, 50, 20, 10, 5]
coins = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

# Get amount from user
amount = float(input("Enter an amount of money: "))

# Ask if the user wants paper money
use_bills = input("Use paper money? (yes/no): ").strip().lower()

# Choose which denominations to use
if use_bills == "yes":
    denominations = bills + coins
else:
    denominations = coins  # coins only

result = {}
remaining = amount

for d in denominations:
    count = int(remaining // d)
    if count > 0:
        result[d] = count
        remaining = round(remaining - count * d, 2)

# Output
for d, c in result.items():
    if d >= 5:  # bill
        print(f"{c} × {int(d)}€ bill")
    elif d >= 1:  # 1€ or 2€ coin
        print(f"{c} × {int(d)}€ coin")
    else:  # cents
        print(f"{c} × {int(d * 100)}¢ coin")
print (result.items())