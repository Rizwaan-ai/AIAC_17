import string

def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        char.lower() for char in sentence if char.isalnum()
    )
    # Check if cleaned sentence is a palindrome
    return cleaned == cleaned[::-1]

# Example usage:
print(is_sentence_palindrome("A man a plan a canal Panama"))  # True