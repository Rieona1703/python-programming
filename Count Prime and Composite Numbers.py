def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

arr = [4, 54, 29, 71, 59, 98, 23]
prime_count = sum(1 for x in arr if is_prime(x))
composite_count = len(arr) - prime_count
print("Composite numbers =", composite_count)
print("Prime numbers =", prime_count)
