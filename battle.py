import random
import util
from colorama import Style


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


class create_t():
	def __init__(self, min_damage, max_damage, name, ttype, life, min_defense, max_defense, block, loot, weapon, defense):
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.name = name
		self.type = ttype
		self.life = life
		self.min_defense = min_defense
		self.max_defense = max_defense
		self.block = block
		self.weapon = weapon
		self.loot = loot
		self.defense = defense

goblin = {
	'min_damage' : [1,2,3],
	'max_damage' : [4,5,6],
	'names' : ['Glork', "Glemmo", "Snarg", 'Teyc', "Sncese", "Snozzle", "Flarms", "Technae", "Xcat", 'Flahg'],
	'health' : [10,11,12,13,14,15],
	'min_defense' : [1,2],
	'max_defense' : [2,3],
	'block' : [1,2,3,4],
	'loot' : ['Goblin Guts', 'Goblin Brain', 'Goblin Claws', 'Goblin Eye'],
	'weapons' : ['Sword', 'Spear'],
	'defense' : ['Shield', 'Armor'],
	'type' : 'Goblin'
}
orc = {
	'min_damage' : [2,3,4],
	'max_damage' : [5,6,7],
	'names' : ['Gluck', "Glurk", "Tlka", "Truken", "Thlgn", "Nrge", 'Rnre', "XCyne"],
	'health' : [12,16,17,18,19,20],
	'min_defense' : [2,3],
	'max_defense' : [4,5],
	'block' : [2,3,4,5],
	'loot' : ['Orc Guts', 'Org Eyes', 'Orc Brain', 'Orc Claws', 'Orc eyes', 'Orc hair'],
	'weapons' : ['Sword', "Spear"],
	'defense': ['Armor', 'Shield', 'Armor', 'Shield', 'Wooden Armor'],
	'type' : 'Orc'
}
troll = {
	'min_damage' : [1,2,3],
	'max_damage' : [6,7,8,9,10],
	'names' : ['Akch', 'SKf', "Elkf", 'Far', 'Erte', 'A;lkj', 'Eigh'],
	'health' : [12,16,17,18,19,20],
	'min_defense' : [4,5],
	'max_defense' : [6,7],
	'block' : [2,3,4,5],
	'loot' : ['Troll Head', 'Troll guts', 'Troll brain', 'Troll teeth', 'Troll eye'],
	'weapons' : ['Sword', "Spear", 'Bow', 'Sword', 'Sword', 'Sword', 'Spear', 'Fire Sword'],
	'defense': ['Armor', 'Shield', 'Armor', 'Armor', 'Armor', 'Shield', 'Shield', 'Fire Armor'],
	'type' : 'Troll'
}
kraveb = {
	'min_damage' : [5,6,7,8,9,10],
	'max_damage' : [11,12,13,14,15,16,17,18,19,20],
	'names' : ['Krorn', 'Hatch', 'Emote', "Trofff", "Grffhssk", 'Hegrrgrck', 'Grckbob', 'Snurfflesnrrk', 'Snorrrkenrreg'],
	'health' : [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
	'min_defense' : [4,5],
	'max_defense' : [6,7],
	'block' : [5,6,7,8,9,10],
	'loot' : ['Kraveb Head', 'Kraveb Guts', 'Kraveb Eye', 'Kraveb claws', 'Kraveb teeth'],
	'weapons' : ['Fire Sword', 'Kraveb Crossbow', 'Kraveb Heavy Spear', 'Kraveb Battle Axe', 'Kraveb Dagger'],
	'defense': ['Kraveb Chestplate', 'Kraveb Plastic Shield', 'Armor', 'Wooden Armor', 'Light Shield'],
	'type' : 'kraveb'
}
thorg = {
	'min_damage' : [10,11,12,13,14,15,16,17,18,19,20],
	'max_damage' : [21,22,23,24,25,26,27,28,29,30],
	'names' : ['Tem', 'Gerfensh', 'Arkg', 'Aher', 'Ahege', 'Hgen', 'Xhe', 'EYr', 'Che', 'Thgey', 'Cehre'],
	'health' : [31,32,33,34,35,36,37,38,39,40],
	'min_defense' : [5,6,7,8,9,10],
	'max_defense' : [11,12,13,14,15],
	'block' : [16,17,18,18,19,20,21,22,23,24,25],
	'loot' : ['Thorg head', 'Thorg Claws', 'Thorg guts'],
	'weapons' : ['Lightening Blade', 'Thorg War Axe', 'Thorg War Spear', 'Thorg War Bow', 'Dragon Slayer', 'Heavy Wooden Cudgel', 'Sharp Stick'],
	'defense': ['Thog War Armor', 'Thorg War Shield'],
	'type' : 'thorg'
}
monsters = [goblin, orc, troll, kraveb, thorg] #Add thug, duckswarm, grim quacker and others later
def get_enemy():
	i = random.choice(monsters)
	e = create_t(random.choice(i['min_damage']), random.choice(i['max_damage']), random.choice(i['names']), i['type'], random.choice(i['health']), random.choice(i['min_defense']), random.choice(i['max_defense']), random.choice(i['block']), random.choice(i['loot']), random.choice(i['weapons']), random.choice(i['defense']))
	return e
def battle(player):
	enemy = get_enemy()
	extra_damage = 0
	extra_health = 0
	if player['specialty1'] == 'Thorgslayer' and enemy.type == 'Thorg':
		extra_damage += 5 * player['specialty1_level']
	elif player['specialty1'] == 'Swordsmen' and player['main_weapon'] in ('Sword', 'Fire Blade', 'Ice Pick', 'Long Sword' 'Dragon Slayer', 'Lightening Blade', 'Yeckity Toe Slizzer'):
		extra_damage += 2 * player['specialty1_level']
	elif player['specialty1'] == 'Archer' and player['main_weapon'] in ('Bow', 'Kraveb Crossbow', 'Street Crossbow', 'Lightening Bow', 'Thorg War Bow'):
		extra_damage += 2 * player['specialty1_level']
	elif player['specialty1'] == 'Spearmen' and player['main_weapon'] in ('Spear', 'Kraveb Heavy Spear', 'Rat Spear', 'Thorg War Spear', 'Yeckity Toe Throwing Spear'):
		extra_damage += 2 * player['specialty1_level']
	elif player['specialty1'] == 'Thug' and player['main_weapon'] == 'Heavy Wooden Clobberstick':
		extra_damage += 5 * player['specialty1_level']
	elif player['specialty1'] == 'Healer':
		extra_health += 2 * player['specialty1_level']
	elif player['specialty1'] == 'Specialist' and player['main_weapon'] in ('Fists', 'Sharp Stick'):
		extra_damage += 5 * player['specialty1_level']
	

	#### BATTLE #####
	enemy_attack_1 = [' leaps and ', ' rolls and ', ' bellows and ', ' roars and ', ' dives and ', ' screams and ']
	enemy_attack_2 = ['vicously strikes you in the ', 'punches you in the ', 'kicks you in the ', 'elbows you in a ', 'slashes you in the ', 'stabs you in the ', 'hits you in the ', 'pokes you in the ']
	enemy_attack_3 = ['eye', 'face', 'stomach', 'head', 'mouth', 'throat', 'leg', 'arm', 'chest', 'nose', 'foot', 'hand', 'snozzle']
	scream = ['You scream ', 'You shout in pain ', 'You roar in anger ', 'You grunt in pain ', '']
	b = True
	while b == True:
		print(BOLD + UNDERLINE + GREEN + "LIFE: " + str(player['life']) + CYAN + ' | ' + RED + enemy.type + ' LIFE: ' + str(enemy.life) + Style.RESET_ALL)
		util.slow_print(CYAN + enemy.name + random.choice(enemy_attack_1) + random.choice(enemy_attack_2) + random.choice(enemy_attack_3))
		block = random.randint(1,3)
		damage_taken = random.randint(enemy.min_damage, enemy.max_damage)
		if block == 1:
			print(GREEN + "You block!")
			damage_taken -= player['shield_defense']
		damage_taken -= random.randint(player['armor_min'], player['armor_max'])
		util.slow_print(RED + random.choice(scream) + 'and take ' + str(damage_taken) + ' damage')
		player['life'] -= damage_taken
		util.slow_print("You attack with your " + player['main_weapon'])
		damage_given = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		block = random.randint(1,3)
		if block == 1:
			damage_given -= enemy.block
		damage_given -= random.randint(enemy.min_defense, enemy.max_defense)
		if damage_taken > 0:
			print(enemy.name + ' takes no damage!')
		else:
			enemy.life -= damage_given
		if enemy.life <= 0:
			print("Enemy defeated!")
			## get loot
			t = random.randint(1,5)
			loot = ''
			if t == 5:
				loot = enemy.weapon
				util.slow_print("You looted the body and got a " + loot)
				player['weapons'].append(loot)
			elif t == 4:
				loot = enemy.defense
				if loot in ('Armor', 'Fire Armor', 'Wooden Armor', 'Kraveb Chest Plate', 'Ice Armor', 'Thorg War Armor', 'Chainmail'):
					util.slow_print("You looted the body and got a " + loot)
					player['armors'].append(loot)
				else:
					util.slow_print("You looted the body and got a " + loot)
					player['shields'].append(loot)
			else:
				loot = enemy.loot
				util.slow_print("You looted the body and got " + loot)
				player['monster_parts'].append(loot)
		elif player['life'] <= 0:
			print("You have been defeated...")
			battle = False