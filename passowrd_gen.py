from random import sample
from random import shuffle

def password_generator():
    capital_letters = [chr(x) for x in range(65,91)]
    small_letters =[chr(x) for x in range(97,123)]
    capital_letters.extend(small_letters)
    numbers = [str(x) for x in range(0,10)]
    symbols = ["+", "-", "?" , "$", "!", "%", "*"]

    while True:
        while True:
            length_password = input("Enter the length of the password: ")

            try:
                int(length_password)
                if int(length_password) < 6:
                    print("value cannot be less than six")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")

        while True:
            numbers_of_letters = input("Enter the numbers of letter you want in your password:" )
            try:
                int(numbers_of_letters)
                if int(numbers_of_letters) < 0:
                    print("value cannot be less than zero")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")

        while True:
            numbers_digits = input("Enter the numbers of digits you want in your password: ")
            try:
                int(numbers_digits)
                if int(numbers_digits) < 0:
                    print("value cannot be less than zero")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")

        while True:
            numbers_of_symbols = input("Enter the numbers of symbol you want in your password: ")
            try:
                int(numbers_of_symbols)
                if int(numbers_of_symbols) < 0:
                    print("value cannot be less than zero")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")

        if (int(numbers_digits) + int(numbers_of_letters) + int(numbers_of_symbols) == int(length_password)):
            letters = sample(capital_letters, int(numbers_of_letters))
            digits = sample(numbers, int(numbers_digits))
            special_characters = sample(symbols, int(numbers_of_symbols))

            letters.extend(digits)
            letters.extend(special_characters)
            shuffle(letters)
            return "".join(letters)
            break

        return 'sum of numbers_digits, numbers_of_letters and numbers_of_symbol must be equal to lenght of password'
print(password_generator())

