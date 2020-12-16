import os
import time

def slow_print(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)
    print()


def rob_infant():
	p = print
	c = os.system('clear')
	p ("")
	p ("")
	p ("")
	p (" __                                  ")
	p ("( -)                    __           ")
	p ("/||\                   (* )          ")
	p (" /\                   0-||           ")
	p ("#####################################")