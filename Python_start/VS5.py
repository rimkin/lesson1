n = int(input())
m = {'север':0, 'юг':0,'запад':0,'восток':0}
for item in range(n):
    a = input().split()
    m[a[0]] += int(a[1])
    print(m[a[0]])
if 'север' not in m:
    m['север'] = 0
if 'юг' not in m:
   m['юг'] = 0
if 'запад' not in m:
   m['запад'] = 0
if 'восток' not in m:
    m['восток'] = 0
o = m['восток'] - m['запад']
d = m['север'] - m['юг']
print(o, d)
