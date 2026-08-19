rates = {
    "USD": 1.0,
    "INR": 86.5,
    "EUR": 0.85,
    "GBP": 0.74,
    "JPY": 147.0
}

print("Supported:", ", ".join(rates))

amount = float(input("Amount: "))
source = input("From currency: ").upper()
target = input("To currency: ").upper()

if source in rates and target in rates:
    usd_value = amount / rates[source]
    result = usd_value * rates[target]
    print(f"{amount:.2f} {source} = {result:.2f} {target}")
else:
    print("Unsupported currency.")
