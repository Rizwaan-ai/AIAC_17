def divide_numbers(a, b):
    """
    Divides two numbers and handles division by zero.
    Args:
        a (float): Numerator.
        b (float): Denominator.
    Returns:
        float: Result of division if successful.
        str: Error message if division by zero occurs.
    Raises:
        TypeError: If inputs are not numbers.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
# Example usage
print(divide_numbers(10, 0))