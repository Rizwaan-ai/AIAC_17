#calculator function
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        else:
            return a / b
    else:
        return "Invalid operation"
result = calculator(10, 5, "add")
print(result)