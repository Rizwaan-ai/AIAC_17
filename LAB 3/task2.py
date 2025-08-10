# Take input from the user, split into a list, convert to integers
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Sort the list using the built-in sorting function
sorted_numbers = sorted(numbers)

# Output the sorted list
print("Sorted numbers:", sorted_numbers)
