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
    el_list = sources + characters
    # list containg pairs of (element, ordered index)
    # print('Number the following elements corresponding to the order in which they should generate.')
    indexed_el = []
    # N = len(el_list)
    for el in el_list:
        # seperating elements (source or characters)
        if len(el) > 1:
            element = el[0]    # .__name__    # string name of function
            # validate input
            # order = int(input(f'{char_dictionary[element]}: '))
            # to bypass manual input
            if element == gen_hexadec:
                order = 1
            else:
                if element == gen_num:
                    order = 3
                else:
                    order = 4
            indexed_el.append([[element, el[1]], order])
        else:
            source_el = el[0]   # extracting name of file
            # validate input
            # order = int(input(f'Word from {source_el}: '))
            # to bypass manual input
            if source_el == 'jp_wordlist.csv':
                order = 2
            else:
                order = 4
            indexed_el.append([source_el, order])
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
    save_list = []
    answer = False
    while not answer:
        save_input = input('Save this password?\n').lower()
        accept = ['yes', 'y']
        deny = ['no', 'n']
        if save_input in accept:
            save_list.append(word)
            print('Password saved to file.')
            answer = True
            return save_list
        elif save_input in deny:
            answer = True
            return save_list
        else:
            print('Respond with yes or no.\n')


def dis_saved(savelist):
    if len(savelist) == 0:
        print(f'Passwords saved to file: None')
    else:
        print(f'Password(s) saved to file:')
        for x in savelist:
            print(x)



