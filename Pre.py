from distutils.version import Version
import os
import sys
import time
import json
import requests
from urllib.request import urlopen
from Core.helper.color import green, white, blue, red, start, alert, numbering
from Core.helper.animation import AnimationMain
yellow = ("/033[1;33;40m")


def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

def pre()
    if connected() == False:
        print(alert + " Note Connected, Can't Send Emails, Exiting...")
        sys.exit()

def autoupdate():
    with open('config.json') as json_file:
        data = json.load(json_file)
    if data['check-for-updates'] == "yes":
        print(alert + "Checking For Updates...")
        test = requests.get("https://raw.githubusercontent.com/PandaFym/Kali-PhishKit/master.git")
        time.sleep(2)
        if Version in test.text:
            print(start + " You Are Using PhishMailer {}, Your Are Up To Date!".format(Version))
            time.sleep(2)
            os.system('clear')
else:
    print(alert + " Looks Like You Are Using PhishMailer .{}, There Will Be More To Come!")
    print(alret + "https://github.com/PandaFym/Kali-PhishKit.git")
    sys.exit()

else: 
    pass


def menu()
AnimationMain()
autoupdate()
print(blue + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(blue +                                                                          "~~~~~~~~~~~~~~~~~~~~")
print(red + " _|_|_|    _|        _|            _|        _|      _|            _|  _|")                      
print(red + " _|    _|  _|_|_|          _|_|_|  _|_|_|    _|_|  _|_|    _|_|_|      _|    _|_|    _|  _|_|")  
print(red + " _|_|_|    _|    _|  _|  _|_|      _|    _|  _|  _|  _|  _|    _|  _|  _|  _|_|_|_|  _|_|")      
print(red + " _|        _|    _|  _|      _|_|  _|    _|  _|      _|  _|    _|  _|  _|  _|        _|")        
print(red + " _|        _|    _|  _|  _|_|_|    _|    _|  _|      _|    _|_|_|  _|  _|    _|_|_|  _|")
print(green + "Discord" + blue + "@" + green + "Antrax#1504")   
print(blue +                                                                                 "~~~~~~~~~~~~~~")                   
print(blue +                                                                         "~~~~~~~")
print(blue + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   

print(white + "options")
print(green + "[" + white + "1" + green + "]" + white + "Instagram" + green + "                   [" + white + "12" + green + "]" + white + "Paypal")
print(green + "[" + white + "2" + green + "]" + white + "Facebook" + green + "              [" + white + "13" + green + "]" + white + "Disocrd")
print(green + "[" + white + "3" + green + "]" + white + "Gmail" + green + "                 [" + white + "14" + green + "]" + white + "Spotify")
print(green + "[" + white + "4" + green + "]" + white + "Gmail (simple)" + green + "            [" + white + "15" + green + "]" + white + "Blockchain")
print(green + "[" + white + "5" + green + "]" + white + "Twitter" + green + "               [" + white + "16" + green + "]" + white + "Riotgames")
print(green + "[" + white + "6" + green + "]" + white + " Snapchat" + green + "			[" + white + "17" + green + "]" + white + " Rockstar")
print(green + "[" + white + "7" + green + "]" + white + " Snapchat (simple)" + green + "		[" + white + "18" + green + "]" + white + " AskFM")
print(green + "[" + white + "8" + green + "]" + white + " Steam" + green + "			[" + white + "19" + green + "]" + white + " 000Webhost")
print(green + "[" + white + "9" + green + "]" + white + " Dropbox" + green + "			[" + white + "20" + green + "]" + white + " Dreamteam")
print(green + "[" + white + "10" + green + "]" + white + " Linkedin" + green + "			[" + white + "21" + green + "]" + white + " Gamehag")
print(green + "[" + white + "11" + green + "]" + white + " Playstation" + green + "	        [" + white + "22" + green + "]" + white + " Mega")
print(red + "-----------------------------------------------------------------------")
print(green + "[" + white + "30" + green + "]" + white + " Send Phishing Email")
print(green + "[" + white + "69" + green + "]" + white + " Bypass Method ")
print(green + "[" + white + "80" + green + "]" + white + " Use Another Language " + red + "-New BETA")
print(green + "[" + white + "99" + green + "]" + red + " EXIT")
print(green + "[" + white + "1337" + green + "]" + white + " Info")
print(green + "[" + white + "4444" + green + "]" + white + " ToDo List\n")

def Welcome():
    os.systen("clear")
    















