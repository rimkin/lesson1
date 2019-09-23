def going_to_the_shop(listbuy):
    if type(listbuy) is int:
        print('it is not possible')
        return None
    elif type(listbuy) is str:
        print('buy={0}'.format(listbuy))
        return 'buy={0}'.format(1)
    a=1
    for item in listbuy:
        print('{0} buy={1}'.format(a,item))
        a=a+1
    return 'buy={0}'.format(len(listbuy))

#b=going_to_the_shop(['bread','milk','eggs','water'])
b=going_to_the_shop({'milk':'good','vodka':'bad'})
print (b)




