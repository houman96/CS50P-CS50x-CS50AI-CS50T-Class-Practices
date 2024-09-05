import sys
import requests
import json


if len(sys.argv) == 2:
    try:
        if float(sys.argv[1]):
            money = sys.argv[1]
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = req.json()
usd = data["bpi"]["USD"]["rate_float"]
result = float(usd) * float(money)
print(money)
print(f"${result:,.4f}")
