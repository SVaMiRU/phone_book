# -*- coding: cp1251 -*-

import os
import sys

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open("numbers.txt", "r") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    функция для переноса строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
    with open(source, 'r') as file:
        lines = file.readlines()

    if num_row < 1 or num_row > len(lines):
        print("Неверный номер строки для переноса")
        return

    data_to_transfer = lines[num_row - 1]

    with open(dest, 'a') as dest_file:
        dest_file.write(data_to_transfer)

    print(f"Строка {num_row} была успешно скопирована из файла {source} в файл {dest}")

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "numbers.txt"

if file not in os.listdir():
    print("указанное имя файла отсутствует")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))      
    elif mode == 2:
        name = input("Введите Ваше имя:")
        phone = input("Введите номер телефона:")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение:")
        print(search_user(file, data))
    elif mode == 4:
        # Тут нужно вызвать функцию с аргументами
        source = input("Введите имя исходного файла: ")
        dest = input("Введите имя файла, куда нужно скопировать строку: ")
        num_row = int(input("Введите номер строки для переноса: "))
        transfer_data(source, dest, num_row)