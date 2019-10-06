import sys
import os

def get_filelist(dirpath):
    print('dirpath = {0}'.format(dirpath))
    return os.listdir(dirpath)

def get_sum(a,b):
    print('sum=',a+b)

def list_output(final_list):
    for item in final_list:
        print('    {0}'.format(item))

def compare_files(path_file_1, path_file_2):
    size_file_1 = os.path.getsize (path_file_1)
    size_file_2 = os.path.getsize (path_file_2)
    if size_file_1 == size_file_2:
        final_list = list(set(a+b))
        print('final_list=',final_list)
        #list_output(final_list)
        return final_list
    else:
        return False



print ('size_file_1 = {0}'.format(os.path.getsize ('C:/Users/rimkin/Desktop/List_1/4.jpg')))
print ('size_file_2 = {0}'.format(os.path.getsize ('C:/Users/rimkin/Desktop/List_2/4.jpg')))
a=get_filelist('C:/Users/rimkin/Desktop/List_1')
print(a)
b=get_filelist('C:/Users/rimkin/Desktop/List_2')
print(b)
get_sum(a,b)
path_file_1 = 'C:/Users/rimkin/Desktop/List_1/4.jpg'
path_file_2 = 'C:/Users/rimkin/Desktop/List_2/4.jpg'
c = compare_files(path_file_1, path_file_2)
list_output(c)


