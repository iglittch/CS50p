import sys
import pyfiglet

if len(sys.argv) == 3:
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "-font":
            text = input("Input: ")
            text = pyfiglet.figlet_format(text, font=sys.argv[2])
            print(text)
        else:
            sys.exit("Invalid usage")
    except pyfiglet.FontNotFound:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text = input("Input: ")
    text = pyfiglet.figlet_format(text)
    print(text)
else:
    sys.exit("Invalid usage")

"""
Expect zero or two command line arguments
0 - random font
2 - specific font 
sys.argv[1] > -f or --font
sys.argv[2] > name of font

Prompt user for str
Output in desired font
"""