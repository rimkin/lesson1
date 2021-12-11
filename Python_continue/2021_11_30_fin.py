import os, re

dir_1 = '/Users/Rimkin/Desktop/Новая папка/orig_96075/generated'
dir_2 = '/Users/Rimkin/Desktop/Новая папка/xml2xpp_96075/generated'

def get_full_names_list(dir): #Возвращает список файлов в директории, которую принимает в виде аргумента
    ret = []
    list_dir = os.listdir(dir)
    for i in list_dir:
        if os.path.isdir(dir + '/' + i):
            get_list_from_folder(dir + '/' + i, '/' + i, ret)
        else:
            ret.append('/' + i)
    return ret

def get_list_from_folder(dir, name, ret):  #Осуществляет проход по папкам
    list_dir = os.listdir(dir)
    for i in list_dir:
        if os.path.isdir(dir + '/' + i):
            get_list_from_folder(dir + '/' + i, name + '/' + i, ret)
        else:
            ret.append(name + '/' + i)

def get_common_list(list1, list2): #Сравнивает 2 списка файлов, возвращает список одноименных
    ret = []
    for i in list1:
        if i in list2:
            ret.append(i)
    if ret == []:
        print('The list is empty')
    else:
        return ret

def read_file(file):  #Осуществляет чтение файла и редактирование
    ret =[]
    a = open(file)
    lines = [line.strip().split() for line in a if not line.startswith('//')]
    #print(lines)
    for line in lines:  #Удаление пустых строк и однострочных комментов
        if line == []:
            continue
        else:
            for i in line:
                st = ''
                for j in range (0, len(i)):
                    #print(i)
                    if i[j] == '/' and j != len(i) - 1:
                        if i[j + 1] == '/':
                            break
                        else:
                            st += i[j]
                    else:
                        st += i[j]
                        #print(st)
                if st != '':
                    ret.append(st)
    ret = ''.join(ret)  #Преобразования списка в строку с последующим удалением многострочных комментов
    if '/*' in ret:
        ret = ret[:ret.find('/*')] + ret[ret.find('*/') + 2:]
    a.close()
    return ret

def common_read_file(list1, list2):  #Сравнивает 2 одноименных файла из разных директорий, возвращает True or False
    if list1 == list2:
        return True
    else:
        return False


def files_run(get_common_list):  #Проходит по списку одноименных файлов, считывает их и сравнивает, возвращает кол-во одинаковых
    counter = 0
    for i in get_common_list:
        adr_1 = dir_1 + i
        adr_2 = dir_2 + i
        file_1 = read_file(adr_1)
        file_2 = read_file(adr_2)
        if common_read_file(file_1, file_2):
            #print(f'File {adr_1} = file {adr_2}')
            counter += 1
        #else:
            #print(f'File {adr_1} not = file {adr_2}')
    print(counter)



list_1 = get_full_names_list(dir_1)
#print(list_1)
list_2 = get_full_names_list(dir_2)
#print(list_2)
full_list = get_common_list(list_1, list_2)
#print(full_list)
files_run(full_list)

#a = read_file('/Users/Rimkin/Dir_1/3.txt')
#b = read_file('/Users/Rimkin/Dir_2/3.txt')
#print(a, b)
#print(common_read_file(a, b))

