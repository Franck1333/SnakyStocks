import yfinance as yf
import pandas as pd
from alpha_vantage.techindicators import TechIndicators

# --- 1. RÉCUPÉRATION DES DONNÉES DE BASE VIA YFINANCE ---
# Ticker Yahoo Finance pour Renault : RNO.PA
ticker = yf.Ticker("RNO.PA")

# Historique des prix (1 an par défaut, données quotidiennes)
df_prices = ticker.history(period="1y", interval="1d")
df_prices.reset_index(inplace=True)

# Informations fondamentales de Renault (format dictionnaire → DataFrame)
info = pd.DataFrame([ticker.info])

# --- 2. INDICATEURS TECHNIQUES AVEC ALPHA VANTAGE ---
# Insérer ici ta clé API Alpha Vantage (gratuite à obtenir sur https://www.alphavantage.co)
API_KEY = "LH5A8N8S9K9XQSYJ"

ti = TechIndicators(key=API_KEY, output_format='pandas')

# Exemple : Indicateur RSI (Relative Strength Index) sur 14 jours
df_rsi, _ = ti.get_rsi(symbol="RNO.PA", interval='daily', time_period=14, series_type='close')

# Exemple : MACD
#df_macd, _ = ti.get_macd(symbol="RNO.PA", interval='daily', series_type='close')

# Fusion des indicateurs techniques avec l’historique des prix
df_combined = df_prices.join(df_rsi, how='left')
#df_combined = df_combined.join(df_macd, how='left')

# --- 3. STRUCTURATION FINALE POUR EXPLOITATION EN 2D ---
# On sélectionne quelques colonnes utiles pour la suite
#df_final = df_combined[[
#    "Date", "Open", "High", "Low", "Close", "Volume",
#    "RSI", "MACD", "MACD_Signal", "MACD_Hist"
#]]
df_final = df_combined[[
    "Date", "Open", "High", "Low", "Close", "Volume",
    "RSI"
]]
# Nettoyage (par sécurité)
df_final.dropna(inplace=True)

# --- 4. EXPORT OPTIONNEL ---
# Tu peux exporter vers CSV pour une exploitation dans Excel ou un notebook ultérieur
df_final.to_csv("renault_data.csv", index=False)

# --- 5. APERCU RAPIDE ---
print(df_final.head())
