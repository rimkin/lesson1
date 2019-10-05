import sys
import os

def compare_files(path_file_1, path_file_2):
    size_file_1 = os.path.getsize (path_file_1)
    size_file_2 = os.path.getsize (path_file_2)
    if size_file_1 == size_file_2:
        return True
    else:
        return False

path_file_1 = 'C:/Users/rimkin/Desktop/List_1/3.jpg'
path_file_2 = 'C:/Users/rimkin/Desktop/List_2/3.jpg'
a = compare_files(path_file_1, path_file_2)
print (a)
print ('size_file_1 = {0}'.format(os.path.getsize ('C:/Users/rimkin/Desktop/List_1/3.jpg')))
print ('size_file_2 = {0}'.format(os.path.getsize ('C:/Users/rimkin/Desktop/List_2/3.jpg')))


