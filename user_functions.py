from pword_config import *


# gen pword and assign to new profile
def generate_password():
    session_save = []
    account = True
    while account:


    generate = True
    while generate:
        word = gen_pword((order_el(source_files, char_list)))
        session_save = save_word(save_prompt(word), word, session_save)
        generate = gen_prompt()

    # now, we need to assignt to a profile, and ask user to fill in information display_save(session_save)

