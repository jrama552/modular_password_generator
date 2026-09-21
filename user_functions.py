from pword_config import *


# gen pword and assign to new profile
def generate_password(vault):
    generate = True
    while generate:
        word = gen_pword((order_el(source_files, char_list)))
        # reassign
        if user_reassign():
            # view all --> assigning new password
            if user_view():
                generate = view_assign(vault, word)
            # filter (search) --> assigning new password
            else:
                generate = view_assign(filter_search(filter_vault(), vault), word)
        for x in vault:
            x.printo()
        # creating new profile
        else:
            pass    # use profile_prompt

        '''vault = save_word(save_prompt(word), word, vault)
        generate = gen_prompt()'''


