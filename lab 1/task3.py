def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {n} is {factorial(n)}")