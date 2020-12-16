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
from colorama import Style
import util

def get_file(filename):
    with open('library/'+filename+'.txt', 'r') as file:
        return file.read()
def print_file(filename):
    file = get_file(filename)
    main = file.split('\n')
    title = main[0]
    sub_title = main[1]
    data = main[2:]
    print(Style.RESET_ALL + BLUE + BOLD + UNDERLINE + title.center(len(sub_title)) + Style.RESET_ALL) #centers main tile on sub title
    print(BLUE + ITALIC + UNDERLINE + sub_title + Style.RESET_ALL + '\n\n\n')
    for line in data:
        print(BLUE + line)
def library():
	util.clear()
	print(Style.RESET_ALL)
	print(PURPLE + BOLD + UNDERLINE + " ---- WELCOME TO THE LIBRARY ----- " + Style.RESET_ALL)
	print("Would you like to read? [1] Yes | [2] No")
	i = input()
	if i == '1':
		file = get_file('all')
		print(file)
		print("Choose something to read?")
		choice = input()
		try:
			print_file(choice)
			input()
		except:
			print("Error! Not a file")
	else:
		pass

