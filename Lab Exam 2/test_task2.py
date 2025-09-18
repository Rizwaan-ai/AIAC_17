import pytest
from task2 import slugify

class TestSlugify:
    """Test cases for the slugify function."""
    
    def test_basic_slugify(self):
        """Test basic slugify functionality."""
        text = "Hello World"
        expected = "hello-world"
        assert slugify(text) == expected
    
    def test_special_characters(self):
        """Test removal of special characters."""
        text = "AI & You!"
        expected = "ai-you"
        assert slugify(text) == expected
    
    def test_numbers_and_hyphens(self):
        """Test preservation of numbers and existing hyphens."""
        text = "Set13-C2"
        expected = "set13-c2"
        assert slugify(text) == expected
    
    def test_multiple_spaces(self):
        """Test handling of multiple spaces."""
        text = "Hello    World   Test"
        expected = "hello-world-test"
        assert slugify(text) == expected
    
    def test_multiple_hyphens(self):
        """Test collapsing of multiple hyphens."""
        text = "Hello--World---Test"
        expected = "hello-world-test"
        assert slugify(text) == expected
    
    def test_leading_trailing_hyphens(self):
        """Test trimming of leading and trailing hyphens."""
        text = "-Hello World-"
        expected = "hello-world"
        assert slugify(text) == expected
    
    def test_leading_trailing_spaces(self):
        """Test handling of leading and trailing spaces."""
        text = "  Hello World  "
        expected = "hello-world"
        assert slugify(text) == expected
    
    def test_mixed_case(self):
        """Test conversion to lowercase."""
        text = "HeLLo WoRLd"
        expected = "hello-world"
        assert slugify(text) == expected
    
    def test_special_characters_and_spaces(self):
        """Test complex text with various special characters."""
        text = "Hello @#$% World! & More"
        expected = "hello-world-more"
        assert slugify(text) == expected
    
    def test_empty_string(self):
        """Test empty string."""
        text = ""
        expected = ""
        assert slugify(text) == expected
    
    def test_only_special_characters(self):
        """Test string with only special characters."""
        text = "@#$%^&*()"
        expected = ""
        assert slugify(text) == expected
    
    def test_only_spaces(self):
        """Test string with only spaces."""
        text = "   "
        expected = ""
        assert slugify(text) == expected
    
    def test_only_hyphens(self):
        """Test string with only hyphens."""
        text = "---"
        expected = ""
        assert slugify(text) == expected
    
    def test_numbers_only(self):
        """Test string with only numbers."""
        text = "12345"
        expected = "12345"
        assert slugify(text) == expected
    
    def test_letters_only(self):
        """Test string with only letters."""
        text = "hello"
        expected = "hello"
        assert slugify(text) == expected
    
    def test_unicode_characters(self):
        """Test handling of unicode characters."""
        text = "Héllo Wörld"
        expected = "hllo-wrld"
        assert slugify(text) == expected
    
    def test_very_long_text(self):
        """Test with very long text."""
        text = "This is a very long text with many words and special characters @#$%^&*()"
        expected = "this-is-a-very-long-text-with-many-words-and-special-characters"
        assert slugify(text) == expected
    
    def test_single_character(self):
        """Test single character."""
        text = "A"
        expected = "a"
        assert slugify(text) == expected
    
    def test_single_number(self):
        """Test single number."""
        text = "5"
        expected = "5"
        assert slugify(text) == expected
    
    def test_mixed_alphanumeric(self):
        """Test mixed alphanumeric with special characters."""
        text = "Test123@#$%World456"
        expected = "test123world456"
        assert slugify(text) == expected


if __name__ == "__main__":
    pytest.main([__file__])
