'''Convert currency from one to another'''

import requests


def converter(amount: float, from_curr: str, to_curr: str) -> float:
    '''Convert currency from one to another'''

    url = 'https://api.exchangerate-api.com/v4/latest/' \
          + from_curr

    response = requests.get(url)
    data = response.json()

    result = amount * data["rates"][to_curr]

    return result


def main():
    '''Call converter function with user amount value'''

    amount = int(input("Enter the amount to convert from USD to RUB: "))
    print(f'{converter(amount, "USD", "RUB"):.2f}')


if __name__ == '__main__':
    main()
