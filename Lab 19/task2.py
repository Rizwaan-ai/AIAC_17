def check_number(num):
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero"
# --- Dynamic Input Section ---
try:
    # 1. Get input from the user (returns a string)
    user_input = input("Enter an integer number (e.g., -5, 0, 7): ")
    # 2. Convert the input string to an integer
    # This step is crucial because the input() function always returns a string.
    dynamic_num = int(user_input)
    # 3. Call the function with the dynamic input
    result = check_number(dynamic_num)
    # 4. Print the final output
    print(f"\nInput: {dynamic_num} → Output: {result}")
except ValueError:
    print("\nError: Invalid input. Please enter a valid integer.")