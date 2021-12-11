dic = {}

def get_val(parent, child):
    if child in dic.keys():
        print(child)
        v = dic.get(child)
        print(v)
        if parent in v:
            return 'Yes'
        #elif len(v) == 0:
        #    return 'No'
        else:
            for item in v:
                print(item)
                print(get_val(parent, item))
                if get_val(parent, item) == 'None':
                    return get_val(parent, v[item + 1])

def full(i):
    if i[0] in dic.keys():
        dic[i[0]].append(i[2:])
    else:
        dic[i[0]] = i[2:]

for n in range(int(input())):
    i = input().strip(':').split(' ')
    full(i)
        
for q in range(int(input())):
    j = input().strip().split(' ')
    if j[0] == j[1]:
        print('Yes')
    elif j[1] in dic.keys():
        print(get_val(j[0], j[1]))
    else:
        print('No')
print(dic)


