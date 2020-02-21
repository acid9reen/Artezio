'''Password regexp'''

import re


def main():
    '''Password regexp'''

    password = input("Enter the password: ")
    reg = r"^(?=.*[a-z])(?=.*[_*%&])(?=.*\d)(?=.*[A-Z])[A-Za-z\d_*%&]{8,12}$"

    pattern = re.compile(reg)
    match = re.search(pattern, password)

    if match:
        print("Password is valid.")
    else:
        print("Invalid password.")


if __name__ == '__main__':
    main()
