import requests
import time

def get_btc_mxn_price():
    url = "https://api.bitso.com/v3/ticker/?book=btc_mxn"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            price = data['payload']['last']
            print("Current price of BTC/MXN:", price)
        else:
            print("Failed to retrieve price information:", data['error']['message'])
    else:
        print("Failed to retrieve price information. Status code:", response.status_code)

# Set the refresh interval (in seconds)
refresh_interval = 10  # Change this value as needed

while True:
    get_btc_mxn_price()
    time.sleep(refresh_interval)