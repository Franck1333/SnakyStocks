#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides :
# "yfinance" utilise les informations du site Yahoo! Finance (https://fr.finance.yahoo.com/)
# https://github.com/ranaroussi/yfinance
# https://ranaroussi.github.io/yfinance/#quick-start
# https://ranaroussi.github.io/yfinance/reference/index.html
# https://www.geeksforgeeks.org/python/export-pandas-dataframe-to-a-csv-file/
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
# https://www.geeksforgeeks.org/python/graph-plotting-in-python-set-1/
# https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html

import yfinance as yf               #Framework permettant l'obtention des informations financières.
import pandas as pd                 #Framework permettant le traitement des informations reçues.
import matplotlib.pyplot as plt     #Framework permettant de générer des graphiques.


def yfinance(TICKER):
    #Obtention des données financières.
    VALEUR = yf.Ticker(TICKER)                         #Choix du ticker.
    HISTORIQUE = VALEUR.history(period='5d')           #Affiche les cours de bourse sur X période.
                                                       #1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
    ###
    #Enregistrement des informations dans un fichier CSV.
    df_HISTORIQUE = pd.DataFrame(HISTORIQUE)
    df_HISTORIQUE.to_csv("HISTORIQUE_"+str(VALEUR)+"_.csv")
    ###

    ###
    #Selection des colonnes dans l'historique reçu.
    openClose_HISTORIQUE = df_HISTORIQUE[["Open", "Close"]]
    open_HISTORIQUE = df_HISTORIQUE[["Open"]]
    close_HISTORIQUE = df_HISTORIQUE[["Close"]]

    #Tentative d'obtention de la date, pour intégration dans l'asbcisse du graph.
    #Le format est trop long, pas utilisable tel quel.
    #date_HISTORIQUE = df_HISTORIQUE.index.values
    #print(date_HISTORIQUE)
    df_HISTORIQUE = pd.to_datetime(df_HISTORIQUE.index)
    df_HISTORIQUE.date
    print(df_HISTORIQUE.date)
    
    ##
    # line OPEN points
    x_open = df_HISTORIQUE.date
    y_open = open_HISTORIQUE
    # plotting the line OPEN points 
    plt.plot(x_open, y_open, label = "OPEN")
    ##
    # line CLOSE points
    x_close = df_HISTORIQUE.date
    y_close = close_HISTORIQUE
    # plotting the line CLOSE points 
    plt.plot(x_close, y_close, label = "CLOSE")
    ##
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title("HISTORIQUE_"+str(VALEUR))
    # show a legend on the plot
    plt.legend()
    # function to show the plot
    plt.show()
    ###
    
    ###_yfinance_
    #print(VALEUR.info)                                     #Affiche les informations générales du ticker.
    #print(VALEUR.calendar)                                 #Affiche le calendrier des moments importants pour le ticker.
    #print(VALEUR.analyst_price_targets)                    #Affiche les analyses du marché.
    #print(VALEUR.quarterly_income_stmt)                    #Affiche les revenus du tickers par quart d'année.
    #print(VALEUR.option_chain(VALEUR.options[0]).calls)    #Ne fonctionne pas sur tout les tickers.
    ###
    ####Paramètres non-testé.
    ###Paramètres pour Ticker multiples.
    #tickers = yf.Tickers('MSFT AAPL GOOG')
    #tickers.tickers['MSFT'].info
    #yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')
    ###Paramètres "FUNDS".
    #spy = yf.Ticker('SPY').funds_data
    #spy.description
    #spy.top_holdings
    ###

def yfinance_beta(TICKER):
    #BETA: Zone d'essais.
    #Obtention des données financières.
    VALEUR = yf.Ticker(TICKER)                         #Choix du ticker.
    HISTORIQUE = VALEUR.history(period='5d')           #Affiche les cours de bourse sur X période.
    df_HISTORIQUE = pd.DataFrame(HISTORIQUE)
    #print(df_HISTORIQUE)

    ###
    #date_HISTORIQUE = df_HISTORIQUE.index.values    
    #date_HISTORIQUE = df_HISTORIQUE.index.values
    #print (date_HISTORIQUE)
    df_HISTORIQUE.index = pd.to_datetime(df_HISTORIQUE.index)
    print(df_HISTORIQUE.index)
    
if __name__ == "__main__":
    #clear_cache()                  #Exemple01
    yfinance("RNO.PA")              #Execution
    #yfinance_beta("RNO.PA")        #Fonction d'essais.
