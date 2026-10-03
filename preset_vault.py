from account_class import *


def preset_vault(vault):
    p1 = Profile('Github', 'jrama552', '', ['Programming', 'School'])
    p2 = Profile('Spotify', 'jiror', '', ['Entertainment'])
    p3 = Profile('MyUCLA', 'Joe', '', ['School', 'Career'])
    p_N = [p1, p2, p3]
    for x in p_N:
        vault.append(x)

