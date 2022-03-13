import os
from AppFunctions import get_function, initialize, print_possible_functions

def main():
    initialize()
    first_start = True
    while True:
        if first_start:
            print_possible_functions()
            first_start = False

        function_handler = get_function()
        function_handler()
    
if __name__ == "__main__":
    os.system("cls") # linux-on "clear"
    main()