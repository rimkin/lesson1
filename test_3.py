mat = 0
fiz = 0
rus = 0
sr = []
i = 0
itog = ''
with open ('C:\\Users\\rimkin\\Downloads\\dataset_3363_4.txt') as file:
    for line in file:
        line = line.strip().split(';')
        mat += int(line[1])
        fiz += int(line[2])
        rus += int(line[3])
        i += 1
        sr.append((int(line[1]) + int(line[2]) + int(line[3])) / 3)
itog += str(mat / i) + ' '
itog += str(fiz / i) + ' '
itog += str(rus / i) 
with open ('C:\\Projects\\GitProjects\\lesson1\\1.txt', 'w') as a:
    for item in sr:
        a.write('{0}\n'.format(item))
    a.write(itog)

