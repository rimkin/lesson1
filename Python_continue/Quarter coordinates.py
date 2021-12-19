count = 4 * [0]
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 < y:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif y < 0 <x:
        count[3] += 1
[print(f"{['Первая', 'Вторая', 'Третья', 'Четвертая'][i]} четверть: {count[i]}") for i in range(4)]