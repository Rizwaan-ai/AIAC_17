import re
import random
import string

def is_valid_email(email):
    # Check for exactly one @
    if email.count('@') != 1:
        return False
    # Must contain at least one dot after @
    if '.' not in email.split('@')[1]:
        return False
    # Must not start or end with special characters
    if not re.match(r'^[A-Za-z0-9][A-Za-z0-9._@+-]*[A-Za-z0-9]$', email):
        return False
    # @ and . must not be at the start or end
    if email[0] in '@.' or email[-1] in '@.':
        return False
    return True

def generate_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3,8)))
    domain = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3,6)))
    tld = random.choice(['com', 'net', 'org', 'io'])
    email = f"{username}@{domain}.{tld}"
    return email

# Example usage:
if __name__ == "__main__":
    for _ in range(5):
        email = generate_email()
        print(f"Generated: {email} | Valid: {is_valid_email(email)}")
    # Test some invalid emails
    test_emails = [
        "@example.com", "user@.com", "user@@example.com", "userexample.com", "user@exam_ple.com."
    ]
    for email in test_emails:
        print(f"Test: {email} | Valid: {is_valid_email(email)}")