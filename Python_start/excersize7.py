import sys
import os

class Along(object):
    def __init__(self,arg):
        self.dirpath=arg
        #print('this is constructor')    
    
    def get_filelist(self):
        print('dirpath = {0}'.format(self.dirpath))
        self.b=os.listdir(self.dirpath)
        return self.b

    def list_output(self):
        for item in self.b:
            print('    {0}'.format(item))   
        return 5

    def list_output2(self,a):
        for item in a:
            print('    {0}'.format(item))
    
    def print_all(self):
        self.get_filelist()
        self.list_output()
        

class_obj1=Along('C:/Projects')
class_obj1.print_all()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
class_obj2=Along('C:/Projects/GitProjects/lesson1')
class_obj2.print_all()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
class_obj3=Along('C:/Projects/GitProjects')
class_obj3.print_all()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
a=os.listdir('C:/Projects/GitProjects/lesson1')
for item in a:
    print('    {0}'.format(item))
b=os.listdir('C:/Projects/GitProjects')
for item in b:
    print('    {0}'.format(item))
#a.get_filelist()
#c=a.list_output()
#print('return={0}'.format(print('c={0}'.format(c))))
#a.list_output2(a.get_filelist())




