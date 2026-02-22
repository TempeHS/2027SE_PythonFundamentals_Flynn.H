import pyfiglet
import sys
import random

if len(sys.argv) not in [1, 3]:
    sys.exit("enter 0 arguments or 2")
figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "--font"):
        sys.exit("invalid usage")
    if sys.argv[2] not in (fonts):
        sys.exit("invalid usage")
    font = sys.argv[2]

else:
    sys.exit("invalid arguments")

text = input("enter text: ")

figlet.setFont(font=font)
print(figlet.renderText(text))
