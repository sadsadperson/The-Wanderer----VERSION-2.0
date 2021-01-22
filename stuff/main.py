### IMPORTS ###
import time
import util
import database
import battle
from colorama import Fore, Back, Style
from secret_lib_thing import print_file
import my_map
import battle
import curses
import os
import skirmish
##################
## PLAYER VAR   ##
##################
player = {
    'life' : 25,
    'gold' : 25,
    'life_regen' : 25,
    'carry_ability' : 5,
    'current_weight' : 0,
    'main_weapon' : 'Fist',
    'main_weapon_min' : 1,
    'main_weapon_max' : 1,
    'main_weapon_ammo' : 'infinite',
    'arrows' : 0,
    'shield' : 'None',
    'shield_defense' : 0,
    'armor' : 'Skin',
    'armor_min' : 1,
    'armor_max' : 1,
    'kills' : [],
    'monster_parts' : [],
    'weapons' : [],
    'shields' : [],
    'armors' : [],
    'specialty1' : '',
    'specialty2' : '',
    'specialty1_level' : 0,
    'specialty2_level' : 0,
    'location' : 'Kreiten Castle',
    'bad_points' : 0,
    'good_points' : 0,
    'level' : 0,
    'next_level' : 25,
    'xp' : 0, #your xp will go up really really as you to the first few missions that are easier
    'name' : '',
    'unlocked_locations' : ['Kreiten Castle', 'The Wastes', 'Iron Clan Lands'],
	# MISSIONS
	'mission1' : False,
	'mission2' : False,
	'mission3' : False,
	'mission4' : False,
	'mission5' : False,
	'mission6' : False,
	'mission7' : False,
	'mission8' : False,
	'mission9' : False,
	'mission10' : False,
	'mission11' : False,
	'mission12' : False,
	'mission13' : False,
	'mission14' : False,
	'mission15' : False,
	'mission16' : False,
    ## We can add more here
	'team' : {'name' : '', 'level' : 0, 'helpers' : [], 'wins' : 0, 'loses' : 0}
	### skill stats
	'skills' : {
		'sword_kills' : 0,
		'spear_kills' : 0,
		'bow_kills' : 0,
		'specialty_kills' : 0,
		'thug_kills' : 0,
		'thorg_kills' : 0,
		'heals' : 0,
	}
}

PURPLE = '\033[95m'
CYAN = '\033[96m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'
FAINT =  '\033[2m'
NORMAL = '\033[22m'

###################
# WEIRD FUNCTIONS #
###################

def print_user():
    global player
    while True:
        util.clear()
        database.save(player)
        ### STRINGIGY BELOW 
        print(Style.RESET_ALL + GREEN + BOLD + UNDERLINE + 'CURRENT RIG')
        print(Style.RESET_ALL + Fore.GREEN + 'LIFE ' + str(player['life']))
        print("CARRYING WEIGHT: " + str(player['current_weight']))
        print("MAIN WEAPON: " + player['main_weapon'] + ' | MIN DAMAGE: ' + str(player['main_weapon_min']) + ' | MAX DAMAGE: ' + str(player['main_weapon_max']) + ' | AMMO: ' + str(player['main_weapon_ammo']))
        print("SHIELD: " + player['shield'] + ' | DEFENSE: ' + str(player['shield_defense']))
        print("ARMOR: " + player['armor'] + ' | MIN DEFENSE: ' + str(player['armor_min']) + ' | MAX DEFENSE: ' + str(player['armor_max']))
        print("[1] Equip weapons/armor/shields")
        print("[2] Unequip All")
        print("[3] View Kills")
        print("[4] View Monsterparts")
        print("[5] Inventory overview")
        print("[6] Clean Inventory [Removes duplicates of weapons/shields/armor]")
        print('[7] Exit')
        i = input()
        if i == '1':
            print("[1] Equip Weapons")
            print("[2] Equip Shields")
            print("[3] Equip Armor")
            b = input()
            if b == '1':
                ###### EQUIP WEAPONS ########
                count = 0
                print(Style.RESET_ALL + Back.BLUE + "  WEAPONS  " + Style.RESET_ALL)
                for weapon in player['weapons']:
                    print(Style.RESET_ALL + Fore.GREEN + '[' + str(count) + ']  ' + weapon + ' | DAMAGE: ' + str(util.get_stat_max(weapon)) + ' | WEIGHT: ' + str(util.get_weight(weapon)))
                    count += 1
                choice = input()
                try:
                    new_weapon = player['weapons'][int(choice)]
                    if player['current_weight'] + util.get_weight(new_weapon) > player['carry_ability']: #checks if player is carrying too much weight
                        print("You are carrying too much weight!")
                        
                    else:
                        player['main_weapon'] = new_weapon
                        player['main_weapon_min'] = util.get_stat_min(player['main_weapon'])
                        player['main_weapon_max'] = util.get_stat_max(player['main_weapon'])
                        player['current_weight'] += util.get_weight(new_weapon)
                        player['ammo'] = util.get_ammo(player, new_weapon)
                except:
                    print("Not an option!")
            elif b == '2':
                ######## EQUIP SHIELDS #########
                count = 0
                print(Style.RESET_ALL + Back.BLUE + "  SHIELDS  " + Style.RESET_ALL)
                for shield in player['shields']:
                    print(Style.RESET_ALL + Fore.GREEN + '[' + str(count) + ']  ' + shield + ' | DEFENSE: ' + str(util.get_shield_stat_max(shield)) + ' | WEIGHT: ' + str(util.get_weight(shield)))
                    count += 1
                choice = input()
                try:
                    new_shield = player['shields'][int(choice)]
                    if player['current_weight'] + util.get_weight(new_shield) > player['carry_ability']:
                        print("You are carrying too much weight!")
                    else:
                        player['shield'] = new_shield
                        player['shield_defense'] = util.get_shield_stat_max(new_shield)
                        player['current_weight'] += util.get_weight(new_shield)
                except:
                    print("Error! Unable to equip item!")
            elif b == '3':
                ######## EQUIP ARMOR ########
                count = 0
                print(Style.RESET_ALL + Back.BLUE + '  ARMOR  ' + Style.RESET_ALL)
                for armor in player['armors']:
                    print(Style.RESET_ALL + Fore.GREEN + '[' + str(count) + ']  ' + armor + ' | MIN DEFENSE: ' + str(util.get_armor_stat_min(armor)) + ' | MAX DEFENSE: ' + str(util.get_armor_stat_max(armor)) + ' | WEIGHT: ' + str(util.get_weight(armor)))
                    count += 1
                choice = input()
                try:
                    new_armor = player['armors'][int(choice)]
                    if player['current_weight'] + util.get_weight(new_armor) > player['carry_ability']:
                        print("You cannot carry that much weight")
                    else:
                        player['armor'] = new_armor
                        player['armor_min'] = util.get_armor_stat_min(new_armor)
                        player['armor_max'] = util.get_armor_stat_max(new_armor)
                        player['current_weight'] += util.get_weight(new_armor)
                except:
                    print("Error! Could not equip item!")
            else:
                print("Not a choice!")
            input()
        elif i == '2':
            player['main_weapon'] = 'Fist'
            player['main_weapon_min'] = 1
            player['main_weapon_max'] = 1
            player['shield'] = 'None'
            player['shield_defense'] = 0
            player['armor'] = 'Skin'
            player['armor_min'] = 1
            player['armor_max'] = 1
            player['current_weight'] = 0
            print("All items unequped!")
            input()
        elif i == '3':
            print(Style.RESET_ALL + UNDERLINE + BOLD + Fore.BLUE + '  KILLS  ' + Style.RESET_ALL)
            for kill in player['kills']:
                print(Fore.GREEN + '  -  ' + kill)
            input()
        elif i == '4':
            print(Style.RESET_ALL + UNDERLINE + BOLD + Fore.BLUE + '  MONSTER PARTS  ' + Style.RESET_ALL)
            for part in player['monster_parts']:
                print(Fore.GREEN + '  -  ' + part)
            input()
        elif i == '7':
            break
        elif i == '5':
            print(GREEN + BOLD + UNDERLINE + '         ~ STATS ~         ' + Style.RESET_ALL)
            print(Style.RESET_ALL + Fore.GREEN + 'LIFE ' + str(player['life']))
            print("You are currently: " + util.get_good_bad(player))
            print("CARRYING WEIGHT: " + str(player['current_weight']))
            print("MAIN WEAPON: " + player['main_weapon'] + ' | MIN DAMAGE: ' + str(player['main_weapon_min']) + ' | MAX DAMAGE: ' + str(player['main_weapon_max']) + ' | AMMO: ' + str(player['main_weapon_ammo']))
            print("SHIELD: " + player['shield'] + ' | DEFENSE: ' + str(player['shield_defense']))
            print("ARMOR: " + player['armor'] + ' | MIN DEFENSE: ' + str(player['armor_min']) + ' | MAX DEFENSE: ' + str(player['armor_max']))
            print(GREEN + BOLD + UNDERLINE + '     ~ ALL INVENTORY ~     ')
            print(Style.RESET_ALL + CYAN + BOLD + '  WEAPONS  ' + Style.RESET_ALL)
            for weapon in player['weapons']:
                print(Fore.BLUE + weapon)
            print(Style.RESET_ALL + CYAN + BOLD + '  SHIELDS  ' + Style.RESET_ALL)
            for shield in player['shields']:
                print(Fore.BLUE + shield)
            print(Style.RESET_ALL + CYAN + BOLD + '  ARMOR  ' + Style.RESET_ALL)
            for a in player['armors']:
                print(Fore.BLUE + a)
            print(Style.RESET_ALL + CYAN + BOLD + '  KILLS  ' + Style.RESET_ALL)
            print("Goblin: " + str(util.count_list(player['kills'], 'Goblin')))
            print("Orc: " + str(util.count_list(player['kills'], 'Orc')))
            print("Troll: " + str(util.count_list(player['kills'], 'Troll')))
            print("Kraveb: " + str(util.count_list(player['kills'], 'kraveb')))
            print("Thorg: " + str(util.count_list(player['kills'], 'thorg')))
            for k in player['kills']:
                if k not in ('kraveb', 'Goblin', 'Orc', 'thorg', 'Troll'):
                    print(Fore.BLUE + k)
            print(Style.RESET_ALL + CYAN + BOLD + '  MONSTER PARTS  ' + Style.RESET_ALL)
            for part in player['monster_parts']:
                print(Fore.BLUE + part)
            print(Style.RESET_ALL + CYAN + BOLD + '  MISSIONS  ' + Style.RESET_ALL)
            print(Fore.BLUE + "Mission 1: " + str(player['mission1']))
            print("Mission 2: " + str(player['mission2']))
            print("Mission 3: " + str(player['mission3']))
            print("Mission 4: " + str(player['mission4']))
            print("Mission 5: " + str(player['mission5']))
            print("Mission 6: " + str(player['mission6']))
            print("Mission 7: " + str(player['mission7']))
            print("Mission 8: " + str(player['mission8']))
            print("Mission 9: " + str(player['mission9']))
            print("Mission 10: " + str(player['mission10']))
            print("Mission 11 (Optional): " + str(player['mission11']))
            print("Mission 12 (Optional): " + str(player['mission12']))
            print("Mission 13 (Optional): " + str(player['mission13']))
            print("Mission 14 (Optional): " + str(player['mission14']))
            print("Mission 15 (Optional): " + str(player['mission15']))
            print("Mission 16 (Optional): " + str(player['mission16']))
            print(Style.RESET_ALL + CYAN + BOLD + '  SKILLS  ' + Style.RESET_ALL)
            print(Fore.BLUE + 'SKILL ONE: ' + player['specialty1'] + ' | LEVEL: ' + str(player['specialty1_level']))
            print('SKILL TWO: ' + player['specialty2'] + ' | LEVEL: ' + str(player['specialty2_level']))
            input()
        elif i == '6':
            player = util.clean(player)
			




###################
#     INTRO       #
###################
while True:
    print(GREEN + BOLD + "Welcome, Have you played before?")
    i = input(NORMAL + ITALIC + BOLD + '[1] Yes | [2] No' + Style.RESET_ALL + Fore.GREEN)
    if i == '1':
        user = input("Username: ")
        try:
            player = database.restore(user)
            break
        except:
            print("Not a user!")
    elif i == 'delete':
        password = input("Password: ")
        if password == os.getenv('SECRET_PASSWORD'):
            database.admin_delete_all()
    else:
        user = input("Username: ")
        win = database.does_user_exist(user)
        if win == False:
            player['name'] = user
            database.save(player)
            print("User created!")
            #intro goes here
            print(GREEN + "Now, time to choose your two skills brave travelor")
            print("The skills you can choose from are: ")
            while True:
                print(BOLD + GREEN + "[1] Swordsmen -- Extra Damage with sword attacks")
                print("[2] Archer -- Extra Damage with bow attacks")
                print("[3] Healer -- Extra Health")
                print("[4] Thorgslayer -- Extra Damage against thorgs")
                print("[5] Thug -- Extra Damage with brute force weapons")
                print("[6] Spearmen -- Extra Damage with spears")
                print("[7] Specialist -- Hyper damage with Sharp Stick")
                choice1 = input("Choose a skill: ")
                choice2 = input("Choose another skill: ")
                player['specialty1'] = database.set_skill(choice1)
                player['specialty2'] = database.set_skill(choice2)
                print("Done!")
                database.save(player)
                break
            break
        else:
            print("User already exists!")

###########
# PLAYING #
###########
playing = True
while playing:
    player['specialty1_level'] = util.get_specialty1_level(player)
    player['specialty2_level'] = util.get_specialty2_level(player)
    database.save(player)
    util.clear()
    print(Style.RESET_ALL + BOLD + GREEN + UNDERLINE + "LOCATION: " + player['location'] + ' | LIFE: ' + str(player['life']) + ' | GOLD: ' + str(player['gold']))
    print(Style.RESET_ALL + NORMAL + CYAN + '')
    print('[1] View Inventory/Equip items')
    print('[2] Travel')
    print('[3] Look Around')
    print("[4] Skirmish")
    choice = input()
    if choice == '1':
        print_user()
    elif choice == '2':
        count = 0
        for location in player['unlocked_locations']:
            print(CYAN + '[' + str(count) + '] ' + location)
            count += 1
        n = int(input())
        if player['unlocked_locations'][n] != player['location']:
            player['location'] = player['unlocked_locations'][n]
            print("Traveling...")
            time.sleep(2)
            util.clear()
            print("You have arrived!")
            input()
        else:
            print("You are already in that location!")
            input()


    elif choice == '3':
        ## Check player location
        if player['location'] == 'Kreiten Castle':
            my_map.kreiten_castle(player)
        elif player['location'] == 'The Wastes':
          my_map.the_wastes(player)
        elif player['location'] == 'Monster Lands':
          my_map.monster_lands(player)
        elif player['location'] == 'Far Lands':
          my_map.far_lands(player)
        elif player['location'] == 'Beggar City':
          my_map.beggar_city(player)
    elif choice == 'hack':
        util.hack(player)
    elif choice == 'mayhem':
        util.mahem(player)
    elif choice == '4':
        skirmish.skirmish(player)
    else:
        print(RED + "Error! Not a choice!")
                