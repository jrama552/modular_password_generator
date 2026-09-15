import json
import csv
import pykakasi     # pip install pykakasi
from gen_functions import char_dictionary

# -------------------------------------------------------------


# loading file to list
def read_file(filename):
    if 'json' in filename:
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            return json.load(f)
    if 'csv' in filename:
        return csv_list(filename)


def csv_list(filename):
    data = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for item in reader:
            data.append(item)
    # print(f'reading csv_list data: \n{data}')
    return data
# ------------------------------------------------------------------------


# writing list to file
def write_file(filename, list_data):
    if 'json' in filename:
        with open(filename, 'w') as f:
            json.dump(list_data, f, indent=4)
    if 'csv' in filename:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(list_data)


# cleaning of csv format
def clean_csv(file='jp_file.csv'):
    # initial 'cleaning'
    data = []
    with open(file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            item = row[0]
            item.strip('\"')    # unnecessary
            # csv.reader() acts a parser--(avoids , issues)
            item = next(csv.reader([item]))
            data.append(item)
        # print(data)

    # writing to new file
    write_file('jp_dict.csv', data)


# function that translates and cuts words
def translator(lst):
    kks = pykakasi.kakasi()
    romaji = []
    # start = time.perf_counter()
    for item in lst:
        roman = kks.convert(item)   # returns a list of dictionaries, hence [index][key]
        word = [roman[0]['hepburn']]    # listizing the words
        if 5 < len(word[0]) < 7:    # sorting
            romaji.append(word)
    return romaji
    # end = time.perf_counter()
    # print(f'{end - start:.5f} seconds') # so basically doesn't take a while luckily


# validates user input and returns order/index for each password element
def validate_order_input(element, valid_range):
    flag = False
    while not flag:
        if len(element) > 1:
            order = input(f'Order the block of custom characters from {char_dictionary[element[0].__name__]} within your password:\n')
            try:
                order = int(order)
            except ValueError:
                print('Try with an integer within the expected range.')
        else:
            order = input(f'Order the block of {element[0]} within your password:\n')
            try:
                order = int(order)
            except ValueError:
                print('Try with an integer within the expected range.')
        if order not in valid_range:
            print('Try with an integer within the expected range.')
        else:
            flag = True
            return order


# displays the blocks that will be included in the user's password
def display_segments(lst):
    print('The following blocks will be included in your password:')
    for element in lst:
        if len(element) > 1:
            print(char_dictionary[element[0].__name__])
        else:
            print(element[0])


'''def ordering(lst):
    to_order = []
    print('Number the following elements corresponding to the order in which they should generate.')
    for element in lst:
        to_order.append([element[0], 0])
    for element in to_order:




def password_display(lst):
    init = False
    if not init:    # building initial display
        display = ['____']
        p_length = len(lst)
        for n in range(0, p_length - 1):
            display.append("+____")

    print(f'Current password configuration: \n {}')'''

