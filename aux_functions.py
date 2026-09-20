import json
import csv
import pykakasi     # pip install pykakasi
from gen_functions import *
from account_class import Profile


# --------------------------init files-----------------------------------


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

# -----------------------------password gen functions -----------------------------------------


def gen_pword(order):
    pword = ''
    for x in order:
        # sorting for functions; [[func, num], order]
        #                       x[0][0] x[0][1]  x[1]
        if len(x[0]) == 2:
            if callable(x[0][0]):
                pword += x[0][0](x[0][1])
        else:
            pword += secrets.choice(read_file(x[0]))[0]
    return pword


def profile_prompt():

    valid = False
    new = ['n']
    reassign = ['re']
    while not valid:
        decision = input('Generate password for [n]ew profile or [re]assign password to existing profile?')
        if decision.lower() in new:
            acc = input('Account/website name:\n')
            user = get_user()   # make an ever-extending list of usernames AND tags that user can add to at anytime
            tags = get_tags()   # tags should be a list; should also be accessing a list of pre-existing tabs
            new_profile = Profile(acc, user, '', tags)

            valid = True
        elif decision.lower() in reassign:
            # need to create a 'search' function first
            valid = True
            pass
        else:
            print("Respond with 'n' or 're'")


def get_user():     # most likely a list of pre-existing users
    return input('Username:\n')


def get_tags():     # most likely a list of pre-existing tags
    return input('Account tags')


# ---------------------------------------------------------------------------------------------------------------------

def order_el(sources, characters):
    el_list = sources + characters  # list of [element, (number of char)]
    indexed_el = []     # list of [element, order/index]
    valid_range = [n for n in range(1, len(el_list) + 1)]
    display_segments(el_list)
    testing = True  # true orders everything w/o manually asking everytime
    if testing:
        indexed_el = [[[gen_hexadec, 2], 1], ['en_wordlist.json', 2],
                      [[gen_num, 2], 3], [[gen_spchar, 1], 3]]
    else:
        for el in el_list:
            # seperating elements (source or characters)
            if len(el) > 1:
                # validates user input and returns index order for each 'block/element'
                order = validate_order_input(el, valid_range)
                indexed_el.append([[el[0], el[1]], order])
            else:
                order = validate_order_input(el, valid_range)
                indexed_el.append([el[0], order])
            valid_range.remove(int(order))
    return sorted(indexed_el, key=lambda x: x[1])


def gen_prompt():
    flag = True
    while flag:
        accept = ['yes', 'y']
        deny = ['no', 'n']
        decision = input('Generate another password?\n')
        if decision.lower() in deny:
            return False
        elif decision.lower() in accept:
            return True
        else:
            print('Answer with y/n')


def save_prompt(word):
    print(f'Generated password: {word}')
    answer = False
    while not answer:
        save_input = input('Save this password?\n').lower()
        accept = ['yes', 'y']
        deny = ['no', 'n']
        if save_input in accept:
            answer = True
            return True
        elif save_input in deny:
            answer = True
            return False
        else:
            print('Respond with yes or no.\n')


def save_word(value, word, lst):
    if value:
        lst.append(word)
        return lst


def display_save(savelist):
    if not savelist:
        print(f'Passwords saved to file: None')
    else:
        print(f'Password(s) saved to file:')
        for x in savelist:
            print(x)

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
            order = input(f'Order the block of custom characters from'
                          f' {char_dictionary[element[0].__name__]} within your password:\n')
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

# --------------------------------------------------------------------------------------------------
