n = 29
is_prime = n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
print("Prime" if is_prime else "Not Prime")