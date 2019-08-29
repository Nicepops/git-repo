__author__ = 'Осипов П.Д.'

import os
import shutil

#easy
#1

def make_dirs(names):
    main_path = os.getcwd()
    for elem in x:
        dir_path = os.path.join(main_path, elem)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)



def remove_dirs(names):
    main_path = os.getcwd()
    dirs = os.listdir(main_path)
    for elem in dirs:
        if elem in x:
            dir_path = os.path.join(main_path, elem)
            os.rmdir(dir_path)
        else:
            print(f'Невозможно удалить папку {names}!')


x = [f'dir_{i}' for i in range(1, 10)]
make_dirs(x)
remove_dirs(x)

#2
def list_dir():
    main_path = os.getcwd()
    dirs = os.listdir(main_path)
    print(f'Папки текущей директории: ')
    for i in dirs:
        dir_path = os.path.join(main_path, i)
        if os.path.isdir(dir_path):
            print(i)

list_dir()


#3

def make_file():
    file_name = os.path.realpath(__file__)
    new_file = file_name+'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(file_name, new_file)
        print(f'Файл {new_file} успешно создан')
    else:
        print('Такой файл уже существует')

make_file()

