import sys
import random
import database
from colorama import Fore, Back, Style
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
			

