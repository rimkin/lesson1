import sys

def f1(a):
    print 'hello function a=',a

# comment1
def f2(r):
    if type(r) != list:
        print 'not a list',r
        return

    index=0
    for item in r:
        print 'item[',index,']=',item
        index=index+1

    for i in range(0,len(r)):
        item=r[i]
        print 'item[',i,']=',r[i]
        

print sys.version
print 'making functions'
a=1
b='1'
c=[1,2,3]
d={'key1':1,'key2':2}
full_list=[]
full_list.append(a)
full_list.append(b)
full_list.append(c)
full_list.append(d)
print 'full_list=',full_list
f2(a)
f2(b)
f2(c)
f2(d)




