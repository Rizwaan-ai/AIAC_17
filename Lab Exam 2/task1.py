def deduplicate_emails(emails):
    """
    Returns the first occurrence of each email (case-insensitive),
    preserving original casing and order.
    
    Args:
        emails (list): List of email strings.
    
    Returns:
        list: Deduplicated list preserving original casing.
    """
    seen = set()
    result = []
    for email in emails:
        normalized = email.lower()
        if normalized not in seen:
            seen.add(normalized)
            result.append(email)
    return result
# Example usage 
if __name__ == "__main__":
    # Get dynamic input from user as comma-separated emails
    print("Enter email addresses separated by commas (e.g., Alice@example.com, bob@example.com, alice@example.com):")
    user_input = input("Emails: ").strip()
    
    if user_input:
        # Split by comma and strip whitespace from each email
        emails = [email.strip() for email in user_input.split(',') if email.strip()]
        deduplicated = deduplicate_emails(emails)
        print(f"\nOriginal emails: {emails}")
        print(f"Deduplicated emails: {deduplicated}")
    else:
        print("No emails entered.")
