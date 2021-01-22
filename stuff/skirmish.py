import database
from util import slow_print
import util
from ai_talk import game_master as g
import random
def skirmish(player):
	util.clear()
	if not player['team']['helpers']:
		g("Hi there, you look like you are new to these skirmishes, let me get you up to speed")
		g("First off, I'm the Game Master, and I'm in charge of the teams here")
		g("Teams get to battle together to win gold and such")
		g("You don't seem to have a team member, so you can't battle right now, come back when you do!")
		input()
	else:
		stat(player)
def stat(player):
	while True:
		team = player['team']
		print("Team Name: " + team['name'] + ' | Level: ' + str(team['level']) + ' | Victories: ' + str(team['wins']))
		print("[1] View Team Members")
		print("[2] Battle")
		print("[3] Back")
		i = input()
		if i == '1':
			for helper in team['helpers']:
				print("[" + str(team['helpers'].index(helper)) + '] ' + helper['name'] + ' | Level: ' + str(helper['level']))
			print("[l] Leave")
			choice = input()
			if choice != 'l':
				fighter = team['helpers'][int(choice)]
				print("Name: " + fighter['name'])
				print("Min Damage: " + str(fighter['min_damage']) + " | Max Damage: " + str(fighter['max_damage']))
				print("Min Defense: " + str(fighter['min_defense']) + ' | Max Defense: ' + str(fighter['max_defense']))
			else:
				pass
		elif i == '2':
			battle(team, player)
		elif i == '3':
			break
	input()
def get_level(x):
	score = x['max_damage'] + x['min_damage'] + x['min_defense'] + x['max_defense'] + x['block'] + x['life']
	level = 0
	if score >= 60:
		level = 4
	elif score >= 45:
		level = 3
	elif score >= 30:
		level = 2
	elif score >= 15:
		level = 1
	else:
		level = 0
	return level
def get_enemy():
	enemy_names = ['dude', 'wassup', 'girkle', 'Frig', 'Fart', "toot", "naoob", "wathge", "wher", "hgea", "ahge", "awehgea", "EWhage", "eahgea", "eiegh", 'AChe', "ehere", 'HEge', "Er'e ad", "adfae", 'Aehage', "kere", "hbeaf", "gherfe"]
	number = random.randint(1,8)
	enemies = []
	for i in range(number):
		enemy = {
			'name' : random.choice(enemy_names),
			'min_damage' : random.randint(1,5),
			'max_damage' : random.randint(6,20),
			'min_defense' : random.randint(1,3),
			'max_defense' : random.randint(4,8),
			'block' : random.randint(1,20),
			'life' : random.randint(5, 25),
			'level' : 0,
		}
		enemy['level'] = get_level(enemy)
		enemies.append(enemy)
	return enemies
def battle(team, player):
	enemies = get_enemy()
	while True:
		
		possible_fighters = team['helpers']
		for fighter in possible_fighters:
			print(fighter['name'] + ' | Life: ' + str(fighter['life']) + ' | Level: ' + str(get_level(fighter)))
		print('   ENEMIES   ')
		count = 0
		for enemy in enemies:
			print('[' + str(count) + '] ' + enemy['name'] + ' | Life: ' + str(enemy['life']) + ' | Level: ' + str(enemy['level']))
			count += 1
		attacker = random.choice(team['helpers'])
		print("Who should " + attacker['name'] + " attack? ")
		i = int(input())
		target = enemies[i]
		print(attacker['name'] + ' attacks ' + target['name'])
		damage = random.randint(attacker['min_damage'], attacker['max_damage'])
		deflected = random.randint(target['min_defense'], target['max_defense'])
		percent = int((deflected / damage) * 100)
		print(target['name'] + "'s armor absorbs " + str(percent) + '% of the damage')
		damage -= deflected
		t = random.randint(1,2)
		if t == 1:
			print(target['name'] + ' blocks ' + str(target['block']) + ' damage!')
			damage -= target['block']
		print(target['name'] + ' takes ' + str(damage) + ' damage')
		enemies[i]['life'] -= damage
		if enemies[i]['life'] <= 0:
			print(attacker['name'] + ' defeated ' + enemies[i]['name'])
			enemies.remove(target)
			attacker_num = player['team']['helpers'].index(attacker)
			player['team']['helpers'][attacker_num]['defeated'].append(target['name'])
			database.save(player)
		if not enemies:
			print("You win!")
			player['team']['wins'] += 1
			v = random.randint(20,100)
			print('You won ' + str(v) + ' gold!')
			player['gold'] += v
			database.save(player)
			break
		enemy_attacker = random.choice(enemies)
		enemy_target = random.choice(possible_fighters)
		print(enemy_attacker['name'] + ' attacks ' + enemy_target['name'])
		damage_taken = random.randint(enemy_attacker['min_damage'], enemy_attacker['max_damage'])
		deflected = random.randint(enemy_target['min_defense'], enemy_target['max_defense'])
		percent = int((deflected / damage_taken) * 100)
		print(enemy_target['name'] + ' deflects ' + str(percent) + '% of the damage!')
		damage_taken -= deflected
		t = random.randint(1,2)
		if t == 1:
			print(enemy_target['name'] + ' blocks!')
			damage_taken -= enemy_target['block']
		print(enemy_target['name'] + ' takes ' + str(damage_taken) + ' damage')
		enemy_target['life'] -= damage_taken
		if enemy_target['life'] <= 0:
			print(enemy_target['name'] + ' has been defeated...')
			possible_fighters.remove(enemy_target)
		if not possible_fighters:
			print("You have been defeated...")
			player['team']['loses'] += 1
			database.save(player)
			break
		input()
	



	



