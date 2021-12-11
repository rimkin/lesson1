b = []
with open ('C:\\Users\\rimkin\\Downloads\\dataset_3363_3.txt') as file:
    for line in file:
        line = line.lower().strip().split()
        b += line
print(b)
m = 0
for item in b:
    x = b.count(item)
    if x > m:
        m = x
        i = item
    elif x == m:
        if item < i:
            i = item
            m = x
    #print(item)
    #print(x)
a = open('1.txt', 'w')
a.write('{0} {1}'.format(i, m))
a.close()
