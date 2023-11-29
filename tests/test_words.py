import unittest
from hangman.words import get_word_list


class TestWords(unittest.TestCase):
    def test_get_word_list(self):
        # Test that get_word_list returns a non-empty list of words
        # Arrange & Act
        word_list = get_word_list()

        # Assert
        self.assertIsInstance(word_list, list, "Word list should be a list.")
        self.assertGreater(len(word_list), 0, "Word list should not be empty.")
