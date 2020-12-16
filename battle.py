### BATTLE ###
def format(x): #used for formatting weapon/shield/armor data
    if len(x) > 18:
        while len(x) != 18:
            p = x.split()
            del p[-1]
            x = ''
            for letter in p:
                x += letter
        return x
    while len(x) != 18:
        x += ' '
    return x
def battle(enemy_list, player):
    win = False
    while win == False:
        ### ENEMY ATTACKS ###
        weapon = player.main_weapon
        if player.weapon_type == 'Bow':
            arrows = player.arrows
        else:
            arrows = ''
        shield = player.shield
        armor = player.armor
        main_weapon = format(weapon)
        extra_main_data = format(arrows)
        shield_data = format(shield)
        armor_data = format(armor)
        print('''
        _____________________________________________________________
        |                            |          EQUIPED GEAR        |
        |                            |[MAIN] ---- '''+main_weapon+'''|
        |                            |[AMMO] ---- '''+extra_main_data+'''|
        |                            |[SHIELD] -- '''+shield_data+'''|
        |                            |                              |
        |                            |[ARMOR] --- '''+armor_data+'''|
        |                            |                              |
        |                            |                              |
        |                            |                              |
        |___________________________________________________________|
        |                                                           |
        |                                                           |
        |'''+attack_text+'''|
        |                                                           |
        |                                                           |
        |___________________________________________________________|
        |                                                           |
        |          [1] ATTACK                                       |
        |          [2] RUN                                          |
        |                                                           |
        |___________________________________________________________|
        ''')