#На обработку поступает последовательность из 10 целых чисел. 
#Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности 
#и максимальное отрицательное число в последовательности. 
#Если отрицательных чисел нет, требуется вывести на экран «NO». 
#Программист торопился и написал программу неправильно.
#Найдите все ошибки в этой программе (их ровно 5). 
#Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения 
#других строк.
mx = -10 ** 6
s = 0
for _ in range(10):     #5
    x = int(input())
    if x < 0:
        s += x          #1
        if x > mx:      #2
            mx = x
if s != 0:              #3
    print(s)
    print(mx)
else:                   #4
    print('NO')
