# -*- coding: cp1251 -*-

import os
import sys

def add_new_user(name: str, phone: str, filename: str):
    """
    Äîáàâëåíèå íîâîãî ïîëüçîâàòåëÿ.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Âîçâðàùàåò âñå ñîäåðæèìîå òåëåôîííîé êíèãè.
    """
    with open("numbers.txt", "r") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Ïîèñê çàïèñè ïî êðèòåðèþ data.
    """
    with open(filename, "r") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "Ïî óêàçàííîìó çíà÷åíèþ ñîâïàäåíèé íå íàéäåíî"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    ôóíêöèÿ äëÿ ïåðåíîñà ñòðîêè èç îäíîãî ôàéëà
    â äðóãîé
    source: str - èìÿ èñõîäíîãî ôàéëà
    dest: str - èìÿ ôàéëà êóäà ïåðåíîñèì
    num_row: int - íîìåð ïåðåíîñèìîé ñòðîêè
    """
    with open(source, 'r') as file:
        lines = file.readlines()

    if num_row < 1 or num_row > len(lines):
        print("Íåâåðíûé íîìåð ñòðîêè äëÿ ïåðåíîñà")
        return

    data_to_transfer = lines[num_row - 1]

    with open(dest, 'a') as dest_file:
        dest_file.write(data_to_transfer)

    print(f"Ñòðîêà {num_row} áûëà óñïåøíî ñêîïèðîâàíà èç ôàéëà {source} â ôàéë {dest}")

INFO_STRING = """
Âûáåðèòå ðåæèì ðàáîòû:
1 - âûâåñòè âñå äàííûå
2 - äîáàâëåíèå íîâîãî ïîëüçîâàòåëÿ
3 - ïîèñê
4 - ïåðåíîñ çàïèñè â äðóãîé ôàéë
"""

file = "numbers.txt"

if file not in os.listdir():
    print("óêàçàííîå èìÿ ôàéëà îòñóòñòâóåò")
    sys.exit()

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))      
    elif mode == 2:
        name = input("Ââåäèòå Âàøå èìÿ:")
        phone = input("Ââåäèòå íîìåð òåëåôîíà:")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Ââåäèòå çíà÷åíèå:")
        print(search_user(file, data))
    elif mode == 4:
        # Òóò íóæíî âûçâàòü ôóíêöèþ ñ àðãóìåíòàìè
        source = input("Ââåäèòå èìÿ èñõîäíîãî ôàéëà: ")
        dest = input("Ââåäèòå èìÿ ôàéëà, êóäà íóæíî ñêîïèðîâàòü ñòðîêó: ")
        num_row = int(input("Ââåäèòå íîìåð ñòðîêè äëÿ ïåðåíîñà: "))
        transfer_data(source, dest, num_row)
