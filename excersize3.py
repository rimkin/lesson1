import sys
import inspect
sys.version


print('format output No 1')

def my_print(s):
    print('%s %s'%(inspect.stack()[1][3],s))

def my_output1(arg1,arg2,arg3):
    print('a=',arg1,'b=',arg2,'c=',arg3) 

def my_output2(arg1,arg2,arg3):
    my_print('a={0} b={1} c={2}'.format(arg1,arg2,arg3))

def my_output3(arg1,arg2,arg3):
    my_print(('a=%.1f b={0} c=%s'%(arg1,arg3)).format(arg2))




a=7.787654
b=[1,'example 1']
c='number 2'
#print('a=',a,'b=',b,'c=',c)
my_output1(a,b,c)
my_output2(a,b,c)
my_output3(a,b,c)
my_print('a={0} b={1} c={2}'.format(a,b,c))
print('hello world')
my_print('hello world')

