import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_true_palindromes(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_sentence_palindrome("Madam In Eden, I’m Adam"))
        self.assertTrue(is_sentence_palindrome("Able was I, I saw Elba"))
        self.assertTrue(is_sentence_palindrome(""))

    def test_false_palindromes(self):
        self.assertFalse(is_sentence_palindrome("Hello, world!"))
        self.assertFalse(is_sentence_palindrome("Python is fun"))
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))

    def test_single_character(self):
        self.assertTrue(is_sentence_palindrome("a"))
        self.assertTrue(is_sentence_palindrome("Z"))

    def test_numbers_and_letters(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))
        self.assertTrue(is_sentence_palindrome("1a2b2a1"))

if __name__ == "__main__":
    unittest.main()