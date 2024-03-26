from pyfiglet import Figlet
import sys
import random


if len(sys.argv) >1 and sys.argv[1] not in ["-f", "-font"]:
    sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    text = random.choice(Figlet.getFonts())
    fig = input("Input: ")

else:
    fig: str = input("Input: ")
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(fig))