import requests
import sys


def main():
    n = get_n()
    price = get_bitcoin()
    final = n * price
    final = round(final, 4)
    print(final)


def get_bitcoin():
    try:
        response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
        response.raise_for_status()
    except requests.RequestException:
        print("Error fetching bitcoin price")
        return None
    except ValueError:
        print("Error: invalid JSON response")
    data = response.json()
    price = data["quotes"]["USD"]["price"]
    return price


def get_n():

    try:
        n = float(sys.argv[1])
        return n
    except (ValueError, IndexError):
        sys.exit("Error: please enter a number")


main()
