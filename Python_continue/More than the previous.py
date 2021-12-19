lst = [int(i) for i in input().split()]
counter = 0
for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        counter += 1
print(counter)
