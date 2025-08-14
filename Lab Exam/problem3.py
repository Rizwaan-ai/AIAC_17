def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n1 = int(input("give n1:"))
n2 = int(input("give n2:"))

primes = [i for i in range(n1, n2+1) if is_prime(i)]
print(f"Prime numbers between {n1} and {n2} are {primes}")