#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import requests
import sys

# === Paramètres ===
API_KEY = "LH5A8N8S9K9XQSYJ"
SYMBOL = "RNO.PA"
URL = "https://www.alphavantage.co/query"


def get_stock_data(symbol, api_key):
    """Récupère les données brutes de l'API Alpha Vantage."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact", #ou full
        "apikey": api_key
    }
    response = requests.get(URL, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print("Erreur API :", data)
        sys.exit(1)

    return data["Time Series (Daily)"]


def process_data(raw_timeseries):
    """Transforme les données brutes en DataFrame trié."""
    df = pd.DataFrame.from_dict(raw_timeseries, orient="index")
    df = df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. adjusted close": "Adj Close",
        "6. volume": "Volume"
    })

    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df[["Open", "Low", "High", "Close"]].astype(float)

    return df


def display_data(df, days=5):
    """Affiche les dernières données."""
    print(f"\n📊 Derniers {days} jours pour ({SYMBOL}) :\n")
    print(df.tail(days))


def save_to_csv(df, filename="renault_prix_daily.csv"):
    """Exporte les données en CSV."""
    df.to_csv(filename)
    print(f"\n✅ Données exportées dans {filename}")


if __name__ == "__main__":
    raw_data = get_stock_data(SYMBOL, API_KEY)
    df = process_data(raw_data)
    display_data(df, days=5)
    save_to_csv(df)
