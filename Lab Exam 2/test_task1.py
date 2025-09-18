import pytest
from task1 import deduplicate_emails


class TestDeduplicateEmails:
    """Test cases for the deduplicate_emails function."""
    
    def test_basic_deduplication(self):
        """Test basic deduplication functionality."""
        emails = ["alice@example.com", "bob@example.com", "alice@example.com"]
        expected = ["alice@example.com", "bob@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_case_insensitive_deduplication(self):
        """Test that deduplication is case-insensitive."""
        emails = ["Alice@example.com", "bob@example.com", "alice@example.com", "BOB@example.com"]
        expected = ["Alice@example.com", "bob@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_preserve_original_casing(self):
        """Test that original casing is preserved for first occurrence."""
        emails = ["ALICE@example.com", "bob@example.com", "alice@example.com", "Bob@example.com"]
        expected = ["ALICE@example.com", "bob@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_preserve_order(self):
        """Test that order of first occurrence is preserved."""
        emails = ["charlie@example.com", "alice@example.com", "bob@example.com", "alice@example.com", "charlie@example.com"]
        expected = ["charlie@example.com", "alice@example.com", "bob@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_no_duplicates(self):
        """Test with no duplicate emails."""
        emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]
        expected = ["alice@example.com", "bob@example.com", "charlie@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_all_duplicates(self):
        """Test with all emails being duplicates."""
        emails = ["alice@example.com", "ALICE@example.com", "Alice@example.com"]
        expected = ["alice@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_empty_list(self):
        """Test with empty list."""
        emails = []
        expected = []
        assert deduplicate_emails(emails) == expected
    
    def test_single_email(self):
        """Test with single email."""
        emails = ["alice@example.com"]
        expected = ["alice@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_mixed_case_domains(self):
        """Test with mixed case domains."""
        emails = ["alice@EXAMPLE.com", "bob@example.COM", "alice@example.com"]
        expected = ["alice@EXAMPLE.com", "bob@example.COM"]
        assert deduplicate_emails(emails) == expected
    
    def test_special_characters_in_email(self):
        """Test with special characters in email addresses."""
        emails = ["alice+test@example.com", "alice.test@example.com", "alice+test@example.com"]
        expected = ["alice+test@example.com", "alice.test@example.com"]
        assert deduplicate_emails(emails) == expected
    
    def test_whitespace_handling(self):
        """Test that function doesn't modify emails with whitespace (edge case)."""
        emails = [" alice@example.com ", "bob@example.com", " alice@example.com "]
        # Note: The function doesn't strip whitespace, so this tests current behavior
        expected = [" alice@example.com ", "bob@example.com"]
        assert deduplicate_emails(emails) == expected


if __name__ == "__main__":
    pytest.main([__file__])
