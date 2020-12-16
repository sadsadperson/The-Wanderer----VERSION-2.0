import os
import sys
import time
from colorama import Fore, Back, Style
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
