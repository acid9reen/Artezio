import requests


def main():
    r = requests.get("https://google.com")
    print(len(r.text))


if __name__ == '__main__':
    main()
