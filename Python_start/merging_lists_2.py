import os
import sys

def get_filelist(dirpath):
    print('dirpath = {0}'.format(dirpath))
    return os.listdir(dirpath)

def get_sum(a,b):
    print('sum=',a+b)



a=get_filelist('C:/Users/rimkin/Desktop/List 1')
print(a)
b=get_filelist('C:/Users/rimkin/Desktop/List 2')
print(b)
get_sum(a,b)
final_list = list(set(a+b))
print('final_list=',final_list)
