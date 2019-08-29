__author__ = 'Осипов П.Д.'

#normal
import os
import HW5easy as easy

def change_dir(name):
    old_path = os.getcwd
    new_path = os.path.join(old_path, name)
    try:
        os.chdir(new_path)
    except OSError as e:
        print(f'Невозможно перейти в папку {name}!\nОшибка: {e}')


def menu():
    menu_options = {
        '1': {'name': 'Перейти в папку', 'func': change_dir, 'param': True},
        '2': {'name': 'Просмотреть содержимое текущей папки', 'func': easy.list_dir(), 'param': False},
        '3': {'name': 'Удалить папку', 'func': easy.remove_dirs(names), 'param': True},
        '4': {'name': 'Создать папку', 'func': easy.make_dirs(names), 'param': True},
        '5': {'name': 'Выход', 'func': quit(), 'param': 0},
    }

    for key, value in menu_options.items():
        print(f'{key}. {value["name"]}')

    temp = input("Выберите пункт меню\n")
        for key, value in menu_options.items():
            if key == temp:
                if value['param']:
                    value['func'](input("Введите название папки\n"))
                    break
                else:
                    value['func']()
                    break
            else:
                print("Попробуйте снова")
                continue

if __name__ == "__main__":
    while True:
        menu()
