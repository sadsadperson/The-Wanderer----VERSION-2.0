import util, time, random, database, os
from colorama import Fore, Back, Style
attack_style = ['vicously', 'wildely', 'heriocly', 'dangerously', 'amazingly', 'savagly', 'strangly']

def get_max():
	class badguy():
		def __init__(self, title, health, defense, block, special_attack, special_attack_damage, attack, loot, phrase1, phrase2, phrase3):
			self.title = title
			self.health = health
			self.defense = defense
			self.block = block
			self.special_attack = special_attack
			self.special_attack_damage = special_attack_damage
			self.attack = attack
			self.loot = loot
			self.t1 = phrase1
			self.t2 = phrase2
			self.t3 = phrase3
	l1 = ['leaps and', 'dives and', 'charges and', 'backflips and', 'twirls and', 'spins and']
	l2 = ['kicks you', 'hacks you', 'stabs you', 'karate chops you', 'ninja kicks you', 'drop kicks you', 'cuts you']
	l3 = ['face', 'leg', 'arm', 'nose', 'eye', 'stomach', 'bum', 'chest', 'back', 'ear']
	out = badguy("Maximus the III", 100, random.randint(5,10), random.randint(10,20), 'Ultra Sword Strike', 50, random.randint(20,30), "Long Sword", l1, l2, l3)
	return out
def max_talk(player):
	from ai_talk import maxy, choice, you
	maxy("Hello there, " + player['name'] + ". You've come far... freind\n")
	you(player, "I'm here-")
	maxy("Yes yes, I know you are here to kill me\nBut is that really the best option?")
	maxy('You and I would make quite a team, if you would join me')
	you(player, "What are you talking about?")
	maxy("The king is old and weak, he wants me dead becuase I'm a threat, I know too much, I'm too dangerous")
	maxy("But you don't have to kill me, we could be allies, we could join together against the king, overthrow him!")
	you(player, "Um... welll")
	maxy("What makes him right anyways? Becuase he's incharge. \nReally " + player['name'] + ', you think that he got his throne fairly?\nHe did the same thing I would like to to do get it!')
	maxy("Now... will you join me and fight against him?")
	print("[1] Listen to Maximus | [2] Fight him now!")
	choice = input()
	if choice == '1':
		player['bad_points'] += 10
		overthrow(player)
	elif choice == '2':
		player['good_points'] += 10
		you(player, "I'm here to kill you Maximus, not to join you")
		maxy("Very well then, it appears that we will have to fight it out!")
		you(player, "As you wish... YAAAAAAH!")
	database.save(player)
def overthrow(player):
	maxy("You are a very wise one, now follow me, and together we will overthrow the king!")
	you(player, "Let's go...")
	time.sleep(2)
	king_battle_with_max(player)
	time.sleep(2)
	you(player, "Now I am king...")
	maxy("Wait just a minute, I am king, you are second in command")
	you(player, "I don't wanna be second in command")
	maxy("Wait a minute, we had a deal!")
	you(player, "Not any more...")
	maxy("What do you mean? Are you going to kill me!")
	you(player, "hmm...")
	print("[1] Kill Maximus and take the throne for yourself")
	print("[2] Let Maximus live")
	choice = input()
	if choice == '1':
		player['bad_points'] += 12
		max_battle()
	elif choice == '2':
		player['good_points'] += 6
		you(player, "I'll let you live... for now")
	database.save(player)
def max_battle(player, maximus):
	win = False
	from ai_talk import s_print
	while win == False:
		os.system('clear')
		print("Maximus: [ Life: " + str(maximus.health) + ' ] You: [ Life: ' + str(player['life']) + ' ]')
		if player['ammo'] not in ('infinite', 'Infinite'):
			if player['ammo'] >= 1:
				s_print("You " + random.choice(attack_style) + " attack Maximus with your " + player['main_weapon'])
				damage_given = random.randint(player['main_weapon_min'], player['main_weapon_max'])
				player['ammo'] -= 1
			else:
				s_print(Fore.RED + "You have no ammo left!")
				s_print("You are forced to resort to fighting with your fists")
				player['ammo'] = 'infinite'
				player['main_weapon'] = 'Fists'
				player['main_weapon_max'] = 3
				player['main_weapon_min'] = 4
		else:
			s_print("You " + random.choice(attack_style) + " attack Maximus with your " + player['main_weapon'])
			damage_given = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		i = random.randint(1,2)
		if i == 2:
			damage_given -= maximus.block + maximus.defense
		else:
			damage_given -= maximus.defense
		s_print(Fore.GREEN + 'Maximus takes ' + str(damage_given) + ' damage')
		maximus.health -= damage_given
		t = random.randint(1,5)
		if t == 5:
			s_print(Fore.RED + "Maximus uses " + maximus.special_attack)
			damage_taken = maximus.special_attack_damage - (random.randint(player['armor_min'], player['armor_max']) + player['shield_defense'])
			player['life'] -= damage_taken
			s_print(Fore.RED + "You take " + str(damage_taken) + ' damage')
		else:
			s_print(Fore.RED + 'Maximus ' + random.choice(maximus.t1) + ' ' + random.choice(maximus.t2) + ' in the ' + random.choice(maximus.t3))
			z = random.randint(1,2)
			if z == 1:
				damage_taken = maximus.attack - random.randint(player['armor_min'], player['armor_max'])
				blocked = player['shield_defense']
				percent = int(blocked / damage_taken)
				damage_taken -= blocked
				s_print(Fore.GREEN + "You blocked and deflected " + str(percent) + '% of the damage')
				s_print(Fore.RED + 'You still took ' + str(damage_taken) + ' damage')
				player['life'] -= damage_taken
			else:
				damage_taken = maximus.attack - random.randint(player['armor_min'], player['armor_max'])
				s_print("You took " + str(damage_taken) + ' damage')
				player['life'] -= damage_taken
		if maximus.health <= 0:
			s_print(Fore.GREEN + "You defeated Maximus the III")
			s_print(Fore.GREEN + "You now own '" + maximus.loot +"' A deadly weapon for battle")
			player['weapons'].append(maximus.loot)
			player['kills'].append('Maximus the III')
			player['gold'] += 100
			s_print("You got 100 Gold!")
			player['mission3'] = True
			database.save(player)
			input()
		elif player['life'] <= 0:
			s_print(Fore.RED + "You have been defeated...")
			input()		
def maximus(player):
	maximus = get_max()
	max_talk(player)
	max_battle(player, maximus)
def king_battle_with_max(player):
	maximus = get_max()
	class king():
		life = 1000
		damage_min = 10
		damage_max = 30
		defense_min = 1
		defense_max = 10
	max_can_fight = True
	targets = ['you', 'max']
	while True:
		print("Your Life: " + str(player['life']) + ' | Maximus: ' + str(maximus.health) + ' | King: ' + str(king.life))
		## You attack
		damage = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		blocked = random.randint(king.defense_min, king.defense_max)
		percent = int((blocked / damage) * 100)
		print("You attack with your " + player['main_weapon'])
		print("The king blocks " + str(percent) + '% of your attack')
		damage -= blocked
		print('The king takes ' + str(damage) + ' damage')
		king.life -= damage
		## Maximus attacks
		if max_can_fight:
			damage2 = maximus.attack
			print("Maximus " + random.choice(maximus.t1) + ' strikes the King in the ' + random.choice(maximus))
			blocked2 = random.randint(king.defense_min, king.defense_max)
			percent2 = int((blocked2 / damage2) * 100)
			damage2 -= blocked2
			print("The king blocks " + str(percent2) + "% of Maximus's attack and takes " + str(damage2) + "damage")
			king.life -= damage2
		## King attacks
		choice = random.randint(targets)
		if choice == 'you':
			print("The king attacks you!")
			k_dam = random.randint(king.damage_min, king.damage_max)
			b = random.randint(1,2)
			k_block = 0
			if b == 1:
				k_block = player['shield_defense']
				b_p = int((k_block / k_dam) * 100)
				print("You block " + str(b_p) + '% of the damage')
			s_block = random.randint(player['armor_min'], player['armor_max'])
			s_per = int((s_block / k_dam) * 100)
			print("Your armor blocks " + str(s_per) + '% of the damage')
			k_dam -= s_block
			k_dam -= k_block
			print("You take " + str(k_dam))
			player['life'] -= k_dam
		else:
			print("The king attacks maximus!")
			dam = random.randint(king.damage_min, king.damage_max)
			print('Maximus takes ' + str(dam) + ' damage')
			maximus.health -= dam
		## check of kill
		if maximus.health <= 0:
			print("Maximus can fight no longer...")
			input()
			max_can_fight = False
			targets.remove('max')
		elif player['life'] <= 0:
			print("You have been defeated...")
			input()
			break
		elif king.life <= 0:
			print("You have defeated the king....")
			player['mission11'] = True
			player['kills'].append("The King")
			player['bad_points'] += 500
			database.save(player)
			input()
			break
		else:
			input()

class the_quack():
	def __init__(self, life, damage_min, damage_max, defense_min, defense_max, t1, t2, t3):
		self.life = life
		self.damage_min = damage_min
		self.damage_max = damage_max
		self.defense_min = defense_min
		self.defense_max = defense_max
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
def grim_quacker(player):
	duck = the_quack(200, 1, 50, 1, 20, ['leaps', 'quacks', 'flaps', 'wiggles', 'waddles'], ['strikes', 'bites', 'hits', 'smacks'], ['chest', 'face', 'leg', 'arm', 'eye', 'nose', 'head', 'snozzle'])
	win = False
	while not win:
		util.clear()
		print('Your life: ' + str(player['life']) + ' | Grim Quacker Life: ' + str(duck.life))
		print("The Grim Quacker " + random.choice(duck.t1) + ' and ' + random.choice(duck.t2) + ' you in the ' + random.choice(duck.t3))
		damage_full = random.randint(duck.damage_min, duck.damage_max)
		absorbed = random.randint(player['armor_min'], player['armor_max'])
		t_percent = int((absorbed / damage_full) * 100)
		print("Your armor absorbs " + str(t_percent) + '% of the damage')
		blocked = 0
		if random.randint(1,2) == 1:
			blocked = player['shield_defense']
			percent = int((blocked / damage_full) * 100)
			print("Your shield deflects " + str(percent) + '% of the damage')
		damage_full -= (absorbed + blocked)
		print("You take " + str(damage_full) + ' damage')
		player['life'] -= damage_full
		print("You vicously attack The Grim Quacker with your " + player['main_weapon'])
		damage = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		duck_blocked = random.randint(duck.defense_min, duck.defense_max)
		pp = (duck_blocked / damage) * 100
		print('The Grim Qackers feathers absorb ' + str(int(pp)) + '% of the damage')
		print("You inflict " + str(damage) + ' damage')
		damage -= duck_blocked
		duck.life -= damage
		# Check for kill
		if duck.life <= 0:
			print("You defeated The Grim Quacker!")
			player['kills'].append('The Grim Quacker')
			player['monster_parts'].append('Grim Qacker Skull')
			player['weapons'].append('Lightening Blade')
			player['unlocked_locations'].append("Beggar City")
			player['gold'] += 100
			player['mission6'] = True
			database.save(player)
			print("You got a Grim Quacker Skull!")
			print("You now have a new weapon: Lightening Blade")
			print("You earned 100 Gold")
			print("You unlocked a new location: Beggar City")
			input()
			win = True
		elif player['life'] <= 0:
			print("You have been defeated...")
			input()
			win = True
		else:
			input()
def mega_rat(player):
	win = False
	from ai_talk import m
	m("Let's fight man to man, no weapons, just our claws... or in your case fists")
	print("[1] Agree | [2] Dissagree")
	i = input()
	if i == '1':
		print("You decide to fight fair")
		player['main_weapon'] = 'Fists'
		player['main_weapon_min'] = 1
		player['main_weapon_max'] = 2
		database.save(player)
	else:
		player['bad_points'] += 20
		print("You strike and kill Mega Rat with your " + player['main_weapon'])
		player['mission7'] = True
		database.save(player)
		win = True
	class rat():
		life = 25
		max_damage = 2
		min_damage = 1
	while not win:
		util.clear()
		print("Your life: " + str(player['life']) + ' | Rat Life: ' + str(rat.life))
		dd = random.randint(rat.min_damage, rat.max_damage)
		print('Mega rat attacks and inflicts ' + str(dd) + ' damage')
		player['life'] -= dd
		ddd = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		print("You attack and inflict " + str(ddd) + 'damage')
		rat.life -= ddd
		if rat.life <= 0:
			print("You defeated Mega Rat")
			print("You got two new weapons: Rat Spear and Rat Dagger")
			player['weapons'].append('Rat Spear')
			player['weapons'].append('Rat Dagger')
			player['mission7'] = True
			database.save(player)
			win = True
		else:
			print("You were defeated by Mega Rat...")
			win = True
		input()
		

def gate_keeper(player):
	from ai_talk import keeper
	if player['mission8'] == True:
		keeper("You are worthy to travel, where do you wish to go?")
		print("[1] Thorg World")
		print("[2] Healing Place")
		print("[3] Blacksmith's shop")
		i = input()
		if i == '1':
			player['location'] = 'Thorg World'
		elif i == '2':
			player['location'] = 'Healing Place'
		elif i == '3':
			player['location'] = "Blacksmiths shop"
		else:
			keeper("I'm afraid I do not know that location...")
	else:
		keeper("Who dares to travel to this hidden place?")
		keeper("I am the keeper, I guard this gate so that none may pass")
		keeper("Leave or be destroyed!")
		print("[1] Leave | [2] Challenge the keeper of the Gate to battle")
		t = input()
		if t == '1':
			keeper('You have made a wise decision')
		else:
			keeper("You dare challenge me to battle?")
			keeper("I can singly handedly wipe out armies! You dare to battle me!")
			print("Are you sure you want to battle him?")
			print("[1] Yes | [2] No")
			z = input()
			if z == '1':
				keeper("Arise my brothers, fellow guardians of the path, let us go into battle!")
				util.slow_print("Fellow Keepers: We have arisen brother, whom will we destroy?")
				multi_battle.keepers_of_the_gate(player)
			else:
				print("You escape...")
			input()
