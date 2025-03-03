import random

# Dictionary of words by category
hang_dict = {
    "science": ["Gravity", "Molecule", "Exoplanet", "Astronomy"],
    "tech": ["Algorithm", "Database", "Programming", "Quantum", "Processor"],
    "games": ["Dungeon", "Strategy", "Adventure", "Spell", "Creativity"],
    "sport": ["Marathon", "Athletic", "Olympic", "Medals", "Competition"],
    "nature": ["Ecosystem", "Degradation", "Environment", "Sustainability", "Ecology"]
}

category_list = list(hang_dict.keys())  # Ensure it matches the keys


def category_menu():
    print("Welcome to the Hangman Game!")

    while True:
        print("\nChoose a category:")
        for category in category_list:
            print(f"- {category.capitalize()}")

        user_category = input("\nYour choice: ").strip().lower()
        if user_category in category_list:
            print(f"You chose: {user_category.capitalize()}\n")
            return user_category
        else:
            print("Invalid category. Please try again.")


def difficulty_menu():
    while True:
        try:
            dif_level = int(input(
                "Choose the difficulty level:\n1 - Easy (8 mistakes allowed)\n2 - Medium (6 mistakes)\n3 - Hard (3 mistakes)\n\nYour choice: "))
            if dif_level in [1, 2, 3]:
                attempts = {1: 8,  # Making a dictionary which transforms each difficulty level in a key, and relates it to the respective number of attempts.
                            2: 6,
                            3: 3}[dif_level]
                print(f"You selected difficulty {dif_level}. You have {attempts} incorrect attempts allowed.\n")
                return attempts
            else:
                print("Invalid input. Choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")


def game(win_word, attempts):
    hidden_word = []
    for l in win_word:
        hidden_word.append("_")
    attempts_left = attempts
    guessed_letters = set()  # A different kind of list to automatically remove duplicates.

    print("\nLet's start!")

    while attempts_left > 0 and "_" in hidden_word:  # While the user still has attempts and at the same time in hidden_word there is still "_", the game will keep running.
        print("\nCurrent word:", " ".join(hidden_word))  # Adding spaces between each letter, and joining all list values in a word again.
        print(f"Attempts left: {attempts_left}")
        if guessed_letters:  # If guessed_letters set is not empty
            print(f"Guessed letters: {', '.join(guessed_letters)}")
        else:
            print("Guessed letters: None")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():  # Allow the user to only input one letter at a time, and guarantee that only will be on the alphabet.
            print("Invalid input. Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)  # .add works to insert new data into a set()

        if guess in win_word:
            print("Good guess!")
            for i, letter in enumerate(win_word):  # Enumerate combines each letter and its respective index. "i" being the index and "letter", each letter of the win_word.
                if letter == guess:
                    hidden_word[i] = guess  # Here is where the substitution of the "_" for the input letter guess occurs.
        else:
            print("Wrong guess!")
            attempts_left -= 1  # Subtract one every time the user guesses wrongly.

    if "_" not in hidden_word:
        print("\nCongratulations! You guessed the word:", "".join(hidden_word))
    else:
        print(f"\nGame Over! The word was: {''.join(win_word)}")


def end_game():
    while True:
        end = input("To close the game type:  exit  \nTo play again:  go  ").strip().lower()
        if end == "go":
            return True  # Return True to continue the game
        elif end == "exit":
            print("Game closed! See you later!")
            return False  # Return False to stop the game
        else:
            print("Invalid input, if you want to close type 'exit'.")