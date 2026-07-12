#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
# "yfinance" utilise les informations du site Yahoo! Finance (https://fr.finance.yahoo.com/)
# https://github.com/ranaroussi/yfinance
# https://ranaroussi.github.io/yfinance/#quick-start
# https://ranaroussi.github.io/yfinance/reference/index.html

import yfinance as yf               #Framework permettant l'obtention des informations financières.
import pandas as pd                 #Framework permettant le traitement des informations reçues.
import matplotlib.pyplot as plt     #Framework permettant de générer des graphiques.


def yfinance(ticker, period='5d', output_csv=True):
    """
    Fetch financial data for a given ticker and plot Open/Close prices.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'RNO.PA', 'MSFT')
        period (str): Data period - '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        output_csv (bool): Whether to save data to CSV file
    
    Returns:
        pd.DataFrame: Historical price data
    """
    try:
        # Fetch financial data
        stock = yf.Ticker(ticker)
        history = stock.history(period=period)
        
        if history.empty:
            print(f"Error: No data found for ticker '{ticker}'")
            return None
        
        # Save to CSV if requested
        if output_csv:
            csv_filename = f"HISTORIQUE_{ticker}_{period}.csv"
            history.to_csv(csv_filename)
            print(f"Data saved to {csv_filename}")
        
        # Extract data for plotting
        dates = history.index
        open_prices = history['Open']
        close_prices = history['Close']
        
        # Create and configure plot
        plt.figure(figsize=(10, 6))
        plt.plot(dates, open_prices, label='OPEN', marker='o', linewidth=2)
        plt.plot(dates, close_prices, label='CLOSE', marker='s', linewidth=2)
        
        # Labels and title
        plt.xlabel('Date')
        plt.ylabel('Price (€/$)')
        plt.title(f"Stock Price History - {ticker}")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return history
        
    except Exception as e:
        print(f"Error fetching data for '{ticker}': {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage
    yfinance("RNO.PA", period='3mo')
    # yfinance("MSFT", period='1mo')
