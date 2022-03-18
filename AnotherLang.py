import os
import sys
import time
import os 
from Core.Languages.russian import *
from Core.Languages.italian import *
from Core.Languages.spanish import *
from Core.helper.Banners import *

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033;[1;37;40m")
blue = ("\033[1;34;40m")
yellow = ("\033[1;33;40m")
start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def numbering(num):
    return green + "[" + white + str(num) + green + "]"

def CurrentDir():
    path = os.getcwd()
    print(green + "[" + white + "+" + green + "]" + white " Your Templates Will Be Saved Here " + path)

def Languages():
    PlanetBanner()
    time.sleep(2) 
    print("\nThis Is My First Time Using Other Languages  \n")
    print( alert + " I Do Not Know If There Are Any Spelling Misstakes etc..." + alert)
    print("\n I Had To Use A Translator, I Do Not Speak These Languages   \n")

    time.sleep(2)

    print(start + " Pick A Language:\n")

    print(numbering(1) + white + " Italian")
    print(numbering(2) + white + " Russian")
    print(numbering(3) + white + " Spanish")
    print(numbering(99) + red + "Exit\n")
    LanguagePick = int(input(green + "root@phishmailer/Languages:~ " + white))

    if LanguagePick ==1:
        MainItalian()

    elif LanguagePick == 2:
        MainRussian()

    elif LanguagePick == 3:
        MainSpanish()

    elif LanguagePick == 99:
        print(alert + red + "Bye Bye")
        sys.exit()

    else:
        print(alert + red + " Invalid Option")
        sys.exit()
        