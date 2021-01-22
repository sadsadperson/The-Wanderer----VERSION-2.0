import util
import ai_talk
import database

value = {
	'Goblin Brain' : 10,
	'Goblin Guts' : 3,
	'Goblin Claws' : 4,
	'Goblin Eye' : 15,
	'Orc Guts' : 4,
	'Orc Eyes' : 8,
	'Orc Brain' : 4,
	'Orc Claws' : 9,
	'Orc hair' : 8,
	'Troll Head' : 15,
	'Troll guts' : 12,
	'Troll brain' : 23,
	'Troll teeth' : 25,
	'Troll eye' : 7,
	'Kraveb Head' : 18,
	'Kraveb Guts' : 8,
	'Kraveb Eye' : 18,
	'Kraveb claws' : 13,
	'Kraveb teeth' : 25,
	'Thorg head' : 50,
	'Thorg Claws' : 48,
	'Thorg guts' : 68,
	'Grim Qacker Skull' : 1000
}


def sell(player):
	util.clear()
	ai_talk.gnole("Hello there young man, I see you have a large amount of loot with you? Would you be interested in selling any of that? I pay well for any monster parts... hehehe")
	print("[1] Sell | [2] Ignore him")
	i = input()
	val = 0
	if i == '1':
		loot = player['monster_parts']
		for x in loot:
			val += value[x]
		print("You earned " + str(val) + ' Gold')
		player['gold'] += val
		player['monster_parts'].clear()
		input()
	else:
		ai_talk.gnole("Oh, well see you when you change you mind!")
		input()
	database.save(player)