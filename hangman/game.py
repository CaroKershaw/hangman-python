import random
from typing import List

from hangman import words

def choose_word() -> str:
    word_list = words.get_word_list()  # TODO Check the words module was imported correctly
    return random.choice(word_list)

def display_word(secret_word: str, guessed_letters: List[str]) -> str:
    pass  # TODO: Implement a function to display the word with underscores for unguessed letters

def take_guess() -> str:
    pass  # TODO: Implement a function to take a user's guess

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = take_guess()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts_left -= 1
            print("Incorrect guess! Try again.")
        else:
            print("Correct guess!")

        if set(guessed_letters) >= set(secret_word):
            print("Congratulations! You guessed the word!")
            break

    else:
        print(f"Sorry, you're out of attempts. The word was {secret_word}.")

if __name__ == "__main__":
    hangman()