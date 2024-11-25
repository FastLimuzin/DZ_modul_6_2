
import os

# Задача 6.2.1
def task_6_2_1():

    abs_path_file_1 = os.path.abspath('data_path_1/test_file_1.txt')
    print(f"Абсолютный путь к test_file_1.txt: {abs_path_file_1}")


    print("\nСодержимое проекта:")
    for root, dirs, files in os.walk('.'):
        print(f"Каталог: {root}")
        for dir_ in dirs:
            print(f"  Папка: {dir_}")
        for file in files:
            print(f"  Файл: {file}")


    abs_path_file_3 = os.path.abspath(os.path.join('data_path_2', 'test_file_3.txt'))
    print(f"\nАбсолютный путь к test_file_3.txt: {abs_path_file_3}")


    new_folder = os.path.join('data_path_2', 'new_folder')
    os.makedirs(new_folder, exist_ok=True)
    print(f"\nПапка создана: {new_folder}")
    os.rmdir(new_folder)
    print(f"Папка удалена: {new_folder}")

# Задача 6.2.2
def write_poem_to_file(file_path, lines):
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"\nТекст записан в файл: {file_path}")

def read_poem_from_file(file_path):
    print("\nТекст из файла:")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    task_6_2_1()
    poem_file = "data_path_1/test_file_1.txt"
    poem_lines = [
        "Если б мишки были пчелами,",
        "То они бы нипочем,",
        "Никогда и не подумали,",
        "Так высоко строить дом."
    ]
    write_poem_to_file(poem_file, poem_lines)
    read_poem_from_file(poem_file)
