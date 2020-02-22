'''Password regexp'''

import re


def main():
    '''Password regexp'''

    password = input("Enter the sentence: ")
    reg = r"\b(\w+).+\1\b.+\1\b.+\1\b\.$"

    pattern = re.compile(reg, re.IGNORECASE)
    match = re.search(pattern, password)

    if match:
        print("Sentence is interrogative.")
    else:
        print("Sentence isn't interrogative.")


if __name__ == '__main__':
    main()
