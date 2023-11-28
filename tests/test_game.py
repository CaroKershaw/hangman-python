import unittest
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
        self.assertEqual(displayed, "p _ _ t _ _", "Displayed word should show guessed letters and underscores.")

    def test_take_guess(self):
        # Test that take_guess returns a lowercase letter
        guess = take_guess()
        self.assertIsInstance(guess, str, "Guess should be a string.")
        self.assertTrue(guess.isalpha(), "Guess should be a letter.")
        self.assertEqual(len(guess), 1, "Guess should be a single letter.")

    def test_hangman_win(self):
        # Test that hangman function works when player wins
        # In this case, the secret word is "python" and all letters are guessed
        with unittest.mock.patch("builtins.input", side_effect=["p", "y", "t", "h", "o", "n"]):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            hangman()
            sys.stdout = sys.__stdout__
            self.assertIn("Congratulations! You guessed the word!", captured_output.getvalue(), "Player should win.")

    def test_hangman_loss(self):
        # Test that hangman function works when player loses
        # In this case, the secret word is "python" and no correct letters are guessed
        with unittest.mock.patch("builtins.input", side_effect=["a", "b", "c", "d", "e", "f"]):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            hangman()
            sys.stdout = sys.__stdout__
            self.assertIn("Sorry, you're out of attempts. The word was python.", captured_output.getvalue(), "Player should lose.")

    # TODO: Add more tests as needed for other functions and scenarios
