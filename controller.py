from module import create_new_contact
from module import create_correct_format
from module import write_data
from module import find_all_by_key
from tabulate import tabulate 


filename = 'phone_directory'

# ur = user request принимает номер запроса от пользователя 
def process_control():
    ur = int(input('Hello, please choose something from menu! \n If you want to create contact, please input 1. \n If you want to find contact, please input 2. \n If you want to see the list contacts, please input 3. \n If you want to close phone directory, please input 4. \n\n' 'Input correct menu item: '))
    while ur > 4 or ur < 1:
        ur = int(input('Input correct menu item: '))
    if ur == 1:
        write_data(create_new_contact())
        exit()
    elif ur == 2:
        print(tabulate(find_all_by_key(create_correct_format(filename)), headers="keys", tablefmt="simple_grid"))
        exit()
    elif ur == 3:
        print(tabulate(create_correct_format(filename), headers="keys", tablefmt="simple_grid"))
        exit()
    else:
        print('The program will be close! \n Have a good day! \n See you later!')
        exit()

