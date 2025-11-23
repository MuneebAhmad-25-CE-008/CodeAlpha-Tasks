import os
import csv
from datetime import datetime

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180.00,   # Apple Inc.
    "TSLA": 250.00,   # Tesla Inc.
    "GOOGL": 140.00,  # Alphabet Inc.
    "MSFT": 370.00,   # Microsoft Corporation
    "AMZN": 145.00,   # Amazon.com Inc.
    "META": 330.00,   # Meta Platforms Inc.
    "NVDA": 480.00,   # NVIDIA Corporation
    "JPM": 150.00,    # JPMorgan Chase & Co.
    "V": 250.00,      # Visa Inc.
    "WMT": 160.00     # Walmart Inc.
}

def clear_screen():
    """Clear the console screen in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")

def display_header():
    """Display the application header."""
    print("\n" + "=" * 60)
    print(" STOCK PORTFOLIO TRACKER ".center(60))
    print("=" * 60 + "\n")

def display_available_stocks():
    """Display all available stocks and their prices."""
    print("Available Stocks:")
    print("-" * 40)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"  {symbol:<10} ${price:>10.2f}")
    print("-" * 40 + "\n")

def get_user_input():
    """
    Get stock names and quantities from user.
    Returns a dictionary with stock symbols as keys and quantities as values.
    """
    portfolio = {}
    print("Enter your stock portfolio details.")
    print("(Press Enter with empty stock name when done)\n")
    
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        
        if not stock_name:
            break
        
        if stock_name not in STOCK_PRICES:
            print(f"Error: '{stock_name}' is not in our database. Please choose from available stocks.\n")
            continue
        
        try:
            quantity = input(f"Enter quantity for {stock_name}: ").strip()
            quantity = int(quantity)
            
            if quantity <= 0:
                print("Error: Quantity must be a positive number.\n")
                continue
            
            if stock_name in portfolio:
                print(f"Warning: {stock_name} already exists. Adding to existing quantity.\n")
                portfolio[stock_name] += quantity
            else:
                portfolio[stock_name] = quantity
            
            print(f"Added: {quantity} shares of {stock_name}\n")
        
        except ValueError:
            print("Error: Please enter a valid number for quantity.\n")
            continue
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """
    Calculate the total investment value and individual stock values.
    Returns a tuple of (total_value, stock_details)
    """
    stock_details = []
    total_value = 0.0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        stock_details.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value
        })
    
    return total_value, stock_details

def display_portfolio(portfolio, total_value, stock_details):
    """Display the portfolio summary."""
    print("\n" + "=" * 60)
    print(" PORTFOLIO SUMMARY ".center(60))
    print("=" * 60 + "\n")
    
    if not portfolio:
        print("No stocks in portfolio.\n")
        return
    
    print(f"{'Stock':<10} {'Quantity':>10} {'Price':>12} {'Total Value':>15}")
    print("-" * 60)
    
    for detail in stock_details:
        print(f"{detail['symbol']:<10} {detail['quantity']:>10} "
              f"${detail['price']:>11.2f} ${detail['value']:>14.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL INVESTMENT VALUE:':<35} ${total_value:>14.2f}")
    print("=" * 60 + "\n")

def save_to_txt(portfolio, total_value, stock_details, filename="portfolio_summary.txt"):
    """Save portfolio summary to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write(" STOCK PORTFOLIO SUMMARY ".center(60) + "\n")
            f.write("=" * 60 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if not portfolio:
                f.write("No stocks in portfolio.\n")
            else:
                f.write(f"{'Stock':<10} {'Quantity':>10} {'Price':>12} {'Total Value':>15}\n")
                f.write("-" * 60 + "\n")
                
                for detail in stock_details:
                    f.write(f"{detail['symbol']:<10} {detail['quantity']:>10} "
                           f"${detail['price']:>11.2f} ${detail['value']:>14.2f}\n")
                
                f.write("-" * 60 + "\n")
                f.write(f"{'TOTAL INVESTMENT VALUE:':<35} ${total_value:>14.2f}\n")
            
            f.write("=" * 60 + "\n")
        
        print(f"✓ Portfolio saved to '{filename}'")
        return True
    except Exception as e:
        print(f"Error saving to text file: {e}")
        return False

def save_to_csv(portfolio, stock_details, filename="portfolio_summary.csv"):
    """Save portfolio summary to a CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Symbol", "Quantity", "Price per Share", "Total Value"])
            
            for detail in stock_details:
                writer.writerow([
                    detail["symbol"],
                    detail["quantity"],
                    f"{detail['price']:.2f}",
                    f"{detail['value']:.2f}"
                ])
        
        print(f"✓ Portfolio saved to '{filename}'")
        return True
    except Exception as e:
        print(f"Error saving to CSV file: {e}")
        return False

def main():
    """Main function to run the stock portfolio tracker."""
    try:
        clear_screen()
        display_header()
        display_available_stocks()
        
        # Get user input
        portfolio = get_user_input()
        
        if not portfolio:
            print("\nNo stocks added. Exiting program.")
            return
        
        # Calculate portfolio value
        total_value, stock_details = calculate_portfolio_value(portfolio)
        
        # Display portfolio summary
        display_portfolio(portfolio, total_value, stock_details)
        
        # Ask if user wants to save the results
        while True:
            save_choice = input("Would you like to save the portfolio summary? (yes/no): ").strip().lower()
            if save_choice in ["yes", "y", "no", "n"]:
                break
            print("Please enter 'yes' or 'no'.\n")
        
        if save_choice in ["yes", "y"]:
            print("\nSelect file format:")
            print("1. Text file (.txt)")
            print("2. CSV file (.csv)")
            print("3. Both")
            
            while True:
                format_choice = input("Enter your choice (1/2/3): ").strip()
                if format_choice in ["1", "2", "3"]:
                    break
                print("Please enter 1, 2, or 3.\n")
            
            print()
            if format_choice == "1":
                save_to_txt(portfolio, total_value, stock_details)
            elif format_choice == "2":
                save_to_csv(portfolio, stock_details)
            else:
                save_to_txt(portfolio, total_value, stock_details)
                save_to_csv(portfolio, stock_details)
            
            print("\nThank you for using Stock Portfolio Tracker!")
        else:
            print("\nThank you for using Stock Portfolio Tracker!")
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
