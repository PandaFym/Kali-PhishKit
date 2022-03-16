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
        test = requests.get()