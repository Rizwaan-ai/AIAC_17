def factorial(n):
    """
    Simple factorial function
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the function
if __name__ == "__main__":
    # Get input from user
    try:
        num = int(input("Enter a number to find factorial: "))
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
    except ValueError:
        print("Please enter a valid integer!")
    
    # Example calculations
    print("\nExample calculations:")
    for i in range(6):
        print(f"Factorial of {i} = {factorial(i)}")
