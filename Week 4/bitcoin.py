import sys
import json
import requests

if len(sys.argv) == 2:
    try:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Non-numeric Argument")

        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ef51bfeaeab6c471522779228e41b73652f6651cdef0d5a854216a1ee5e06f81").json()

        bitcoin_price = float(response["data"]["priceUsd"])

        result = bitcoin_price * n

        print(f"${result:,.4f}")

    except requests.RequestException:
        sys.exit()

else:
    sys.exit("Missing command-line argument")


