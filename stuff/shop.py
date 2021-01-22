import util
from colorama import Fore, Style
import database
def shop(player):
	while True:
		
		util.clear()
		print(Fore.GREEN + "GOLD: " + str(player['gold']) + ' | LIFE: ' + str(player['life']))
		shop_list = [
			['[1]', 'Sword', '10 Gold'],
			['[2]', 'Shield', '10 Gold'],
			['[3]', 'Bow', '10 Gold'],
			['[4]', 'Heal', 'Free [unless you want extra health]'],
			['[5]', 'Spear', '10 Gold'],
			['[6]', 'Arrows', '1 Gold Each'],
			['[7]', 'Armor', '10 Gold'],
			['[8]', 'Leave Store', ' '],
		]
		util.format_print(shop_list)
		buy = input()
		if buy == '1':
			if player['gold'] >= 10:
				print("You purchased a sword!")
				player['weapons'].append("Sword")
				player['gold'] -= 10
			else:
				print("You need more money")
		elif buy == '2':
			if player['gold'] >= 10:
				print("You purchased a shield!")
				player['shields'].append("Shield")
				player['gold'] -= 10
			else:
				print("You need more money")
		elif buy == '3':
			if player['gold'] >= 10:
				print("You purchased a bow!")
				player['weapons'].append("Bow")
				player['gold'] -= 10
			else:
				print("You need more money")
		elif buy == '5':
			if player['gold'] >= 10:
				print("You purchased a Spear!")
				player['weapons'].append("Spear")
				player['gold'] -= 10
			else:
				print("You need more money")
		elif buy == '7':
			if player['gold'] >= 10:
				print("You purchased a Armor!")
				player['armors'].append("Armor")
				player['gold'] -= 10
			else:
				print("You need more money")
		elif buy == '4':
			if player['life'] >= 25:
				if player['gold'] >= 5:
					print("You have healed")
					player['gold'] -= 5
					player['life'] += 5
					player['skills']['heals'] += 1
				else:
					print("You need more money")
			else:
				player['life'] = 25
				player['skills']['heals'] += 1
		elif buy == '6':
			amount = int(input("How many arrows would you like to buy?\n"))
			if player['gold'] >= amount:
				print("You purchased " + str(amount) + ' Arrows!')
				player['gold'] -= amount
			else:
				print("You need more money to buy that many arrows!")
		elif buy == '8':
			break
		database.save(player)
		input()