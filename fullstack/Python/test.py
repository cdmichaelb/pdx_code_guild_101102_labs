def check_anagram(list_to_check) -> bool:
    sorted_strings = []
    for ana_string in list_to_check:  # Move through the list of strings.
        ana_string = list(ana_string)  # Convert string to a list.
        ana_string.sort()  # Sort the list by alphabetical order.
        sorted_strings.append("".join(ana_string))  # Convert list back to string
    for check_string in range(len(sorted_strings)):  # Check each sorted string.
        if (
            not sorted_strings[check_string] == sorted_strings[check_string - 1]
        ):  # If current string being checked does not match previous string then not anagram.
            return False
    return True


def get_list_of_words() -> list:
    while True:
        list_to_check = (
            input("\nPlease enter a list of words separated by a comma.\n")
            .lower()
            .split(",")
        )  # Get list of words from user.
        if (
            len(list_to_check) < 2
        ):  # If user doesn't enter at least 2 words then they must enter again.
            print(
                "You must enter at least 2 words separated by a comma. Please try again.\n"
            )
            continue
        else:
            break
    return list_to_check


if __name__ == "__main__":
    list_to_check = get_list_of_words()
    if check_anagram(list_to_check):
        print(f"Your words {list_to_check} are an anagram!")
    else:
        print(f"Your words {list_to_check} are not an anagram!")
    print("\ngoodbye")  # Tell user goodbye.pyth
