import secrets
import string

char_dictionary = {
    'gen_hexacosa': 'Alphabet + Digits 0-9',
    'gen_nonalpha': 'Special characters + Digits 0-9',
    'gen_digits': 'Digits 0-9',
    'gen_hexadec': 'Letters A-F + Digits 0-9',
    'gen_punc': 'Special subset of special characters'
    # 'gen_alpha': 'Alphabet',
    # 'gen_spchar': 'Special characters',
    # 'gen_all': 'Alphabet + Digits 0-9 + Special Characters'
}


# gen two characters with random digits + alpha
def gen_hexacosa(N):
    hexacosa = string.ascii_letters + string.digits
    return ''.join(secrets.choice(hexacosa) for n in range(0, N))


# gen three characters with special characters + digits
def gen_nonalpha(N):
    nonalpha = string.digits + string.punctuation
    return ''.join(secrets.choice(nonalpha) for n in range(0, N))


def gen_num(N):
    num = string.digits
    return ''.join(secrets.choice(num) for n in range(0, N))


def gen_spchar(N):
    special = string.punctuation    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    return ''.join(secrets.choice(special) for n in range(0, N))


def gen_hexadec(N):
    hexadec = string.hexdigits
    return ''.join(secrets.choice(hexadec) for n in range(0, N))


def gen_punc(N):
    special = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    lst = ['{', '}', "|", '[', ']', '/', '(', ')', '\\', '`', ',']
    for x in lst:
        special = special.replace(x, '')
    return ''.join(secrets.choice(special) for n in range(0, N))
