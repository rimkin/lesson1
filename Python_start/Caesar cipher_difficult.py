# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.

lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = 0
lst_count = []

s = input('Введите фразу для шифрования  ')
lst = s.split()
for i in range(len(lst)):
    for j in lst[i]:
        if j.isalpha():
            counter += 1
    lst_count.append(counter)
    counter = 0
for index, elem in enumerate(s):
    if elem.isalpha():
        if elem in lower_alphabet:
            ind = lower_alphabet.find(elem)
            print(lower_alphabet[(ind + lst_count[counter]) % 26], end='')
        else:
            ind = upper_alphabet.find(elem)
            print(upper_alphabet[(ind + lst_count[counter]) % 26], end='')
    elif not elem.isalpha() and s[index - 1].isalpha():
        counter += 1
        print(elem, end='')
    else:
        print(elem, end='')

