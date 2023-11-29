import unittest
from unittest.mock import patch
from hangman.game import choose_word, display_word, take_guess, hangman

class TestGame(unittest.TestCase):
    def test_choose_word(self):
        # Test that choose_word returns a non-empty string
        word = choose_word()
        self.assertIsInstance(word, str, "Chosen word should be a string.")
        self.assertGreater(len(word), 0, "Chosen word should not be empty.")

    def test_display_word(self):
        # Test that display_word returns a string with underscores for unguessed letters
        secret_word = "python"
        guessed_letters = ["p", "t"]
        displayed = display_word(secret_word, guessed_letters)
        self.assertEqual(displayed, "p _ t _ _ _", "Displayed word should show guessed letters and underscores.")

    @patch("builtins.input", side_effect=["a"])
    def test_take_guess_valid_entry(self, mock_input):
        # Test that take_guess returns a lowercase letter
        guess = take_guess()
        self.assertIsInstance(guess, str, "Guess should be a single lowercase letter.")
        self.assertTrue(guess.isalpha(), "Guess should be a single lowercase letter.")
        self.assertEqual(len(guess), 1, "Guess should be a single lowercase letter.")
        
    @patch("builtins.input", side_effect=["1"])
    def test_take_guess_invalid_entry(self, mock_input):
        # TODO: Add test that take_guess rejects invalid input
        pass

    def test_hangman_win(self):
        # TODO: Add test that hangman function works when player wins
        pass

    def test_hangman_loss(self):
        # TODO: Add test that hangman function works when player loses
        pass

    # TODO: Add more tests as needed for other functions and scenarios
