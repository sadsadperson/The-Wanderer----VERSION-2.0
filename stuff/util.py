import os
import sys
import time
from colorama import Fore, Back, Style
import database
### UTIL ####
'''
This is a file for all the utility items we want to use, such as slow_print, clear, etc.
'''
def clear():
    os.system('clear')


def slow_print(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)
    print()

# Talk funciton is used for poeple talking to player
def talk(x):
    slow_print(Fore.BLUE + Style.BRIGHT + x + Style.RESET_ALL)

# Mission is for when a mission is being explained to the player
def mission(x):
    slow_print(Fore.GREEN + Style.BRIGHT + x + Style.RESET_ALL)

#get weapon stats
def get_stat_min(weapon): #returns the minimum damage of a weapon
    if weapon == 'Sword':
        return 1
    elif weapon == 'Fire Blade':
        return 2
    elif weapon == 'Kraveb Dagger':
        return 3
    elif weapon == 'Kraveb Battle Axe':
        return 12
    elif weapon == 'Ice Pick':
        return 8
    elif weapon == 'Long Sword':
        return 10
    elif weapon == 'Heavy Wooden Clobberstick':
        return 1
    elif weapon == 'Dragon Slayer':
        return 12
    elif weapon == 'Lightening Blade':
        return 10
    elif weapon == 'Rat Dagger':
        return 8
    elif weapon == 'Thorg War Axe':
        return 20
    elif weapon == 'Yeckity Toe Slizzer':
        return 15
    elif weapon == 'Sharp Stick':
        return 1
    elif weapon == 'Bow':
        return 5
    elif weapon == 'Kraveb Crossbow':
        return 10
    elif weapon == 'Street Crossbow':
        return 8
    elif weapon == 'Lightening Bow':
        return 12
    elif weapon == 'Thorg War Bow':
        return 25
    elif weapon == 'Spear':
        return 8
    elif weapon == 'Kraveb Heavy Spear':
        return 18
    elif weapon == 'Rat Spear':
        return 10
    elif weapon == 'Thorg War Spear':
        return 80
    elif weapon == 'Yeckity Toe Throwing Spear':
        return 15
    else:
        return "a;ldkjf;aldjf;lakjd;f"
def get_stat_max(weapon):
    if weapon == 'Sword':
        return 3
    elif weapon == 'Fire Blade':
        return 4
    elif weapon == 'Kraveb Dagger':
        return 8
    elif weapon == 'Kraveb Battle Axe':
        return 20
    elif weapon == 'Ice Pick':
        return 12
    elif weapon == 'Long Sword':
        return 15
    elif weapon == 'Heavy Wooden Clobberstick':
        return 30
    elif weapon == 'Dragon Slayer':
        return 18
    elif weapon == 'Lightening Blade':
        return 15
    elif weapon == 'Rat Dagger':
        return 10
    elif weapon == 'Thorg War Axe':
        return 40
    elif weapon == 'Yeckity Toe Slizzer':
        return 20
    elif weapon == 'Sharp Stick':
        return 30
    elif weapon == 'Bow':
        return 10
    elif weapon == 'Kraveb Crossbow':
        return 15
    elif weapon == 'Street Crossbow':
        return 12
    elif weapon == 'Lightening Bow':
        return 18
    elif weapon == 'Thorg War Bow':
        return 50
    elif weapon == 'Spear':
        return 8
    elif weapon == 'Kraveb Heavy Spear':
        return 18
    elif weapon == 'Rat Spear':
        return 10
    elif weapon == 'Thorg War Spear':
        return 80
    elif weapon == 'Yeckity Toe Throwing Spear':
        return 15
    else:
        return "a;ldkjf;aldjf;lakjd;f"
def get_shield_stat_max(s):
    if s == 'Shield':
        return 5
    elif s == 'Light Shield':
        return 3
    elif s == 'Kraveb Plastic Shield':
        return 1
    elif s == 'Dragon Scale Shield':
        return 10
    elif s == 'Thorg War Shield':
        return 25
def get_shield_weight_stat(s):
    if s == 'Shield':
        return 2
    elif s == 'Light Shield':
        return 1
    elif s == 'Kraveb Plastic Shield':
        return 0
    elif s == 'Dragon Scale Shield':
        return 2
    elif s == 'Thorg War Shield':
        return 4
def get_armor_stat_max(a):
    if a == 'Armor':
        return 4
    elif a == 'Fire Armor':
        return 8
    elif a == 'Wooden Armor':
        return 1
    elif a == 'Kraveb Chest Plate':
        return 10
    elif a == 'Ice Armor':
        return 20
    elif a == 'Thorg War Armor':
        return 20
    elif a == 'Chainmail':
        return 10
def get_armor_stat_min(a):
    if a == 'Armor':
        return 2
    elif a == 'Fire Armor':
        return 3
    elif a == 'Wooden Armor':
        return 1
    elif a == 'Kraveb Chest Plate':
        return 4
    elif a == 'Ice Armor':
        return 1
    elif a == 'Thorg War Armor':
        return 10
    elif a == 'Chainmail':
        return 5
def get_weight(item):
    if item == 'Sword':
        return 1
    elif item == 'Fire Blade':
        return 2
    elif item == 'Kraveb Dagger':
        return 1
    elif item == 'Kraveb Battle Axe':
        return 5
    elif item == 'Ice Pick':
        return 3
    elif item == 'Long Sword':
        return 3
    elif item == 'Heavy Wooden Clobberstick':
        return 5
    elif item == 'Dragon Slayer':
        return 3
    elif item == 'Lightening Blade':
        return 1
    elif item == 'Rat Dagger':
        return 0
    elif item == 'Thorg War Axe':
        return 5
    elif item == 'Yeckity Toe Slizzer':
        return 2
    elif item == 'Sharp Stick':
        return 0
    elif item == 'Bow':
        return 3
    elif item == 'Kraveb Crossbow':
        return 5
    elif item == 'Street Crossbow':
        return 3
    elif item == 'Lightening Bow':
        return 2
    elif item == 'Thorg War Bow':
        return 5
    elif item == 'Spear':
        return 1
    elif item == 'Kraveb Heavy Spear':
        return 2
    elif item == 'Rat Spear':
        return 1
    elif item == 'Thorg War Spear':
        return 5
    elif item == 'Yeckity Toe Throwing Spear':
        return 1
    elif item == 'Shield':
        return 2
    elif item == 'Light Shield':
        return 1
    elif item == 'Kraveb Plastic Shield':
        return 0
    elif item == 'Dragon Scale Shield':
        return 2
    elif item == 'Thorg War Shield':
        return 4
    elif item == 'Armor':
        return 2
    elif item == 'Fire Armor':
        return 3
    elif item == 'Wooden Armor':
        return 0
    elif item == 'Kraveb Chest Plate':
        return 4
    elif item == 'Ice Armor':
        return 4
    elif item == 'Thorg War Armor':
        return 5
    elif item == 'Chainmail':
        return 1

def get_level(xp):
    if xp >= 5000:
        return 25
    elif xp >= 4500:
        return 24
    elif xp >= 4000:
        return 23
    elif xp >= 3500:
        return 22
    elif xp >= 3000:
        return 21
    elif xp >= 2500:
        return 20
    elif xp >= 2250:
        return 19
    elif xp >= 2000:
        return 18
    elif xp >= 1750:
        return 17
    elif xp >= 1500:
        return 16
    elif xp >= 1250:
        return 15
    elif xp >= 1150:
        return 14
    elif xp >= 1050:
        return 13
    elif xp >= 950:
        return 12
    elif xp >= 850:
        return 11
    elif xp >= 750:
        return 10
    elif xp >= 700:
        return 9
    elif xp >= 650:
        return 8
    elif xp >= 600:
        return 7
    elif xp >= 550:
        return 6
    elif xp >= 500:
        return 5
    elif xp >= 450:
        return 4
    elif xp >= 400:
        return 3
    elif xp >= 350:
        return 2
    elif xp >= 300:
        return 1
    elif xp <= 300:
        return 0
def get_ammo(player, weapon):
    if weapon in ('Bow', 'Kraveb Crossbow', 'Street Crossbow', 'Lightening Bow', 'Thorg War Bow'):
        return player['ammo']
    else:
        return ('Infinite')
def format_print(table_data):
    for row in table_data:
        print("{: >20} {: >20} {: >20}".format(*row))
def rem_dup(target):
	out = []
	for x in target:
		if x not in out:
			out.append(x)
	return out
def clean(player):
	player['weapons'] = rem_dup(player['weapons'])
	player['shields'] = rem_dup(player['shields'])
	player['armors'] = rem_dup(player['armors'])
	return player
def list_count(target):
	t = 0
	for x in target:
		t += 1
	return t
def list_count_special(target, value):
	t = 0
	for x in target:
		if x == value:
			t += 1
	return t

def get_specialty1_level(player):
	level = 1
	if player['specialty1'] == 'Swordsmen':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty1'] == 'Archer':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty1'] == 'Spearmen':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty1'] == 'Healer':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty1'] == 'Thorgslayer':
		count = list_count_special(player['kills'], 'thorg')
		if count >= 80:
			level = 10
		elif count >= 70:
			level = 9
		elif count >= 60:
			level =  8
		elif count >= 50:
			level = 7
		elif count >= 40:
			level = 6
		elif count >= 30:
			level = 5
		elif count >= 20:
			level = 4
		elif count >= 10:
			level = 3
		elif count >= 5:
			level = 2
		elif count <= 2:
			level = 1
		return level
	elif player['specialty1'] == 'Thug':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty1'] == 'Specialist':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level

###################################################
###################################################
###################################################

def get_specialty2_level(player):
	level = 1
	if player['specialty2'] == 'Swordsmen':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty2'] == 'Archer':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty2'] == 'Spearmen':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty2'] == 'Healer':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty2'] == 'Thorgslayer':
		count = list_count_special(player['kills'], 'thorg')
		if count >= 80:
			level = 10
		elif count >= 70:
			level = 9
		elif count >= 60:
			level =  8
		elif count >= 50:
			level = 7
		elif count >= 40:
			level = 6
		elif count >= 30:
			level = 5
		elif count >= 20:
			level = 4
		elif count >= 10:
			level = 3
		elif count >= 5:
			level = 2
		elif count <= 2:
			level = 1
		return level
	elif player['specialty2'] == 'Thug':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
	elif player['specialty2'] == 'Specialist':
		count = list_count(player['kills'])
		if count >= 150:
			level = 10
		elif count >= 130:
			level = 9
		elif count >= 110:
			level =  8
		elif count >= 90:
			level = 7
		elif count >= 70:
			level = 6
		elif count >= 50:
			level = 5
		elif count >= 40:
			level = 4
		elif count >= 30:
			level = 3
		elif count >= 20:
			level = 2
		elif count <= 10:
			level = 1
		return level
def sentence(t):
	count = t
	while count != 0:
		clear()
		print("You have " + str(count) + ' seconds left in jail...')
		count += 1
def count_list(the_list, target_val):
	count = 0
	for item in the_list:
		if item == target_val:
			count += 1
	return count
def get_good_bad(player):
	if player['good_points'] > player['bad_points']:
		return 'On the path of light'
	elif player['bad_points'] > player['good_points']:
		return "On the path of darkness"
	elif player['bad_points'] == player['good_points']:
		return "Neither Good nor Bad"
all_armor = ['Armor', 'Fire Armor', 'Wodden Armor', 'Kraveb Chest Plate', 'Ice Armor', 'Thorg War Armor', 'Chainmail']
all_shields = ['Shield', 'Light Shield', 'Kraveb Plastic Shield', 'Dragon Scale Shield' ,'Thorg War Shield']
all_swords = ['Sword', 'Fire Blade', 'Kraveb Dagger', 'Kraveb Battle Axe', 'Ice Pick', 'Long Sword', 'Heavy Wooden Clobberstick', 'Dragon Slayer', 'Lightening Blade', 'Rat Daggar', 'Thorg War Axe', 'Yeckity Toe Slizzer', 'Sharp Stick']
def hack(player):
	while True:
		print("Welcome " + player['name'])
		print("What would you like to hack: ")
		print("[1] Add all weapons")
		print("[2] Add all shields")
		print("[3] Add all armor")
		print("[4] Add custom health")
		print("[5] Add locations")
		print("[6] Add Gold")
		print("[7] Exit hacks")
		choice = input()
		if choice == '1':
			for item in all_swords:
				player['weapons'].append(item)
		elif choice == '2':
			for item in all_shields:
				player['shields'].append(item)
		elif choice == '3':
			for item in all_armor:
				player['armors'].append(item)
		elif choice == '4':
			new_health = int(input("How much health would you like: "))
			player['life'] = new_health
		elif choice == '5':
			location = input("Location: ")
			player['unlocked_locations'].append(location)
		elif choice == '6':
			new_gold = int(input("Gold: "))
			player['gold'] += new_gold
		elif choice == '7':
			break
		database.save(player)
def mahem(player):
	while True:
		clear()
		i = input(Style.RESET_ALL + Back.WHITE + Fore.BLACK + 'Hack: ')
		if i == 'command':
			try:
				z = input(Back.WHITE + Fore.BLACK + 'Command: ')
				exec(z)
				print("Command run" + Style.RESET_ALL)
				input("Press enter to continue")
			except Exception as e:
				print(Fore.RED + "Could not run command!")
				print("Error: " + str(e) + Style.RESET_ALL)
				input("Press enter to continue")
		if i == 'leave':
			clear()
			break
def change_map(old_map, new_map):
	with open('maps/' + new_map, 'r') as file:
		new_data = file.read()
	with open('maps/' + old_map, 'w') as file:
		file.write(new_data)
def new_helper(player, a, b, c, d, e, f, g, h, i):
	"function(player, name, life, min_damage, max_damage, min_defense, max_defense, block, level, defeated_list)"
	new = {
		'name' : a,
		'life' : b,
		'min_damage' : c,
		'max_damage' : d,
		'min_defense' : e,
		'max_defense' : f,
		'block' : g,
		'level' : h,
		'defeated' : i,
	}
	player['team']['helpers'].append(new)
	database.save(player)