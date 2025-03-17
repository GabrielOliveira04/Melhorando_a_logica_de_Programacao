import requests

API_KEY = "fca_live_KKGejJDCHynUg3MilHALSuBZLDR2HpHbz3Dbs6Si"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "BRL"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None

while True:
    base = input("Enter the base currency (q para quit) :").upper()
    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticket, value in data.items():
        print(f"{ticket} : {round(value, 2)} ")        
