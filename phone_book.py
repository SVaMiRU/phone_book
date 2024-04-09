# -*- coding: cp1251 -*-

import os
import sys

def add_new_user(name: str, phone: str, filename: str):
    """
    ���������� ������ ������������.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    ���������� ��� ���������� ���������� �����.
    """
    with open("numbers.txt", "r") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    ����� ������ �� �������� data.
    """
    with open(filename, "r") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "�� ���������� �������� ���������� �� �������"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    ������� ��� �������� ������ �� ������ �����
    � ������
    source: str - ��� ��������� �����
    dest: str - ��� ����� ���� ���������
    num_row: int - ����� ����������� ������
    """
    with open(source, 'r') as file:
        lines = file.readlines()

    if num_row < 1 or num_row > len(lines):
        print("�������� ����� ������ ��� ��������")
        return

    data_to_transfer = lines[num_row - 1]

    with open(dest, 'a') as dest_file:
        dest_file.write(data_to_transfer)

    print(f"������ {num_row} ���� ������� ����������� �� ����� {source} � ���� {dest}")

INFO_STRING = """
�������� ����� ������:
1 - ������� ��� ������
2 - ���������� ������ ������������
3 - �����
4 - ������� ������ � ������ ����
"""

file = "numbers.txt"

if file not in os.listdir():
    print("��������� ��� ����� �����������")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))      
    elif mode == 2:
        name = input("������� ���� ���:")
        phone = input("������� ����� ��������:")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("������� ��������:")
        print(search_user(file, data))
    elif mode == 4:
        # ��� ����� ������� ������� � �����������
        source = input("������� ��� ��������� �����: ")
        dest = input("������� ��� �����, ���� ����� ����������� ������: ")
        num_row = int(input("������� ����� ������ ��� ��������: "))
        transfer_data(source, dest, num_row)