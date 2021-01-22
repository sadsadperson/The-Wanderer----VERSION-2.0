import sys
import random
import database
from colorama import Fore, Back, Style
import time
import util
import boss_fight
talk = {
	'talk' : [],
	'good' : 0,
	'mean' : 0,
	'murderous' : 0,
	'common_talk' : [],
}
def s_print(x):
	for char in x:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(.02)
	print()
def keeper(x):
	s_print(Fore.YELLOW + "Keeper of the Gate: " + x + Style.RESET_ALL)
def game_master(x):
	s_print(Fore.YELLOW + "Game Master: " + x + Style.RESET_ALL)
def old_man(x):
	s_print('👨‍🦳: ' + x)
def gnole(x):
	s_print('🧐: ' + x)
def ice_man(x):
	s_print('🥶: ' + x)
def horrified_villager(x):
	s_print('😱: ' + x)
def thorg(x):
	s_print('👺: ' + x)
def speak(x):
	s_print('😀: ' + x)
def m(x):
	s_print("🐭: " + x)
def z(x):
	s_print('👁: ' + x)
def k(x):
	s_print(Fore.GREEN + '🤴: ' + x)
def maxy(x):
	s_print(Fore.YELLOW + 'Maximus the III: ' + x)
def you(player, x):
	s_print(Fore.GREEN + player['name'] + ': ' + x)
def choice(choice1, choice2):
	print("[1] " + choice1 + ' | [2] ' + choice2)
	return input()
def king(player):
	util.clear()
	if player['bad_points'] > 5:
		k("Why have you come here? I know your evil deeds!")
		t = choice('Kill him', "Tell him you are sorry for the bad things you did")
		if t == '1':
			s_print("You draw your " + player['main_weapon'])
			k("So it is treason then?")
			battle.king_fight()
		else:
			k("If you truly wish to be pardoned, you can, but you will have to pay for your crimes!")
			k("Guards, lock him in the dungeon until he has paid for his crimes!")
			util.sentence(player['bad_points'] * 3)
	
	elif player['mission1'] == False and util.count_list(player['monster_parts'], 'Kraveb Head') >= 3:
		player['mission1'] = True
		player['weapons'].append("Ice Pick")
		k("You have completed your quest! Very good, here is an Ice Pick!")
		k("It is a deadly weapon at close range against enemies, weild it with skill and you will be very strong in battle")
		player['gold'] += 25
		k("Also, here is 25 gold coins for finishing the task so fast")
		k("And now I have another mission for you!")
		time.sleep(1)
		util.clear()
		k("A fiend roams my lands, his name is Maximus the III")
		k("He claims he is the heir to this throne, although he is not, and attemps to stir the commonfolk up")
		k("I would allow you to hunt him but you have not proven yourself yet")
		k("Find and kill a Thorg, and you will be strong enough to battle him!")
	elif player['mission1'] != True:
		k("You, warrior! You seem to be strong, I have a quest for you!")
		k("Monsters plague my lands, and if you bring me the head of three kraveb, I will grant you a special weapon!")
	elif player['mission1'] == True and player['mission2'] != True and 'Thorg' in player['kills']:
		k("You are a strong warrior, for you have defeated a thorg!")
		k("Now I know you are strong enough to battle Maximus himself!")
		k("For now he is banished to the realm of monsters, here is a key to that land, but beware, it is a very dangerous place to be!")
		player['unlocked_locations'].append("Monster Lands")
		s_print("You have unlocked a new location: Monster Lands")
		player['mission2'] = True
		database.save(player)
	elif player['mission3'] == False:
		k("Go to the monsterlands, and defeat Maximus the III")
	elif player['mission3'] == True:
		k("You have defeated Maximus the III? You are more powerful then I first thought")
		k("You are very powerful, powerful enough to travel to dangerous lands")
		s_print("You unlocked a new location: Far Place")
		player['unlocked_locations'].append('Far Place')
		database.save(player)
	input()
#### CREATING AN AI VILLAGER #####
class create_villager():
	def __init__(self, quest, cash, life, food, fear_level, happy, sad, angry, dangerous, intro):
		self.quest = quest
		self.cash = cash
		self.life = life
		self.food = food
		self.fear_level = fear_level
		self.happy = happy
		self.sad = sad
		self.angry = angry
		self.dangerous = dangerous
		self.intro = intro
small_talk = {
	'talk1' : [["Hi there, what's your name?", "Your new, what's your name?", "Dude, what's the name? ", "Yo, who are you!"], ['Tell them your name', "Don't tell them your name", "Tell them a fake name", "Ignore them"]],
	'talk2' : [['Weathers nice huh?', "Do you like the weather?", "Not too bad weather, you agree?"],['Ignore them', "Agree with them"]],
	'talk3' : [['Ever fought a monster? ', "Are you a warrior", "You look like you fight alot, do you fight alot?"], ['Ignore them', "Say yes", "Say no"]],
	'talks' : ['talk1', 'talk2', 'talk3']
}
ask1 = {
	'ask' : ['Can I have some money?', "Times have been hard, could I have some cash", "I really hate to ask, but could I have a few coins?", "Please sir, could you spare a few gold coins to a poor travelor?"],
	'good_answer' : ["Give them the money", "Loan them a few coins", "Chuck them a coin", 'Ignore them'],
	'mean_answer' : ['Tell them no!', 'Kick some dust in their face and walk away', "Punch them in the head", "Shove them away"],
	'murderous_answer' : ['Kill them', "Rob them", "Murder them", "Stab them with a knife and loot the body"],
	'n_answer' : ['Ignore them', "Give them some money", "Tell them no", 'Kill them']
}
happy_intro = ["It's a great day isn't it! I'm ", "Hello and welcome, I'm ", "Nice to see you here, by the way I'm "]
sad_intro = ['Waaaa... me sad... me name is', "A'm a whiney butt and crying, my name is "]
angry_intro = ['What do you want! Punk!', "Get outta my town fart face!", "I know who you are butt! Get out of here!"]
deadly_intro = ['Imma gunna kill you', "You better move on pard, cuase I plan on taking OFF YOUR HEAD!", "Prepare to meet your maker!", "You killed my brother! Now I'm gunna kill you"]
advice = ['Having a strong shield is often better then a more powerful weapon', "Don't attempt to face a Thorg without a strong suit of armor", "If you are a specialty class, specialty weapons like sharp stick, or brute force cudgels are more dangerous in your hands", "The Thorg war bow is the most powerful weapon", "Spears are powerful and light, make use of them", "Watchout for Yeckity Toe, they are small, but deadly", "If you talk to street rats sometimes they give you stuff", "If you are attacked by a duck swarm, retreat as soon as possible!", "Watchout for thugs!", "You can learn much information from the library"]
random_talk = ["Did you know that the sky is blue!", "Katie said that bo was her best freind", "Did you know that you resemble my brother", "*the villager does not want to talk with you*", "I HATE YOU", "Dude, just get some cake and eat it man", "Like legit, I used to be an actor", "I used to be a warrior like you, that was a long time ago...", "My son my son! Somebody killed my son!", "I had a freind.. I think a Thorg ate him...", "*Hippie eats a leaf*", 'Chattering chattering sometimes I talk to much!...', "Sigh..."]
def create_person(player):
	villager = create_villager('None', random.randint(1,100), random.randint(1,25), random.randint(1,10), random.randint(1, 3), random.randint(1, 3), random.randint(1, 3), random.randint(1, 3), random.randint(1, 10), '')
	villager.fear_level = villager.fear_level * talk['murderous']
	villager.happy = villager.happy * talk['generous']
	villager.sad = villager.sad * talk['mean']
	villager.angry = villager.angry * talk['theif']
	if villager.happy > villager.sad and villager.happy > villager.angry:
		villager.intro = random.choice(happy_intro)
	elif villager.angry > villager.sad and villager.angry > villager.happy:
		villager.intro = random.choice(angry_intro)
	elif villager.sad > villager.angry and villager.sad > villager.happy:
		villager.intro = random.choice(sad_intro)
	else:
		villager.intro = random.choice(deadly_intro)
	speak(villager.intro)
	intro_talk = random.choice(small_talk['talks'])
	speak(random.choice(small_talk[intro_talk][0]))
	count = 0
	for choice in small_talk[intro_talk][1]:
		print(Fore.GREEN + '[' + str(count) + '] ' + choice + Style.RESET_ALL)
	choice = input()
	speaking = True
	while speaking:
		if villager.cash < 3:
			speak(random.choice(ask1['ask']))
			prompt = ''
			if talk['good'] > talk['bad'] and talk['good'] > talk['murderous']:
				print(Fore.GREEN + "Do you: " + random.choice(ask1['good_answer']) + Style.RESET_ALL)
				prompt = 'good'
			elif talk['bad'] > talk['good'] and talk['bad'] > talk['murderous']:
				print(Fore.GREEN + "Do you: " + random.choice(ask1['bad_answer']) + Style.RESET_ALL)
				prompt = 'bad'
			elif talk['murderous'] > talk['good'] and talk['murderous'] > talk['bad']:
				print(Fore.GREEN + "Do you: " + random.choice(ask1['murderous_answer']))
				prompt = 'murder'
			else:
				prompt = random.choice(ask1['n_answer'])
				print(Fore.GREEN + "Do you: " + prompt + Style.RESET_ALL)
			answer = input("[1] Yes | [2] No\n")
			if answer == '1':
				if prompt == 'good':
					talk['good'] += 1
					print(Fore.GREEN + "You did a good thing")
				elif prompt == 'bad':
					print(Fore.RED + 'You did a bad thing')
					talk['bad'] += 1
				elif prompt == 'murder':
					print(Fore.RED + Style.BRIGHT + 'You killed them!' + Style.RESET_ALL)
					talk['murderous'] += 1
				elif prompt == 'Ignore them':
					print("You ignored them")
					talk['good'] += 1
				elif prompt == 'Give them some money':
					print("You gave them some money!")
					talk['good'] += 2
				elif prompt == 'Tell them no':
					print("You told them no")
					talk['mean'] += 1
				elif prompt == 'Kill them':
					print("You killed them!")
					talk['murderous'] += 1
			else:
				print("Do you want to: ")
				print("[1] Ignore them")
				print("[2] Give them some money")
				print("[3] Tell them no")
				print("[4] Kill them")
				c = input()
				if c == '4':
					print("You killed the villager!")
					talk['murderous'] += 1
				elif c == '1':
					print("You ignored them")
				elif c == '3':
					print("You told them no!")
					talk['bad'] += 1
		else:
			i = random.randint(1,2)
			if i == 1:
				speak(random.choice(advice))
			else:
				speak(random.choice(random_talk))
			

def farlands(player):
	if player['bad_points'] > player['good_points']:
		z("You are not welcome here!")
		z("You deeds are evil, get out of my sight or I will kill you!")
		print("[1] Leave | [2] Stay")
		i = input()
		if i == '1':
			z("And stay away!")
		else:
			z("You dare challenge me!")
			print(Fore.RED + "Z inflicts 1000 Damage on you and blasts you from his site")
			player['life'] -= 1000
			player['location'] = 'Monster Lands'
			database.save(player)
	elif player['mission5'] != True:
		z("You are not welcome here!")
		z("Get out of my sight or I will kill you!")
		print("[1] Leave | [2] Stay")
		i = input()
		if i == '1':
			z("And don't come back!")
		else:
			z("I told you to leave!")
			you(player, 'Wait, I come in peace')
			z("Peace has not been in this place since the swarms attacked")
			you(player, 'Swarms?')
			z("Duck swarms... usually they aren't dangerous, but in a large swarm, these ducks will devour you in seconds")
			you(player, 'If I drive them off would I be welcome here?')
			z("Ha! You, defeate them? Good luck!")
			z("If killing the ducks was all that was needed to be done, I would of done it myself years agod\nNo, you must defeat the Grim Quacker to destroy the swarms")
			you(player, "I thought Grim Quackers were just a thing of legend?")
			z("They are real, and here, defeat it, and I will allow you come here in peace")
			you(player, "I will kill this Grim Quacker...")
	elif player['mission5'] == True and player['mission6'] != True:
		z('So you have survived it swarms? That was the easy part, go and defeat the Grim Quacker')
	elif player['mission6'] == True:
		z("You are welcome in my lands...")
	input()
	util.clear()
def mega_rat(player):
	if player['mission7'] != True:
		m("I am mega rat! I own this town and extract payments from it's citizens")
		m("Gimmeh all your money or I'll kill you in the street!")
		print("[1] Give Mega Rat all you money | [2] Kill Mega Rat")
		i = input()
		if i == '1':
			you(player, "Fine, here's all my money")
			player['gold'] = 0
			database.save(player)
			m("Ah, now that you've given me all my money? Time to die!")
			boss_fight.mega_rat(player)
		else:
			m("So you want to kill me?")
			boss_fight.mega_rat(player)
	else:
		m("Mega rat is dead, I am the new leader, Ultra Rat, you may come here in peace")
def speak_dude(player):
	util.clear()
	good_talk = ['Hi there, how are you?', "Hello, nice day isn't it?", "Hi there!"]
	bad_talk = ['Ohno, are you here to kill me?', "Please, go away", 'Help its the bad man!']
	good_talk2 = ["I'm off to go fishing see you later", "Goodbye now", "See you around"]
	bad_talk2 = ["Please don't kill me!", "Go away!", "AAHHHH!"]
	if player['bad_points'] > player['good_points']:
		old_man(random.choice(bad_talk))
		input()
		old_man(random.choice(bad_talk2))
		print("[1] Kill the villager")
		print("[2] Leave the villager")
		print("[3] Rob the villager")
		choice = input()
		if choice == '1':
			s_print("You killed a villager!")
			player['bad_points'] += 3
		elif choice == '2':
			s_print("You walked away from the villager")
		elif choice == '3':
			cash = random.randint(1,20)
			s_print("You robbed the villager and got " + str(cash) + ' gold')
			player['bad_points'] += 1
			player['gold'] += cash
		else:
			s_print("You walked away...")
	else:
		old_man(random.choice(good_talk))
		input()
		old_man(random.choice(good_talk2))
		print("[1] Give the villager some money")
		print("[2] Leave the villager")
		print("[3] Rob the villager")
		i = input()
		if i == '1':
			cash = random.randint(1,10)
			s_print("You gave the villager " + str(cash) + 
			' gold')
			player['gold'] -= cash
			player['mission13'] = True
		elif i == '3':
			cash = random.randint(1,20)
			s_print("You robbed the villager and got " + str(cash) + ' gold')
			player['gold'] += cash
			player['mission13'] = True
		else:
			s_print("You walked away...")
	input()
	util.clear()
def ultra_thorg(player):
	thorg("What do you want tiny human?")
	you("Dude, chill, I just came here to kill you and stop your evil reign by stealing your throne and sealing your passage to the monsterworld!")
	thorg("ROOOOAARRRR!!! ")
	s_print("Ultra the thorg attacks you...")
	boss_fight.ultra_the_thorg_fight(player)
