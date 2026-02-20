
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock] = quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"✅ Added {quantity} shares of {stock}")

print("\n📊 Portfolio Summary")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {qty} shares × ${price} = ${qty * price}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save result to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares × ${stock_prices[stock]}\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n📁 Portfolio saved to 'portfolio_summary.txt'")