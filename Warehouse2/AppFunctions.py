import os
from FunctionHandler import FunctionHandler
from OtherFunctions import find_item_by_name, get_county_code_and_currency
from UtilFunctions import get_non_empty_str, get_number_input
import sys
import csv
from csv import reader

WAREHOUSE = list()
FUNCTION_HANDLER = FunctionHandler("BaseFunctions")

possible_functions = {
    8: "KilépéS",
    4: "Termék törlése",
    2: "Termék hozzáadása",
    3: "Termék módosítása",
    5: "Műveletek kiírása",
    1: "Raktáron lévő termékek kiírása",
    6: "Fájl mentési helyének módosítása",
    7: "Fájl mentése"
}

country_codes = [("HU", "Forint"), ("EN", "Font"), ("DE", "Euro"), ("J", "Jen")]
header = ["Név", "Ár", "Mennyiség", "Ország", "Valuta"]
change_path = True
path = os.getcwd()
filename = "warehouse.csv"
completeName = os.path.join(path, filename)

def initialize():
    reload_items()
    FUNCTION_HANDLER.add_function(8, escape)
    FUNCTION_HANDLER.add_function(4, delete_item)
    FUNCTION_HANDLER.add_function(2, add_item)
    FUNCTION_HANDLER.add_function(3, modify_item)
    FUNCTION_HANDLER.add_function(5, print_possible_functions)
    FUNCTION_HANDLER.add_function(1, print_items)
    FUNCTION_HANDLER.add_function(6, set_path)
    FUNCTION_HANDLER.add_function(7, write_to_csv)
    
def escape():
    quit()

def print_possible_functions():
    global possible_functions, completeName
    for key, item in sorted(possible_functions.items()):
        print(f"{key}. {item}")
    print()

def get_item():
    name = get_non_empty_str("Add meg a termék nevét", "Nem megfelelő érték, adj meg másikat!")
    price = get_number_input("Add meg a termék árát", "Nem megfelelő érték, adj meg másikat!")
    quantity = get_number_input("Add meg a termék mennyiségét", "Nem megfelelő érték, adj meg másikat!")
    countrycodes_index = get_county_code_and_currency(country_codes,"Add meg a termék származási helyének és valutájának számát", "Nem megfelelő érték, adj meg másikat!")
    return (name, price, quantity, country_codes[countrycodes_index-1][0], country_codes[countrycodes_index-1][1])

def add_item(storage = WAREHOUSE):
    name_is_taken = False
    while True:
        item = get_item()
        for i in storage:
            if item[0] == i[0]:
                print("Már van ilyen nevű termék!")
                name_is_taken = True
                break
        if not name_is_taken:
            storage.insert(len(storage), item)
            print(f"{item[0]} sikeresen hozzáadva!")
        break

def print_items(storage = WAREHOUSE):
    if not storage:
        print("A raktár jelenleg üres!")
        return
    for i in header:
        print(i, end=' ')
    print()
    for item in storage:
        print(*item, sep=' ')

def get_function(handler = FUNCTION_HANDLER):
    while True:
        function_key = get_number_input("Add meg a művelet számát", "Nincs ilyen művelet")
        try:
            return handler.get_function(function_key)
        except:
            print("Nem létező művelet!")

def delete_item(storage = WAREHOUSE, ask_msg = "Add meg a törlendő termék nevét"):
    while True:
        item = find_item_by_name(storage, ask_msg, "Nem megfelelő érték, adj meg másikat!")
        try:
            return storage.pop(storage.index(item))
        except:
            break

def modify_item(storage = WAREHOUSE):
    while True:
        item = delete_item(storage, "Add meg a módosítandó termék nevét")
        if item:
            price = get_number_input("Add meg a termék árát", "Nem megfelelő érték, adj meg másikat!")
            quantity = get_number_input("Add meg a termék mennyiségét", "Nem megfelelő érték, adj meg másikat!")

            new_item = (item[0], price, quantity, item[3], item[4])
            storage.insert(len(storage), new_item)
        else:
            break
        break

def write_to_csv(storage = WAREHOUSE):
    global completeName, change_path
    try:
        file = open(completeName, 'w+', newline ='', encoding='utf-8')
        print(f"Saved to {completeName}")
    except:
        print("Nem lehet megnyitni a fájlt!")
        return
    with file:    
        writer = csv.writer(file)
        writer.writerow(i for i in header)
        writer.writerows(storage)

def reload_items(storage = WAREHOUSE):
    global completeName
    try:
        with open(completeName, 'r', newline ='', encoding='utf-8') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            if header != None:
                for row in csv_reader:
                    storage.append(row)
    except:
        ("Nincsenek mentett termékek!")

def set_path():
    global change_path, completeName, filename
    if change_path:
        user_input = get_non_empty_str("Add meg a módosított mentési helyet", "Nem megfelelő érték, adj meg másikat!")
        try:
            completeName = os.path.join(user_input, filename)
            print(completeName)
            file = open(completeName, 'w+', newline ='', encoding='utf-8')
            change_path = False
        except:
            print("Hibás elérési út!")
            return
    else:
        print("A futás során csak egyszer módosíthatsz mentési helyet!")




