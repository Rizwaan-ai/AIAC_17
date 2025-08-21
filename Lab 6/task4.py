def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter a number: "))
print("Sum using for loop:", sum_to_n_for(n))
