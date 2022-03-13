from UtilFunctions import get_non_empty_str, get_number_input

def find_item_by_name(storage, ask_msg: str, error_msg: str, not_found = "Nem található ilyen névvel termék:"):
    while True:
        name = get_non_empty_str(ask_msg, error_msg)
        for i in storage:
            if i[0] == name:
                return i
        print(f"{not_found} {name}")
        break

def get_county_code_and_currency(storage, ask_msg: str, error_msg: str):
    print("Az alábbi országkódok ismertek:")
    for i in storage:
        print(storage.index(i) + 1, i)
    while True:
        user_input = get_number_input(f"{ask_msg}", f"{error_msg}")
        if user_input > 0 and user_input <= len(storage):
            return user_input
        else:
            print("Nem ismert országkód!")
            continue