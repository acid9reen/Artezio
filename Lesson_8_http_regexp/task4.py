'''Date time regexp'''

import re


def main():
    '''Date time regexp'''

    date_time = input("Enter the date time: ")
    reg = r"\d{4}-([0]\d|1[0-2])-([0-2]\d|3[01])T" \
          r"([0-1]\d|2[0-3]):[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z)"

    pattern = re.compile(reg)
    match = re.search(pattern, date_time)

    if match:
        print("Date time is valid.")
    else:
        print("Invalid date time.")


if __name__ == '__main__':
    main()
