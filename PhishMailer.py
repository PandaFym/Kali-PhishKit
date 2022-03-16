#!/usr/bin/env python3
#Created By Antrax

#Noraml Import
import time
import os
import sys
import json
import requests
from sys import version_info

if version_info<(3,0,0):
    print('[!] Please use Python3. $ python3 PhisherMailer.py')
    sys.exit()

#emails:
from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import BlockChain
from Core.eletter import Spotify 
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import Mega
from Core.eletter import RiotGames
from Core.eletter import Steam 
from Core.eletter import Gamehag
from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.eletter import Playstation
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import PayPal1
from Core.ipmenu import Snapchat
from Core.pre import * 
#Email-Sender
from Core.Mailer.MailerMain import *
from Core.helper.ToDo import TODO

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")

def CurrentDir():
    path = os.getcwd()
    print(green + "[" + white + "+" + green + "]" + white + " Your Template Will Be Saved Here " + path + '/TemplateName.html')

def mainMenu():
    menu()

    print(green)

    CurrentDir()

    mailPick = int(input(green + "root@phishmailer:~ " + white))

    try: 

        if mailPick == 1:
                Instagram()

        elif mailPick == 2:
                Facebook()
        
        elif mailPick == 3:
                Gmail()

        elif mailPick == 4:
                GmailActivity()

        elif mailPick == 5:
                Twitter()
            
        elif mailPick == 6: 
                Snapchat()
            
        elif mailPick == 7:
                SnapchatSimple()
            
        elif mailPick == 8:
                Steam()

        elif mailPick == 9:
                Dropbox()

        elif mailPick == 10:
                Linkedin()

        elif mailPick == 11:
                Playstation()
        
        elif mailPick == 12:
                PayPal1()
            
        elif mailPick == 13:
                Discord()
        
        elif mailPick == 14:
                Spotify()

        elif mailPick == 15:
                BlockChain()

        elif mailPick == 16:
                RiotGames()
        
        elif mailPick == 17:
                Rockstar()
        
        elif mailPick == 18:
                AskFM()
            
        elif mailPick == 19: 
                Webhost000()

        elif mailPick == 20:
                Dreamteam()

        elif mailPick == 21:
                Mega()

        elif mailPack == 30: 
                MailerMenu()

        elif mailPick == 69:
                RedirectionMain()

        elif mailPick == 80: 
                Languages()

        elif mailPick == 99:
            os.system("clear")
            print("Happy Phishing 01")
            print("Hope You Like This Tool") 
            sys.exit()

        elif mailPick == 1337: 
            print("/n" + green + "[" + white + "+" + green + "]" + white + "This Tool Was Created For People To Launch Phishing Attacks")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
            print("\n" + green + "[" + white + "+" + green + "]" + white + "But I Don't Give A Flying F*ck About What You Do With This;]") 
            CurrentDir()
            print(green + "[" + white + "+" + green + "]" + white + "Restart PhishMailer? Y/N")

            ReRun = input("root@phishmailer:~ " + white)
            if ReRun == "Y" or ReRun == "y":
                os.system("clear")
                mainMenu()
        else:
                os.system("clear")
                print(alert + " SHUTTING DOWN")
            
    elif mailPick == 4444:
        TODO()
        print(start + "Restart PhishMailer? Y/N")
        restart = input("root@phishmailer:~ " + whtie)
        if restart == "Y" or restart "y":
            os.system("clear")
            mainMenu()
    else: 
            print("\nSomething Went Wrong There Buddy")
            print("Are You Okay? Did You Get Hit In The Face By A Fuck You?")
            sys.exit

  except ValueError:
            print("\nSomething Went Wrong There Buddy")
            print("Are You Okay? Did You Get Hit In The Face By A Fuck You?")

mainMenu()                   