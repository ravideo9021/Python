from pyfiglet import Figlet
import random


argument = input("Input: ")
figlet = Figlet()
font = Figlet(font = random.choice(figlet.getFonts()))
print(font.renderText(argument))