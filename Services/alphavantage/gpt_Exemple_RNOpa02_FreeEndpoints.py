#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#AIDES: https://chatgpt.com/share/6893c1c4-0a14-800d-8559-ede4b8456e69
#AIDES: https://www.alphavantage.co/documentation/#daily
#INFOS: Welcome to Alpha Vantage! Your API key is: LH5A8N8S9K9XQSYJ. Please record this API key at a safe place for future data access.
#------

import pandas as pd
import requests
import time

# === Paramètres ===
api_key = "LH5A8N8S9K9XQSYJ"
symbol = "RNO.PA"
url = f"https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "outputsize": "compact",  # ou "full" si tu veux l'historique complet
    "apikey": api_key
}

# === Requête API ===
response = requests.get(url, params=params)
data = response.json()

# === Extraction des données ===
if "Time Series (Daily)" not in data:
    print("Erreur API :")
    print(data)
    exit()

raw_timeseries = data["Time Series (Daily)"]
df = pd.DataFrame.from_dict(raw_timeseries, orient="index")
df = df.rename(columns={
    "1. open": "Open",
    "2. high": "High",
    "3. low": "Low",
    "4. close": "Close",
    "5. adjusted close": "Adj Close",
    "6. volume": "Volume"
})

# On convertit l'index en datetime pour tri + on trie du plus ancien au plus récent
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# On ne garde que les colonnes demandées (hauts, bas, cours actuel)
df = df[["Low", "Close", "High"]].astype(float)

# === Aperçu des 5 derniers jours (modifiable selon besoin) ===
print("\n📊 Derniers jours (prix bas, actuel, haut) pour Renault (RNO.PA) :\n")
print(df.tail())

# === Export CSV facultatif ===
df.to_csv("renault_prix_daily.csv")
exit()
