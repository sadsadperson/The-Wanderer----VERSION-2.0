import random
import os
import util
import database
from ai_talk import s_print

class enemy_class():
	def __init__(self, num, life, damage_max, damage_min, defense, loot):
		self.num = num
		self.life = life
		self.damage_max = damage_max
		self.damage_min = damage_min
		self.defense = defense
		self.loot = loot

def duck_fight(player):
	## prepare swarm
	number = 0
	swarm = []
	for i in range(50):
		swarm.append(enemy_class(number, 1,1,1,0,['Duck Beak', 'Duck Foot', 'Feathers']))
		number += 1

	## battle
	battle = True

	while battle:
		print("Life: " + str(player['life']))
		print("Choose an enemy to attack: ")
		for enemy in swarm:
			print('[' + str(swarm.index(enemy)) + '] Duck | Life: ' + str(enemy.life))
		try:
			target = int(input(":: "))
		except:
			print("Gimmeh a number!")
		damage = random.randint(player['main_weapon_min'], player['main_weapon_max'])
		print("You inflicted " + str(damage) + ' damage on Duck')
		swarm[target].life -= damage
		if swarm[target].life <= 0:
			print('Enemy defeated!')
			loot = random.choice(swarm[target].loot)
			print("You got " + loot)
			swarm.remove(swarm[target])
		if not swarm:
			print("You defeated the swarm!")
			player['mission4'] = True
			input()
			battle = False
		print("Enemies turn to attack")
		input()
		for enemy in swarm:
			print("Enemy attacks!")
			d = random.randint(enemy.damage_min, enemy.damage_max)
			print("You take " + str(d) + ' damage')
			player['life'] -= d
		if player['life'] <= 0:
			print("You have been defeated...")
			battle = False
			input()
		input()
def keepers_of_the_gate(player):
	class keeper1():
		name = 'Keeper Kang Tangfoot'
		life = 50
		max_damage = 15
		min_damage = 8
		min_defense = 3
		max_defense = 6
		block = 8
		loot = 'Chainmail'
	class keeper2():
		name = 'Keeper Chow Gheten'
		life = 28
		max_damage = 18
		min_damage = 5
		min_defense = 1
		max_defense = 3
		block = 5
		loot = 'Dragon Scale Shield'
	class keeper3():
		name = 'Keeper Thug Bonecrusher'
		life = 30
		max_damage = 20
		min_damage = 10
		min_defense = 1
		max_defense = 2
		block = 3
		loot = 'Ice Armor'
	enemies = [keeper1, keeper2, keeper3]
	fighting = True
	while fighting:
		print("Life: " + str(player['life']))
		for enemy in enemies:
			print("[" + str(enemies.index(enemy)) + '] ' + enemy.name + ' | Life: ' + str(enemy.life))
		attack = int(input("Target for attack: "))
		try:
			raw_damage = random.randint(player['main_weapon_min'], player['main_weapon_max'])
			blocked = 0
			absorbed = random.randint(enemies[attack].min_defenes, enemies[attack].max_defense)
			w = random.randint(1,2)
			if w == '2':
				blocked = enemies[attack].block
			total_blocked = absorbed + blocked
			percent = int((total_blocked / raw_damage) * 100)
			damage = raw_damage - total_blocked
			s_print(enemies[attack].name + ' blocks ' + str(percent) + '% of the damage but still takes ' + str(damage) + ' damage')
			enemies[attack].life -= damage
			chop = enemies[attack]
			if enemies[attack].life <= 0:
				s_print("You defeated " + chop.name)
				enemies.remove(chop)
				s_print("You looted the body and got " + chop.loot)
				if chop.loot == 'Chainmail':
					player['armors'].append('Chainmail')
				elif chop.loot == 'Dragon Scale Shield':
					player['shields'].append('Dragon Scale Shield')
				elif chop.loot == 'Ice Armor':
					player['armors'].append('Ice Armor')
		except:
			print("Please choose a target on the list!")
		input()
		attacker = random.choice(enemies)
		s_print(attacker.name + ' attacks!')
		damage_taken = random.randint(attack.min_damage, attacker.max_damage)
		i = random.randint(1,2)
		block = 0
		if i == 1:
			block = player['shield_defense']
			s_print("You block " + str(block) + ' damage')
		armor = random.randint(player['armor_min'], player['armor_max'])
		dd = int((armor / damage_taken) * 100)
		damage_taken -= (block + armor)
		s_print("Your armor absorbs " + str(dd) + '% of the damage')
		s_print("You take " + str(damage_taken) + ' damage')
		player['life'] -= damage_taken
		## check for win
		if not enemies:
			s_print("You defeated the keepers at the gate!")
			s_print("You can now travel here any time, as you have one their respect and obediance")
			s_print("Now you can also call on the keepers for skirmishes")
			s_print("The keepers have also given you the power to return to your home base at anytime")
			player['unlocked_locations'].append("Home")
			util.new_helper(player, keeper1.name, keeper1.life, keeper1.min_damage, keeper1.max_damage, keeper1.min_defense, keeper1.max_defense, keeper1.block, 1, [])
			util.new_helper(player, keeper2.name, keeper2.life, keeper2.min_damage, keeper2.max_damage, keeper2.min_defense, keeper2.max_defense, keeper2.block, 1, [])
			util.new_helper(player, keeper3.name, keeper3.life, keeper3.min_damage, keeper3.max_damage, keeper3.min_defense, keeper3.max_defense, keeper3.block, 1, [])
			fighting = False
		elif player['life'] <= 0:
			print("You have been defeated by the keepers")
			fighting = False
		database.save(player)

