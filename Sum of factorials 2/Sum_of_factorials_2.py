from math import factorial
n = int(input())
factorial_total = 0
fact = 1
for i in range(1, n + 1):
    fact = factorial(i)
    factorial_total += fact
print(factorial_total)
