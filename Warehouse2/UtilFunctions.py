def get_non_empty_str(ask_msg: str, error_msg: str):
    while True:
        user_input = input(f"{ask_msg}: ")
        if not user_input:
            print(f"{error_msg}")
            continue
        elif user_input.isdigit():
            print(f"{error_msg}")
            continue
        return user_input

def get_number_input(ask_msg: str, error_msg: str):
    while True:
        user_input = input(f"{ask_msg}: ")
        if not user_input.isdigit():
            print(f"{error_msg}")
            continue
        return int(user_input)