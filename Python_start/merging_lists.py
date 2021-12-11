a=[1,2,3]
b=[]

def get_sum(a,b):
    b.append(1)
    b.append(2)
    b.append(400)
    b.append(100)
    print(a+b)



get_sum(a,b)
print('b=',b)
final_list = list(set(a+b))
print(final_list)

 