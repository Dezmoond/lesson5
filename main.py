import os
import shutil
import platform
import borndayforewer
import use_functions

def create_folder():
    name = input("Введите название папки: ")
    os.makedirs(name, exist_ok=True)
    print(f"Папка '{name}' создана")


def delete_file_or_folder():
    name = input("Введите название файла или папки для удаления: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален")
    else:
        print("Такого файла или папки нет")


def copy_file_or_folder():
    src = input("Введите имя файла/папки для копирования: ")
    dest = input("Введите новое имя файла/папки: ")
    if os.path.isdir(src):
        shutil.copytree(src, dest)
        print(f"Папка '{src}' скопирована в '{dest}'")
    elif os.path.isfile(src):
        shutil.copy2(src, dest)
        print(f"Файл '{src}' скопирован в '{dest}'")
    else:
        print("Такого файла или папки нет")


def list_directory():
    print("Содержимое директории:", os.listdir())


def list_folders():
    print("Папки:", [d for d in os.listdir() if os.path.isdir(d)])


def list_files():
    print("Файлы:", [f for f in os.listdir() if os.path.isfile(f)])


def os_info():
    print("Операционная система:", platform.system(), platform.release())


def creator_info():
    print("Создатель программы: Даниил Савченко")


def change_directory():
    path = input("Введите новый путь рабочей директории: ")
    try:
        os.chdir(path)
        print("Рабочая директория изменена")
    except FileNotFoundError:
        print("Указанный путь не найден")

#def victory_game():
#    borndayforewer.otvet('Введите год рождения А.С.Пушкина: ', '1799')
#    borndayforewer.otvet('В какой день июня родился Пушкин? ', '6')
#def bank():
#    use_functions.display_menu()

def main():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Просмотр содержимого директории")
        print("5. Просмотр только папок")
        print("6. Просмотр только файлов")
        print("7. Информация об ОС")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")
        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            list_directory()
        elif choice == "5":
            list_folders()
        elif choice == "6":
            list_files()
        elif choice == "7":
            os_info()
        elif choice == "8":
            creator_info()
        elif choice == "9":
            borndayforewer.victory()
        elif choice == "10":
            use_functions.bank()
        elif choice == "11":
            change_directory()
        elif choice == "12":
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()