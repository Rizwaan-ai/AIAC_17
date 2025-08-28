def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n - 1)
    # The code already uses recursion as required.
print(factor(5))