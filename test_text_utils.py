import unittest
from text_utils import reverse_string, count_vowels, is_palindrome, get_word_frequencies, replace_word


class TestTextUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(123), "Error: Input is not a string.")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels(123), "Error: Input is not a string.")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome(123))

    def test_get_word_frequencies(self):
        self.assertEqual(get_word_frequencies("hello hello world"), {'hello': 2, 'world': 1})
        self.assertEqual(get_word_frequencies(123), "Error: Input is not a string.")

    def test_replace_word(self):
        self.assertEqual(replace_word("hello world", "world", "universe"), "hello universe")
        self.assertEqual(replace_word("hello world", 123, "universe"), "Error: Words to replace must be strings.")
        self.assertEqual(replace_word(123, "hello", "world"), "Error: Input is not a string.")


if __name__ == '__main__':
    unittest.main()
