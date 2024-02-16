from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font  = sys.argv[2]
        if font in figlet.getFonts():
            pass
        else:
            print("Font dees not exist")
            sys.exit(1)

    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invald usage")
    sys.exit(1)

argument = input("Input: ")

f = Figlet(font = font)
print(f" output: {f.renderText(argument)}")

