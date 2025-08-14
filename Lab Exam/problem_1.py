import re

def extract_urls(text):
    # Regex to match URLs starting with http://, https://, or www.
    url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    return re.findall(url_pattern, text)

# Sample input string
sample_text = """
Check out our website at https://www.example.com for more info.
You can also visit our blog at http://blog.example.com or our partner site at www.partner.com/page.
Don't forget to follow us!
"""

# Extract and print URLs
urls = extract_urls(sample_text)
print(urls)
