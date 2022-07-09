"""
programming 101
->Lab 05
10/01/21
Michael Broetje
"""
# Imports
import random
import string

# Tables
pwg_yes_no = ["yes", "no", "y", "n"]  # Valid Answers

pwg_letters, pwg_numbers, pwg_puncutation = (
    string.ascii_letters,
    string.digits,
    string.punctuation,
)  # Table of letters, digits, and punctuation.
pwg_all_chars = (
    pwg_puncutation + pwg_letters + pwg_numbers
)  # Table combining all char tables.

# Variables
(
    pwg_try_again,
    pwg_new_pass,
    pwg_password,
    pwg_characters,
    pwg_compiled_password,
    pwg_customize,
    pwg_custom_letters,
    pwg_custom_numbers,
    pwg_custom_symbols,
) = (True, "", [], "", "", "", "", "", "")

# Functions
def pwg_create_password_list(
    pwg_chars, pwg_len
):  # Create list of characters for password.
    pwg_fun_password = []
    while len(pwg_fun_password) <= int(pwg_len) - 1:
        pwg_fun_password.append(random.choice(pwg_chars))
    return pwg_fun_password


def pwg_question(question_string):  # Ask user a number question.
    pwg_question_chars = ""
    while (
        pwg_question_chars == ""
        or pwg_question_chars == "0"
        or not pwg_question_chars.isdigit()
    ):
        pwg_question_chars = input(
            f"""How many {question_string} do you want to use for your password?
> """
        )
    return pwg_question_chars


# Main Loop
while pwg_try_again == True:  # Run while user wants to create new passwords.
    while (
        pwg_customize == "" or not pwg_customize.lower() in pwg_yes_no
    ):  # Ask if user wants to customize password.
        pwg_customize = input(
            f"""Do you want to customize your password?
> """
        )
    print("")  # Spacing for formating.
    if (
        pwg_customize == "no" or pwg_customize == "n"
    ):  # User does not want to customize.
        pwg_characters = pwg_question("characters")  # Use function to gather input.
        pwg_password = pwg_create_password_list(
            pwg_all_chars, pwg_characters
        )  # Use function to create password using characters.
        random.shuffle(
            pwg_password
        )  # Randomize created password. Not neccisary here, but why not.

    else:  # User wants to customize.
        pwg_custom_letters = pwg_question("letters")  # Use function to gather input.
        pwg_custom_numbers = pwg_question("numbers")  # Use function to gather input.
        pwg_custom_symbols = pwg_question("symbols")  # Use function to gather input.
        pwg_password = (
            pwg_create_password_list(pwg_letters, pwg_custom_letters)
            + pwg_create_password_list(pwg_numbers, pwg_custom_numbers)
            + pwg_create_password_list(pwg_puncutation, pwg_custom_symbols)
        )  # Use function to create password using characters.
        random.shuffle(pwg_password)  # Randomize created password.

    """Compile Password"""
    for i in range(len(pwg_password)):
        pwg_compiled_password = (
            pwg_compiled_password + pwg_password[i]
        )  # Take password from a list to a string.

    print(
        f"""
Here is your password: {pwg_compiled_password}"""
    )  # Print password

    # Ask if user wants to create a new password.
    while not pwg_new_pass.lower() in pwg_yes_no:  # Check answer is valid.
        pwg_new_pass = input(
            f"""
Create another password? (Yes or No)
> """
        )
    if (
        pwg_new_pass.lower() == "no" or pwg_new_pass.lower() == "n"
    ):  # User does not want a new password, quit.
        pwg_try_again = False
    elif (
        pwg_new_pass.lower() == "yes" or pwg_new_pass.lower() == "y"
    ):  # User wants a new password. Sanitize variables and tables.
        (
            pwg_try_again,
            pwg_new_pass,
            pwg_password,
            pwg_characters,
            pwg_compiled_password,
            pwg_customize,
            pwg_custom_letters,
            pwg_custom_numbers,
            pwg_custom_symbols,
        ) = (True, "", [], "", "", "", "", "", "")
