from main_functions import *
import time
import os

start = time.perf_counter()

# future project: automate lists and functions
init_list = [
    #['en_wordlist.json', init_en],
    ['jp_wordlist.csv', init_jp]
]


# pulling the lists to use
source_files = [[item[0]] for item in init_list]
# elements within password
char_list = [
    [gen_hexadec, 2],
    [gen_num, 2],
    [gen_spchar, 1]
    # [gen_function, number of characters]
]


# if file already exists, do nothing
if __name__ == '__main__':
    for file, init in init_list:
        if not os.path.exists(file):
            init()
    # get everything below cleaned up and out of main ideally
    generate = True
    session_save = []
    t = 0
    while generate:
        generate = gen_prompt(t)
        if not generate:
            break
        word = gen_pword((order_el(source_files, char_list)))
        session_save = save_prompt(word)
        t += 1
    dis_saved(session_save)

end = time.perf_counter()
print(f'\n{end - start:.5f} seconds')


# LEFT OFF: SEE CLAUDE (lol)
# 1. seperate functions (clean up so each func is only doing
# one thing)
# 2. clean up functions (out of main)
# 3. other center (search, remove, assign passwords to 'account')
# 4. save account/password pairs (password notepad) to file and retrieve
# 5. ask user for input (what do you want to generate w/ (i.e. the
# actual customization and modular part of the pword generation)
