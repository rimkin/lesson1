import sys
import os
def tralala():
    print ('hello python {0}'.format(sys.version))
    return 555

def lalala():
    print ('return tralala {0}'.format(tralala()))

def get_filelist(dirpath):
    print('dirpath = {0}'.format(dirpath))
    return os.listdir(dirpath)

def get_sum(a,b):
    return a+b

def get_square(a):
    return a*a

def list_output(a):
    for item in a:
        print('    {0}'.format(item))   

lalala()
l1=get_filelist('./..')
print('l1={0}'.format(l1))
print('sum={0}'.format(get_sum('si','sia')))
print('a^2={0}'.format(get_square(get_sum(1000,700))))
l2=get_filelist('./')
list_output(l2)





