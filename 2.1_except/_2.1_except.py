d = {}
s = []
n = 0

def rec(t):
    if str(t) in d.keys():
        for item in d.get(t):
            print(item)
            if item in s:
                print(n)
                break
            else:
                rec(item)
                return

n = int(input())
for i in range(n):
    nasl = input().split(' ')
    if len(nasl) > 1:
        if nasl[0] in d.keys():
            for item in range(2, len(nasl)):
                d[nasl[0]].append(nasl[item])
        else:
            d[nasl[0]] = nasl[2:]
print(d)

m = int(input())
for i in range(m):
    exc = input()
    print(s)
    print(rec(exc))
    if rec(exc) == True:
        print(exc)
    s.append(exc)


