import json
import requests
import sys

def cline():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

try:
    cline()

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    rate = r.json()["bpi"] ["USD"] ['rate_float']
    bc = rate * float(sys.argv[1])

    print(f"${bc:,.4f}")

except requests.RequestException:
    sys.exit()