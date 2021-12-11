n = int(input())
factorial_total = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
        print('fact =', factorial, 'i =', i, 'j =', j)
    factorial_total += factorial
print(factorial_total)