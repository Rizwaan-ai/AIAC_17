def find_largest(numbers):
    if len(numbers) != 3:
        raise ValueError("List must contain exactly 3 numbers.")
    return max(numbers)

# Dynamic input from user
numbers = list(map(float, input("Enter three numbers separated by spaces: ").split()))
if len(numbers) != 3:
    raise ValueError("Please enter exactly three numbers.")

largest = find_largest(numbers)
print(f"The largest number among the entered values is: {largest}")