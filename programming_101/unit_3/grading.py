import random  # Imported the random library.

# Define variables so they are valid.
grading_try_again = True
grading_numerical_grade = ""

# Easier to use a function to reuse code, rather than write all this code twice once for user and once for rival.
def grading_calculate_grade(score) -> str:
    if (
        score >= 90 and score <= 100
    ):  # Greater than or equal to 90, but lesser than or equal to 100.
        grading_letter_grade = "A"
    elif (
        score >= 80 and score <= 90
    ):  # Greater than or equal to 90, but lesser than or equal to 100.
        grading_letter_grade = "B"
    if (
        score >= 70 and score <= 80
    ):  # Greater than or equal to 90, but lesser than or equal to 100.
        grading_letter_grade = "C"
    elif (
        score >= 60 and score <= 70
    ):  # Greater than or equal to 90, but lesser than or equal to 100.
        grading_letter_grade = "D"
    elif score >= 0 and score < 60:  # Less than 60 but higher than 0 is failure.
        grading_letter_grade = "F"
    else:
        print(
            "You did not enter a valid numerical grade."
        )  # Number > 100 or < 0, or not a number.

    grading_modulus = score % 10
    if grading_letter_grade == "F":  # Grade of F does not have a - or + typically.
        grading_modulus_symbol = ""
    elif grading_modulus >= 5:  # High letter grade.
        grading_modulus_symbol = "+"
    elif grading_modulus <= 5:  # Low letter grade.
        grading_modulus_symbol = "-"
    elif grading_modulus == 5:  # Even letter grade.
        grading_modulus_symbol = ""
    score_result = (
        grading_letter_grade + grading_modulus_symbol
    )  # Combined letter grade with grade modifier.

    return score_result  # Returns the result to be used.


# Loop if the user wants to try again.
while grading_try_again == True:
    grading_rival_score = random.randint(
        0, 100
    )  # Randomize the rival's numerical grade.

    while (
        grading_numerical_grade == ""
        or grading_numerical_grade > 100
        or grading_numerical_grade < 0
    ):  # Loop until user enters something.
        grading_numerical_grade = input("Please enter your numerical grade: ")
        # Todo: Check if input is int. Loop if not.
        grading_numerical_grade = int(
            grading_numerical_grade
        )  # Convert users input to an int.

    grading_user_grade = grading_calculate_grade(
        grading_numerical_grade
    )  # Use above defined function to calc user grade.
    grading_rival_grade = grading_calculate_grade(
        grading_rival_score
    )  # Use above defined function to calc rival grade.

    # Compare user to rival.
    if grading_numerical_grade >= grading_rival_score:  # User is better than rival.
        grading_output = f"""Your grade is {grading_user_grade} ({grading_numerical_grade}%). 
    Your rival had a {grading_rival_grade} ({grading_rival_score}%).
    You beat your rival!"""
    elif grading_numerical_grade <= grading_rival_score:  # Rival is better than user.
        grading_output = f"""Your grade is {grading_user_grade} ({grading_numerical_grade}%). 
    Your rival had a {grading_rival_grade} ({grading_rival_score}%).
    Your rival beat you."""
    else:  # User and rival tie.
        grading_output = f"""Your grade is {grading_user_grade} ({grading_numerical_grade}%). 
    Your rival had a {grading_rival_grade} ({grading_rival_score}%).
    You both tied."""

    print(grading_output)  # Print output.

    # Check if user wants to try again and reset variables.
    grading_try_again = input("Do you want to run again? (y/n): ")
    if "y" in grading_try_again:
        grading_try_again = True
        grading_numerical_grade = ""


"""
Example output:

Please enter your numerical grade: 3
Your grade is F (3%). 
    Your rival had a F (7%).
    Your rival beat you.
Do you want to run again? (y/n): n

"""
