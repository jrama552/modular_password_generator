from aux_functions import *
from gen_functions import *
from english_words import get_english_words_set     # pip install english-words


# depending on whether we listize x, we get different json
def init_en():
    words = get_english_words_set(['web2'], lower=True)
    short_words = [[x] for x in words if 6 <= len(x) <= 8]
    write_file('en_wordlist.json', short_words)
    # print(read_file('en_wordlist.json'))


# cleans csv, extracts list, rewrites to clean csv
def init_jp():
    # clean csv
    clean_csv()
    # csv to list (extracting hirgana)
    jp = [row[1] for row in read_file('jp_dict.csv')]
    # translating
    romaji_jp = translator(jp)  # print(f'printing romaji list: \n{romaji_jp}')
    # writing file
    write_file('jp_wordlist.csv', romaji_jp)    # print(f' reading new wordlist: \n{read_file("jp_wordlist.csv")}')


def order_el(sources, characters):
    el_list = sources + characters  # list of [element, (number of char)]
    indexed_el = []     # list of [element, order/index]
    valid_range = [n for n in range(1, len(el_list) + 1)]
    display_segments(el_list)
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


def gen_prompt(count):
    deny = ['no', 'n']
    if count == 0:
        decision = input('Generate password?\n')
    else:
        decision = input('Generate another password?\n')
    if decision in deny:
        return False
    else:
        return True


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



