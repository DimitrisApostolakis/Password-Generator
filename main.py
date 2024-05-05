import string
import secrets


def passwordGenerator(given_length):
    filtered_symbols = "!#@*&_"
    random_output = "".join(
        secrets.choice(string.ascii_letters + string.digits + filtered_symbols) for _ in range(given_length))
    return random_output


while True:
    try:
        length = int(input("Choose the length of the password: "))
        if not 8 <= length <= 32:
            print("Please provide an number between 8 - 32!")
            continue
        else:
            print(passwordGenerator(length))
            break
    except ValueError:
        print("Please provide an integer number!")
        continue
