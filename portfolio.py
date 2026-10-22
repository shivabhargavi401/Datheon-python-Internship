import csv

stocks = {
    "AAPL": 220,
    "MSFT": 420,
    "GOOGL": 180,
    "AMZN": 200,
    "NVDA": 130
}

portfolio = []

while True:
    symbol = input("Enter stock symbol (or done): ").upper()

    if symbol == "DONE":
        break

    if symbol not in stocks:
        print("Stock not found. Try AAPL, MSFT, GOOGL, AMZN or NVDA.")
        continue

    try:
        buy = float(input("Purchase price per share: "))
        qty = int(input("Number of shares: "))

        if buy <= 0 or qty <= 0:
            print("Enter positive values.")
            continue

    except ValueError:
        print("Please enter valid numbers.")
        continue

    current = stocks[symbol]
    invested = buy * qty
    value = current * qty
    profit = value - invested
    percent = profit / invested * 100

    portfolio.append([
        symbol, buy, qty, current,
        invested, value, profit, round(percent, 2)
    ])

print("\nSTOCK PORTFOLIO REPORT")

for s in portfolio:
    print(
        f"{s[0]} | Invested: {s[4]:.2f} | "
        f"Market Value: {s[5]:.2f} | "
        f"Profit/Loss: {s[6]:.2f} | "
        f"Change: {s[7]}%"
    )

with open("portfolio_summary.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Symbol", "Buy Price", "Quantity", "Current Price",
        "Invested", "Market Value", "Profit/Loss", "Percentage"
    ])

    writer.writerows(portfolio)

print("\nReport saved to portfolio_summary.csv")