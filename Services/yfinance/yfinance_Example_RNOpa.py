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
from pathlib import Path            #Framework permettant de gérer les chemins de fichiers et de répertoires.


def yfinance(ticker, period='5d', output_csv=True):                                                                                                 # Obtention des informations financières pour un ticker donné et génération d'un graphique des prix Open/Close.
    """
    Fetch financial data for a given ticker and plot Open/Close prices.
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'RNO.PA', 'MSFT')
        period (str): Data period - '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
        output_csv (bool): Whether to save data to CSV file
    
    Returns:
        pd.DataFrame: Historical price data
    """
    try: # Validate input parameters
        # Fetch financial data
        stock = yf.Ticker(ticker)                                                                                                                   # Create a Ticker object for the given ticker
        history = stock.history(period=period)                                                                                                      # Fetch historical market data for the specified period
        
        if history.empty: # Check if the fetched data is empty
            print(f"Error: No data found for ticker '{ticker}'")                                                                                    # Affichage console pour indiquer qu'aucune donnée n'a été trouvée pour le ticker spécifié
            return None                                                                                                                             # Return None to indicate that no data was retrieved
        
        # Save data to CSV if requested
        if output_csv:
            csv_filename = f"HISTORIQUE_{ticker}_{period}.csv"                                                                                      # Create a CSV filename based on the ticker and period
            history.to_csv(csv_filename)                                                                                                            # Save the historical data to a CSV file with a name based on the ticker and period
            print(f"Data saved to {csv_filename}")                                                                                                  # Affichage console pour confirmer l'enregistrement du fichier CSV
        
        # Extract data for plotting
        dates = history.index # Dates for the x-axis
        open_prices = history['Open']                                                                                                               # Open prices for the y-axis
        close_prices = history['Close']                                                                                                             # Close prices for the y-axis
    
        # Create and configure plot
        plt.figure(figsize=(10, 6))                                                                                                                 # Set the figure size to 10 inches by 6 inches
        plt.plot(dates, open_prices, label='OPEN', marker='o', linewidth=2)                                                                         # Plot the open prices with circle markers and a line width of 2
        plt.plot(dates, close_prices, label='CLOSE', marker='s', linewidth=2)                                                                       # Plot the close prices with square markers and a line width of 2
        
        # Labels and title
        plt.xlabel('Date')                                                                                                                          # Set the x-axis label to 'Date'
        plt.ylabel('Price (€/$)')                                                                                                                   # Set the y-axis label to 'Price (€/$)'
        plt.title(f"Stock Price History - {ticker}")                                                                                                # Set the plot title to include the ticker symbol
        plt.legend()                                                                                                                                # Display the legend to differentiate between open and close prices
        plt.grid(True, alpha=0.3)                                                                                                                   # Enable grid lines with 30% transparency for better readability
        plt.xticks(rotation=45)                                                                                                                     # Rotate x-axis labels by 45 degrees for better visibility
        plt.tight_layout()                                                                                                                          # Adjust the layout to prevent clipping of labels and titles
        
        # Enregistrer le graphique en haute résolution
        rootPNG = Path(__file__).resolve().parents[2]                                                                                               # Remonter de deux niveaux pour atteindre le répertoire racine du projet
        report = rootPNG / "Rapports"/ "PNG"                                                                                                        # Chemin vers le répertoire "Rapports/PNG"
        report.mkdir(parents=True, exist_ok=True)                                                                                                   # Créer le répertoire s'il n'existe pas 
        filename = report / f"{ticker}_{period}.png"                                                                                                # Nom du fichier PNG
        plt.savefig(filename, dpi=600, bbox_inches='tight')                                                                                         # Enregistrer le graphique en haute résolution (600 dpi) avec des marges ajustées
        print(f"Data saved to {filename}")                                                                                                          # Affichage console pour confirmer l'enregistrement du graphique
        plt.close()                                                                                                                                 # Fermer la figure pour libérer de la mémoire et éviter les conflits avec d'autres graphiques
        #plt.show()
        
        return history                                                                                                                              # Return the historical price data as a DataFrame
        
    except Exception as e:                                                                                                                          # Handle any exceptions that occur during data fetching or processing
        print(f"Error fetching data for '{ticker}': {str(e)}")                                                                                      # Affichage console pour indiquer l'erreur rencontrée lors de la récupération des données
        return None                                                                                                                                 # Return None to indicate that an error occurred


if __name__ == "__main__":
    # Example usage
    yfinance("RNO.PA", period='3mo') # Fetch and plot data for Renault (RNO.PA) over the last 3 months
    # yfinance("MSFT", period='1mo')
