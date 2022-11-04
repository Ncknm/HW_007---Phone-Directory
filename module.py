from tabulate import tabulate 

filename = 'phone_directory'
key_array = ['Name', 'Surname', 'Patronymic', 'Phone']

def create_correct_format (data, sep = ','):
    with open(f'{data}.txt', 'r') as ph:
        correct_data = []
        for line in ph:
            line = line.replace('\n', '')
            correct_data.append(dict(zip(key_array, line.split(sep))))
        return correct_data


def convert_data(data, sep):
    format_data = ''
    values_list = []
    for i in data:
        values_list.append(data[i])
    format_data += sep.join(values_list)
    return format_data + '\n'


def create_new_contact ():
    new_contact = dict(zip(key_array, input('Input your name, surname, patronymic and phone (by spaces): ').split()))
    print(tabulate([new_contact], headers="keys", tablefmt="simple_grid"))
    return new_contact


def write_data(data):
    with open(f'{filename}.txt', 'a', encoding = 'utf-8') as ph:
        ph.write(convert_data((data), ',')) 
    with open(f'{filename}.csv', 'a', encoding = 'utf-8') as phc:
        phc.write(convert_data((data), ':'))


def find_all_by_key(data):
    count = 0
    value = input('If you want find somebody please input search parametrs: ')
    for dict_ in data:
        for values in dict_:
            if value in dict_[values]:
                yield dict_
                count += 1
    if count == 0:
        print('No matches found')


    