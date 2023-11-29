import random
from typing import List
from hangman import words


def choose_word() -> str:
    word_list = (
        words.get_word_list()
    )  # TODO Check the words module was imported correctly
    return random.choice(word_list)


def display_word(secret_word: str, guessed_letters: List[str]) -> str:
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def take_guess() -> str:
    while True:
        guess = input("Enter your guess (a single lowercase letter): ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single lowercase letter.")


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
