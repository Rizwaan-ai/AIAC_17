def largest_of_three(a, b, c):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    return max(a, b, c)

print("The largest number is:", largest_of_three(0, 0, 0))