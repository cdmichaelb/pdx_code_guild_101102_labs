"""
programming 101
->Lab 02
09/28/21
Michael B
"""

# Not entirely sure if this is done correctly, but it functions.
# The while loops below would not work unless I defined them first.
madlib_quit = ""
madlib_adjective_words = ""
madlib_noun_word = ""
madlib_scifi_word = ""
madlib_plant_name = ""

while (
    madlib_quit != "yes"
):  # Loops whole program until yes is responded to the quit message.

    while madlib_noun_word == "":  # Loops to prevent no response.
        madlib_noun_word = input("Please enter a noun: ")
    while len(madlib_adjective_words) < 2:  # Loops to ensure two adjectives.
        madlib_adjective_words = input("Please enter two adjective words: ").split(
            ",", 2
        )
    while madlib_scifi_word == "":  # Loops to prevent no response.
        madlib_scifi_word = input("Please enter a scifi word: ")
    while madlib_plant_name == "":  # Loops to prevent no response.
        madlib_plant_name = input("Please enter a plant name: ")

    # Formated multi-line string for the madlib story.
    output = f"""
    This is a story about {madlib_noun_word} he has a {madlib_scifi_word}.
    A {madlib_scifi_word.title()} is used to cultivate the growth of {madlib_adjective_words[0].strip().lower()} {madlib_plant_name.title()}.
    {madlib_noun_word.title()} likes {madlib_adjective_words[1].strip().lower()} {madlib_plant_name.title()} though.
    """

    print(output)  # Prints the story.

    madlib_quit = input(
        "Do you want to quit the program? (yes or no): "
    )  # Asks user if they want to quit.
