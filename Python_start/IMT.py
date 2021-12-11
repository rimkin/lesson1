#Индекс массы тела

weight, height = float(input()), float(input())
IMT = weight / (height ** 2)
print(IMT)
if IMT >= 18.5 and IMT <= 25:
    print('Оптимальная масса')
elif IMT < 18.5:
    print('Недостаточная масса')
elif IMT > 25:
    print('Избыточная масса')
else:
    print('Something wrong')