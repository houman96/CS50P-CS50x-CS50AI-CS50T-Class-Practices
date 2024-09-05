import sys
import pyfiglet


acceptablefonts = ['alphabet', 'slant', 'rectangles', 'regular']

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet = pyfiglet.Figlet()

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in acceptablefonts:
            text = input("Input: ")
            figlet = pyfiglet.Figlet(sys.argv[2])
else:
    sys.exit("Invalid usage")

print(figlet.renderText(text))


