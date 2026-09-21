from account_class import *


def preset_vault(vault):
    p1 = Profile('Github', 'jrama552', '', ['Programming'])
    p2 = Profile('Spotify', 'jiror', '', ['Entertainment'])
    p_N = [p1, p2]
    for x in p_N:
        vault.append(x)

  
