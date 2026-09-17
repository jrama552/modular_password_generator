from pword_config import *


def generate_password():
    session_save = []
    generate = True
    while generate:
        word = gen_pword((order_el(source_files, char_list)))
        session_save = save_word(save_prompt(word), word, session_save)
        generate = gen_prompt()
    display_save(session_save)

