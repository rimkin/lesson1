import os                                                               
file = open('C:\\Users\\rimkin\\Downloads\\dataset_3363_2.txt', 'r')
a = file.readline().strip()
file.close()
b = ''
for i in range(0, len(a)):
    if i == len(a) - 2 and not ('0' <= a[i] <= '9'):
        c = a[i]
        d = int(a[i + 1])
        b += c * d
    else:
        if not ('0' <= a[i] <= '9') and i <= len(a) - 3:
            c = a[i]
            if not ('0' <= a[i + 2] <= '9'):
                d = int(a[i + 1])
            else:
                if i <= len(a) - 3:
                    p = a[i + 1] + a[i + 2]
                    d = int(p)
        else:
            continue
        b += c * d
print(b)
out = open('dataset_3363_2.txt', 'w')
out. write(b)
out.close()
