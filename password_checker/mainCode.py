import getpass
from data import minSymbol_count, minDigits_count, minUpperCase_count, minLetters_count

# this is the my code but chatgpt cleaned it


def passwordStrengthChecker(text):
    if not text:
        return "Error: no password was found"

    letter_count = sum(1 for char in text if char.isalpha())
    uppercase_count = sum(1 for char in text if char.isupper())
    digit_count = sum(1 for char in text if char.isdigit())
    symbol_count = sum(1 for char in text if not char.isalnum())

    if (
        symbol_count >= minSymbol_count and
        digit_count >= minDigits_count and
        uppercase_count >= minUpperCase_count and
        letter_count >= minLetters_count
    ):
        return "Strong Password"

    if digit_count >= 2 and uppercase_count >= 1 and letter_count >= 5:
        return "Acceptable password"

    return "Weak Password"


# Use getpass if you want hidden input (for security), or input() for testing
password = getpass.getpass("Your Password: ")
print(passwordStrengthChecker(password))
# my code
# import getpass

# from data import minSymbol_count, minDigits_count, minUpperCase_count, minLetters_count

# password = input("Your Password:")


# def passwordisNotEmpty(string):
#     if string:
#         return string
#     return None


# def passwordStrengthChecker(text):
#     if passwordisNotEmpty(text):
#         letter_count = sum(1 for char in text if char.isalpha())
#         uppercase_count = sum(1 for char in text if char.isupper())
#         digit_count = sum(1 for char in text if char.isdigit())
#         symbol_count = sum(1 for char in text if not char.isalnum())
#         if symbol_count >= minSymbol_count and digit_count >= minDigits_count and uppercase_count >= minUpperCase_count and letter_count >= minLetters_count:
#             return "Strong Password"
#         if digit_count >= 2 and uppercase_count >= 1 and letter_count >= 5:
#             return "Acceptable password"
#         else:
#             return "Weak Password"
#     return "Error:no password was found"


# print(passwordStrengthChecker(password))
