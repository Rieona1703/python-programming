n = int(input("enter a number"))
divisors = [i for i in range(1, n) if n % i == 0]
if sum(divisors) == n:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
