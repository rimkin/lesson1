#На вход программе подается натуральное число n, затем n строк, затем еще одна строка — 
#поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых 
#встречается поисковый запрос.

lst = [input() for _ in range(int(input()))]
k = input().lower()
for i in lst:
    if k in i.lower():
        print(i)