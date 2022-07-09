"""Imports"""
import random

"""Variables"""
rps_player_move, rps_run_once, rps_try_again, rps_try_again_answer = "", 0, True, ""

"""Tables / Dictionaries"""
rps_winning_games = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}  # Dictionary of winning game states.
rps_valid_moves = ["rock", "paper", "scissors"]  # List of valid moves.
rps_valid_try_again = ["yes", "no"]  # List of valid quit answers.

"""Strings"""
rps_intro_string = f"""
Welcome to Rock, Paper, Scissors!

Your options are:

- Rock
- Paper
- Scissors

Enter your selection:
> """
rps_invalid_string = f"""
Invalid Selection. Try again.
> """

"""Code"""
while rps_try_again == True:  # Loop as long as player wants to keep playing.
    rps_computer_move = random.choice(rps_valid_moves)  # Randomize computer move.

    while (
        not rps_player_move.lower() in rps_valid_moves
    ):  # Check if player entered a valid move.
        if rps_run_once == 0:  # First time ask for a move.
            rps_player_move = input(rps_intro_string)
        else:  # Player entered an invlid move, alert and ask again.
            rps_player_move = input(rps_invalid_string)
        rps_run_once = +1

    print(
        f"""
You picked {rps_player_move.lower()}.
Computer picked {rps_computer_move}."""
    )  # Generic statement printed for each of the game states.
    if rps_player_move.lower() == rps_computer_move:  # Game is a tie.
        print(f"""The game is a tie.""")
    elif (
        rps_player_move.lower() in rps_winning_games
        and rps_winning_games[rps_player_move.lower()] == rps_computer_move
    ):  # Game is a win.
        print(f"""You Win!""")
    else:  # Game is a loss.
        print(f"""You lose.""")

    while (
        not rps_try_again_answer.lower() in rps_valid_try_again
    ):  # Ask if player wants to play again.
        rps_try_again_answer = input(
            f"""
Try again? (Yes or No)
> """
        )
    if rps_try_again_answer.lower() == "no":
        rps_try_again = False
    elif (
        rps_try_again_answer.lower() == "yes"
    ):  # Player wants to play again, reset game variables.
        rps_try_again_answer, rps_player_move, rps_run_once = "", "", 0
