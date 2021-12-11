# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии
# с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:
#     направление: шифрование или дешифрование;
#     язык алфавита: русский или английский;
#     шаг сдвига (со сдвигом вправо).

lower_alphabet, upper_alphabet, s_1 , num = '', '', '', 0


def lang(language):
    global lower_alphabet
    global upper_alphabet
    global num
    if language == 'rus':
        lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        num = 32
    elif language == 'eng':
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 26
    else:
        print('Язык указан неверно,попробуйте еще раз')
        return lang(input('Выберите язык (русский - rus; английский - eng)  '))


def cip(cipher, step):
    global s_1
    if cipher == '+':
        for i in s:
            if i in lower_alphabet:
                ind = lower_alphabet.find(i)
                s_1 += lower_alphabet[(ind + step) % num]
            elif i in upper_alphabet:
                ind = upper_alphabet.find(i)
                s_1 += upper_alphabet[(ind + step) % num]
            else:
                s_1 += i
    elif cipher == '-':
        for i in s:
            if i in lower_alphabet:
                ind = lower_alphabet.find(i)
                s_1 += lower_alphabet[(ind + num - step) % num]
            elif i in upper_alphabet:
                ind = upper_alphabet.find(i)
                s_1 += upper_alphabet[(ind + num - step) % num]
            else:
                s_1 += i
    else:
        return cip(input('Вы неверно ответили на вопрос, попробуйте еще раз. Желаете зашифровать - "+" или '
                         'дешифровать - "-"?  '), step_1)


cipher_1 = input('Желаете зашифровать - "+" или дешифровать - "-"?  ')
language_1 = input('Выберите язык (русский - rus; английский - eng)  ')
step_1 = int(input('Укажите шаг сдвига  '))
s = input('Введите фразу  ')

lang(language_1)
cip(cipher_1, step_1)
print(s_1)
