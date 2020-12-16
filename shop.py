import os
import time
import util
def shop(player):
    while True:
        util.clear()
        print(Style.RESET_ALL + BOLD + GREEN + UNDERLINE +"| LIFE: " + str(player['gold']) + " | GOLD: " + str(player['Life']))
        print(Style.RESET_ALL + NORMAL + CYAN + '')
        print("__________MARKET__________")
        print("------WEAPONS SHOP--------")
        print("[1] Sword          10 Gold")
        print("[2] Bow            10 Gold")
        print("[3] Shield         10 Gold")
        print("[4] Armor          10 Gold")
        print("[5] Heal            5 Gold")
        i = input()
        if i == 1 and player['gold'] >= 10:
            print("Purchased Sword")
            input()
			player
        elif i == 2 and gold >= 10:
            print ("Purchased bow!")
            input()
        elif i == 3 and gold >= 10:
            print ("Purchased Sheild!")
            input()
	
