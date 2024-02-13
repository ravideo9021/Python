from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font  = sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit()
else:
    print("Invald usage")
    sys.exit()

argument = input("Input: ")

font = Figlet(font = font)
print(f" output: {font.renderText(argument)}")
