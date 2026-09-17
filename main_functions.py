from user_functions import *


# ------------------------------------------action center-------------------------------------------------


def user_action():
    flag = False
    while not flag:
        actions = ['g', 'v', 'e', 'ex']
        intent = input('What do you want to do?\n[g]enerate password, '
                       '[v]iew saved passwords, [e]dit saved passwords, [ex]it\n')
        if not intent.lower() in actions:
            print("Answer must be 'g', 'v', 'e', or 'ex'.")
        else:
            print(f'user intent: {intent}')
            flag = True
            return intent


def direct_user(intent):
    if intent == 'g':
        print(f'intent: generate password')
        generate_password()
        return True
    elif intent == 'v':
        print(f'intent: {intent}')
        # function
        return True
    elif intent == 'e':
        print(f'intent: {intent}')
        # function
        return True
    else:
        return False


