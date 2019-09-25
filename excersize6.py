class Buys(object):
    def __init__(self):
        self.buys=['milk','water','oil']
        self.cnt=0
        #self.buys=3

    def print_buys(self,listbuy):
        i=1
        l1=listbuy
        if (type(l1) is int) or (type(l1) is str):
            l1=[l1]  
        elif type(l1) is dict:
            l1=l1.values()
        if l1 ==None:
            l1=self.buys                  

        for item in l1:
            print('{0} buy={1}'.format(i,item))
            i=i+1
        self.cnt+=len(l1)
        return self.cnt    

a=Buys()
b=a.print_buys('poij')
print (b)
b=a.print_buys(['ooo','nnn'])
print (b)
b=a.print_buys({'key1':'ooo','key2':'nnn'})
print (b)
b=a.print_buys(None)
print (b)

t1=['a','s','d','f']
t2=t1.copy()
print('t1={0}; t2={1}'.format(t1,t2))
t1.append('p')
print('t1={0}; t2={1}'.format(t1,t2))

t3='qwerty'
t4=t3
print('t3={0}; t4={1}'.format(t3,t4))
t3+='p'
print('t3={0}; t4={1}'.format(t3,t4))
