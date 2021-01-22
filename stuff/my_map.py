import util
from colorama import Fore, Back, Style
from getch import getch
import shop
import secret_lib_thing
import ai_talk
import battle
import curses
import sell
import boss_fight
import multi_battle
### MAP ###
#maps should be a list of lists, they should be 30 characters wide by 30 characters high
#maps shoudl always be bordered by | and _
# | and _ are symbols the the player will not be able to go through, so they can be used as walls and roads if the player needs to keep on a road.
def listify(x):
    return [char for char in x]
def mapify(map_str):
    with open('stuff/maps/'+map_str, 'r') as file:
        raw = file.read()
    format1 = raw.split('\n')
    format2 = []
    for x in format1:
        z = listify(x)
        format2.append(z)
    return format2
def print_map(x):
	the_map = x
	for b in the_map:
		out = ''
		for i in b:
			if i == '|' or i == '_':
					out += Back.BLACK + '   ' + Style.RESET_ALL
			elif i == ' ':
					out += Back.WHITE + '   ' + Style.RESET_ALL
			elif i == 'L':
					out += Back.BLACK + ' 🏛 ' + Style.RESET_ALL
			elif i == 'S':
					out += Back.BLACK + ' 🏦 ' + Style.RESET_ALL
			elif i == 'P':
					out += Back.BLACK + ' 👤 ' + Style.RESET_ALL
			elif i == 'player':
					out += Back.BLACK + ' 🤺 ' + Style.RESET_ALL
			elif i == 'K':
					out += Back.YELLOW + Fore.BLACK + ' K ' + Style.RESET_ALL
			elif i == 't':
				out += Back.BLACK + ' 💰 ' + Style.RESET_ALL
			elif i == 'M':
					out += Back.RED + ' 👺 ' + Style.RESET_ALL
			elif i == 'B':
					out += Back.WHITE + ' ☠️ ' + Style.RESET_ALL
			elif i == 'D':
					out += Back.WHITE + ' 🦆 ' + Style.RESET_ALL
			elif i == 'Q':
					out += Back.WHITE + ' 💀 ' + Style.RESET_ALL
			elif i == 'G':
					out += Back.WHITE + ' 💂 ' + Style.RESET_ALL
			elif i == 'Z':
					out += Back.WHITE + ' 👁 ' + Style.RESET_ALL
			elif i == 'x':
					out += Back.WHITE + '   ' + Style.RESET_ALL
		print(out)
def kreiten_castle(player):
	if player['mission11'] == True:
		util.change_map('krieten_castle_map.txt', 'mission11_hack_map.txt')
	the_map = mapify('kreiten_castle_map.txt')
	print_map(the_map)
	x = 15
	y = 15
	while True:
		o_x = x
		o_y = y
		print("\033[H",end="")
		print_map(the_map)
		the_map[y][x] = ' '
		key_pressed = getch()
		if key_pressed == 'w':
			y -= 1
		elif key_pressed == 's':
			y += 1
		elif key_pressed == 'd':
			x += 1
		elif key_pressed == 'a':
			x -= 1
		elif key_pressed == 'l':
			break
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A', 't'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
		elif the_map[y][x] == 't':
			sell.sell(player)
		elif the_map[y][x] == 'K':
			ai_talk.king(player)
		else:
			x = o_x
			y = o_y
def the_wastes(player):
	the_map = mapify('the_wastes_map.txt')
	print_map(the_map)
	x = 15
	y = 15
	while True:
		o_x = x
		o_y = y
		print("\033[H",end="")
		print_map(the_map)
		the_map[y][x] = ' '
		key_pressed = getch()
		if key_pressed == 'w':
			y -= 1
		elif key_pressed == 's':
			y += 1
		elif key_pressed == 'd':
			x += 1
		elif key_pressed == 'a':
			x -= 1
		elif key_pressed == 'l':
			break
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A', 'M'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
		elif the_map[y][x] == 'M':
			battle.battle(player)
		else:
			x = o_x
			y = o_y
    

def monster_lands(player):
	the_map = mapify('monster_lands.txt')
	print_map(the_map)
	x = 15
	y = 15
	while True:
		o_x = x
		o_y = y
		print("\033[H",end="")
		print_map(the_map)
		the_map[y][x] = ' '
		key_pressed = getch()
		if key_pressed == 'w':
			y -= 1
		elif key_pressed == 's':
			y += 1
		elif key_pressed == 'd':
			x += 1
		elif key_pressed == 'a':
			x -= 1
		elif key_pressed == 'l':
			break
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A', 'M', 'B'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
		elif the_map[y][x] == 'M':
			battle.battle(player)
		elif the_map[y][x] == 'B':
			ai_talk.mega_rat(player)
		else:
			x = o_x
			y = o_y

def far_lands(player):
	the_map = mapify('far_lands.txt')
	print_map(the_map)
	x = 15
	y = 15
	while True:
		o_x = x
		o_y = y
		print("\033[H",end="")
		print_map(the_map)
		the_map[y][x] = ' '
		key_pressed = getch()
		if key_pressed == 'w':
			y -= 1
		elif key_pressed == 's':
			y += 1
		elif key_pressed == 'd':
			x += 1
		elif key_pressed == 'a':
			x -= 1
		elif key_pressed == 'l':
			break
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A', 'M', 'B', 'G', 'Z', 'Q', 'D'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
		elif the_map[y][x] == 'M':
			battle.battle(player)
		elif the_map[y][x] == 'D':
			multi_battle.duck_fight(player)
		elif the_map[y][x] == 'Q':
			boss_fight.grim_quacker(player)
		elif the_map[y][x] == 'G':
			boss_fight.guard(player)
		elif the_map[y][x] == 'Z':
			ai_talk.farlands(player)
		else:
			x = o_x
			y = o_y

def beggar_city(player):
	the_map = mapify('beggar_city.txt')
	print_map(the_map)
	x = 15
	y = 15
	while True:
		o_x = x
		o_y = y
		print("\033[H",end="")
		print_map(the_map)
		the_map[y][x] = ' '
		key_pressed = getch()
		if key_pressed == 'w':
			y -= 1
		elif key_pressed == 's':
			y += 1
		elif key_pressed == 'd':
			x += 1
		elif key_pressed == 'a':
			x -= 1
		elif key_pressed == 'l':
			break
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A', 'M', 'B', 'G', 'Z', 'Q', 'D', 'x'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
		elif the_map[y][x] == 'M':
			battle.battle(player)
		elif the_map[y][x] == 'D':
			multi_battle.duck_fight(player)
		elif the_map[y][x] == 'B':
			ai_talk.mega_rat(player)
		elif the_map[y][x] == 'Z':
			ai_talk.farlands(player)
		elif the_map[y][x] == 'x':
			boss_fight.gate_keeper(player)
		else:
			x = o_x
			y = o_y