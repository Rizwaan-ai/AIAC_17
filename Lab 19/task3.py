def factorial(n):
    # Base case: Factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive step: n * factorial(n - 1)
    elif n > 0:
        return n * factorial(n - 1)
    else:
        # Handle negative inputs gracefully
        return "Factorial is not defined for negative numbers."
try:
    user_input = input("\nEnter an integer for factorial: ")
    num = int(user_input)
    print(f"Input: {num} → Factorial = {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")