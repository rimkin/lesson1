#На обработку поступает последовательность из 7 целых чисел. 
#Известно, что вводимые числа по абсолютной величине не превышают 10^6. 
#Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности 
# или 0, если чётных чисел в последовательности нет. 
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). 

s = 0                       #1
for _ in range(7):          #2
    n = int(input())        #4
    if n % 2 == 0:          #3
        s += n
print(s)
