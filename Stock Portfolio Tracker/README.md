# Stock Portfolio Tracker

A simple Python application to track stock portfolio and calculate total investment value.

## Features

- **Stock Selection**: Choose from a predefined list of 10 popular stocks (AAPL, TSLA, GOOGL, MSFT, AMZN, META, NVDA, JPM, V, WMT)
- **Quantity Input**: Enter the quantity of shares for each stock
- **Investment Calculation**: Automatically calculates total investment value based on hardcoded stock prices
- **Portfolio Summary**: Displays a formatted summary of your portfolio with individual and total values
- **File Export**: Save portfolio summary to:
  - Text file (.txt) for readable format
  - CSV file (.csv) for spreadsheet compatibility

## How to Run

1. Navigate to the `src` directory:
   ```bash
   cd "Stock Portfolio Tracker/src"
   ```

2. Run the program:
   ```bash
   python stock_portfolio_tracker.py
   ```

3. Follow the prompts to:
   - View available stocks and their prices
   - Enter stock symbols and quantities
   - View your portfolio summary
   - Optionally save the results to a file

## Example Usage

```
Enter stock symbol (e.g., AAPL): AAPL
Enter quantity for AAPL: 10
Added: 10 shares of AAPL

Enter stock symbol (e.g., AAPL): TSLA
Enter quantity for TSLA: 5
Added: 5 shares of TSLA

Enter stock symbol (e.g., AAPL): [Press Enter to finish]
```

## Stock Prices (Hardcoded)

| Symbol | Company              | Price   |
|--------|----------------------|---------|
| AAPL   | Apple Inc.           | $180.00 |
| TSLA   | Tesla Inc.           | $250.00 |
| GOOGL  | Alphabet Inc.        | $140.00 |
| MSFT   | Microsoft Corp.      | $370.00 |
| AMZN   | Amazon.com Inc.      | $145.00 |
| META   | Meta Platforms Inc.  | $330.00 |
| NVDA   | NVIDIA Corporation   | $480.00 |
| JPM    | JPMorgan Chase & Co. | $150.00 |
| V      | Visa Inc.            | $250.00 |
| WMT    | Walmart Inc.         | $160.00 |

## Key Concepts Demonstrated

- **Dictionary**: Hardcoded stock prices stored in a dictionary
- **Input/Output**: User input for stock names and quantities
- **Basic Arithmetic**: Calculation of investment values
- **File Handling**: Optional saving of results to .txt or .csv files

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)
