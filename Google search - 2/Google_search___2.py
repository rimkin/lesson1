#На вход программе подается натуральное число n, затем n строк, затем число k — 
#количество поисковых запросов, затем k строк — поисковые запросы. Напишите программу, 
#которая выводит все введенные строки, в которых встречаются все поисковые запросы.

a = 0
lst = [input() for _ in range(int(input()))]
k = int(input())
search = [input().lower() for _ in range(k)]
for i in lst:
    for j in search:
        if j in i.lower():
            a += 1
    if a == k:
        print(i)
    a = 0