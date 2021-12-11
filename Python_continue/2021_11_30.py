import os, fnmatch, re
list_1 = os.listdir('/Users/Rimkin/Desktop/Новая папка/orig_96075/generated')
list_2 = os.listdir('/Users/Rimkin/Dir_2')
list_3 = []

def compare(file_name):
    pass

#for path, dirs, files in os.walk(os.path.abspath(r'/Users/Rimkin/Dir_1')):
#    for filename in fnmatch.filter(files, "*.txt"):
#        print(filename)
with open('/Users/Rimkin/Dir_1/3.txt') as file:
    lines = [line for line in file if not line.startswith('(#|\n| )')]
print(lines)
#with open(filename, 'w') as file:
#    file.writelines(lines)
#a = open('/Users/Rimkin/Dir_1/3.txt')
#while True:
 #   lin = a.readline().strip().replace(' ', '')
  #  print(lin)
   # if lin.startswith('#'):
    #    print('123')
     #   continue
    #elif not lin:
     #   break
    #else:
     #   print(re.sub(r'(\n|\t| )', '', lin))
#a.close()
#st = a.read().strip()
#print(re.sub(r'(\n|\t| )', '', st))
