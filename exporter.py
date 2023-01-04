import requests
from prometheus_client import start_http_server, Gauge

# Constants
API_URL = 'https://api.coingecko.com/api/v3/coins'

# Create Prometheus metrics

current_price = Gauge('current_price', 'Current price of the coin', ['coin_name'])
high = Gauge('high', 'High price of the coin', ['coin_name'])
low = Gauge('low', 'Low price of the coin', ['coin_name'])

# Start the HTTP server for Prometheus
start_http_server(8000)

while True:
  # Set up the request parameters
  params = {
    'per_page': '100',
    'order': 'market_cap_desc',
  }

  # Get the current market data from CoinGecko
  response = requests.get(API_URL, params=params).json()
  for coin in response:
    # Set the values for the current coin
    if isinstance(coin, dict):
        current_price.labels(coin['name']).set(coin['market_data']['current_price']['usd'])
        high.labels(coin['name']).set(coin['market_data']['high_24h']['usd'])
        low.labels(coin['name']).set(coin['market_data']['low_24h']['usd'])




