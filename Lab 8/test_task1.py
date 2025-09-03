import unittest
from task1 import is_valid_email, generate_email

class TestEmailFunctions(unittest.TestCase):

    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "john.doe123@domain.net",
            "alice_bob@sub-domain.org",
            "a1b2c3@xyz.io",
            "user.name+tag@domain.com"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "@example.com",           # starts with @
            "user@.com",              # domain starts with .
            "user@@example.com",      # double @
            "userexample.com",        # missing @
            "user@exam_ple.com.",     # ends with .
            ".user@domain.com",       # starts with .
            "user@domain.com.",       # ends with .
            "user@domaincom",         # missing .
            "user@domain..com",       # double dot in domain
            "user@-domain.com",       # domain starts with -
            "user@domain-.com",       # domain ends with -
            "user@domain.c",          # tld too short
            "user@.domain.com",       # domain starts with .
            "user@domain.com-",       # ends with -
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_generate_email_validity(self):
        # Generated emails should always be valid
        for _ in range(20):
            email = generate_email()
            self.assertTrue(is_valid_email(email), f"Generated invalid email: {email}")

if __name__ == "__main__":
    unittest.main()