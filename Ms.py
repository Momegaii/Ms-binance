import requests
import time
from binance.client import Client

# Replace with your Binance API key and secret
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Initialize the Binance client
client = Client(api_key, api_secret)

# Define the transfer parameters
asset = 'USDT'  # The asset you want to transfer (e.g., USDT)
amount = 100     # The amount to transfer
from_wallet = 'SPOT'  # From Spot wallet
to_wallet = 'FUNDING'  # To Funding wallet

# Binance API endpoint for wallet transfer
url = 'https://api.binance.com/sapi/v1/funding/transfer'

# Set up parameters for the transfer
params = {
    'asset': asset,
    'amount': amount,
    'type': 'SPOT_TO_FUNDING',  # 'SPOT_TO_FUNDING' or 'FUNDING_TO_SPOT'
    'timestamp': int(time.time() * 1000)  # Get current timestamp in milliseconds
}

# Sign the request
params['signature'] = client._get_signature(params)

# Perform the transfer via API call
try:
    response = requests.post(url, params=params, headers={'X-MBX-APIKEY': api_key})
    data = response.json()
    if response.status_code == 200:
        print(f"Transfer successful: {data}")
    else:
        print(f"Error during transfer: {data}")
except Exception as e:
    print(f"Error during transfer: {e}")
