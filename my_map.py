import util
from colorama import Fore, Back, Style
from getch import getch
import shop
import secret_lib_thing
import ai_talk
import battle
### MAP ###
#maps should be a list of lists, they should be 30 characters wide by 30 characters high
#maps shoudl always be bordered by | and _
# | and _ are symbols the the player will not be able to go through, so they can be used as walls and roads if the player needs to keep on a road.

def listify(x):
    return [char for char in x]
def mapify(map_str):
    with open('maps/'+map_str, 'r') as file:
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
			elif i == 'M':
					out += Back.RED + ' 👺 ' + Style.RESET_ALL
		print(out)
def kreiten_castle(player):
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
		if the_map[y][x] not in ('S', 'L', 'P', '|', '_', 'K', 'A'):
			the_map[y][x] = 'player'
		elif the_map[y][x] == 'S':
			shop.shop(player)
		elif the_map[y][x] == 'P':
			pass
		elif the_map[y][x] == 'L':
			secret_lib_thing.library()
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
    

