import re

def slugify(text):
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove all non-alphanumeric characters except hyphen
    text = re.sub(r'[^a-z0-9\-]', '', text)
    # Collapse multiple hyphens
    text = re.sub(r'-{2,}', '-', text)
    # Trim leading/trailing hyphens
    text = text.strip('-')
    return text
# Example usage 
if __name__ == "__main__":
    # Get dynamic input from user as a list
    print("Enter text strings as a list (e.g., ['Hello World!', 'AI & You', 'Set13-C2']):")
    user_input = input("Text list: ").strip()
    
    try:
        # Evaluate the input as a Python list
        texts = eval(user_input)
        if not isinstance(texts, list):
            print("Error: Input must be a list format.")
        else:
            # Process each text string to create slugs
            slugs = [slugify(text) for text in texts]
            print(f"\nOriginal texts: {texts}")
            print(f"URL slugs: {slugs}")
    except:
        print("Error: Invalid list format. Please enter texts in the format: ['text1', 'text2', 'text3']")