# Function using For Loop
def print_multiples_for(num):
    print(f"\nFirst 10 multiples of {num} using for loop:")
    for i in range(1, 11):  # loop from 1 to 10
        print(f"{num} x {i} = {num * i}")


# Function using While Loop
def print_multiples_while(num):
    print(f"\nFirst 10 multiples of {num} using while loop:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1


# ---------- Main Program ----------
number = int(input("Enter a number: "))

print_multiples_for(number)
print_multiples_while(number)
