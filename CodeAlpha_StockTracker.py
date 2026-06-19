import os

def calculate_portfolio():
    # 1. Hardcoded stock prices dictionary
    STOCK_PRICES = {
        "APPL": 180,
        "TSLA": 250,
        "MSFT": 420,
        "GOOGL": 175,
        "AMZN": 185
    }
    
    portfolio = {}
    
    print("=======================================")
    print("   CodeAlpha Stock Portfolio Tracker   ")
    print("=======================================")
    print("Available stocks to track:")
    for ticker, price in STOCK_PRICES.items():
        print(f" - {ticker}: ${price}")
    print("=======================================\n")

    # 2. Main data input loop
    while True:
        ticker = input("Enter stock ticker symbol (or type 'done' to finish): ").strip().upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in STOCK_PRICES:
            print(f"❌ '{ticker}' is not in our system. Please choose from the available list.")
            continue

        # Get and validate stock quantity
        try:
            quantity = int(input(f"Enter the number of shares for {ticker}: "))
            if quantity < 0:
                print("❌ Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number for quantity.")
            continue

        # Update portfolio (add quantities together if they enter the same stock twice)
        if ticker in portfolio:
            portfolio[ticker] += quantity
        else:
            portfolio[ticker] = quantity
            
        print(f"✅ Added {quantity} shares of {ticker} to your tracking list.\n")

    # 3. Calculations and Report Generation
    if not portfolio:
        print("\nEmpty portfolio. No tracker file generated.")
        return

    print("\n" + "="*40)
    print("          PORTFOLIO SUMMARY            ")
    print("="*40)
    
    total_portfolio_value = 0
    report_lines = [
        "=======================================\n",
        "         STOCK PORTFOLIO REPORT        \n",
        "=======================================\n",
        f"{'Stock':<10}{'Shares':<10}{'Price':<10}{'Total Value':<12}\n",
        "-" * 45 + "\n"
    ]

    for ticker, shares in portfolio.items():
        unit_price = STOCK_PRICES[ticker]
        stock_total_value = shares * unit_price
        total_portfolio_value += stock_total_value
        
        # Display to console
        print(f"{ticker:<10}{shares:<10}${unit_price:<9}${stock_total_value:<11}")
        
        # Append formatted line for the text file
        report_lines.append(f"{ticker:<10}{shares:<10}${unit_price:<9}${stock_total_value:<11}\n")

    print("-" * 40)
    print(f"Total Portfolio Investment: ${total_portfolio_value:,}")
    print("=" * 40)

    # Append totals to file report data
    report_lines.append("-" * 45 + "\n")
    report_lines.append(f"Total Portfolio Investment: ${total_portfolio_value:,}\n")
    report_lines.append("=======================================\n")

    # 4. File Handling: Save results to a .txt file
    filename = "portfolio_summary.txt"
    try:
        with open(filename, "w") as file:
            file.writelines(report_lines)
        print(f"\n💾 Report successfully saved to: {os.path.abspath(filename)}")
    except IOError:
        print("\n❌ Error: Could not save the report file.")

if __name__ == "__main__":
    calculate_portfolio()