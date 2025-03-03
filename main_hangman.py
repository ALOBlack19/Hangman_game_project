from functions_hangman import *

while True:
    user_category = category_menu()
    attempts = difficulty_menu()
    round_word = list(random.choice(hang_dict[user_category]).lower())
    game(round_word, attempts)

    # Ask if the player wants to play again or exit
    if not end_game():
        break  # If the user chooses to exit, break out of the loop and end the game.

#This file runs the game

