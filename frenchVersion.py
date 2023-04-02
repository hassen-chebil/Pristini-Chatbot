
from chatOptions import loc, tim, langChange,web
from voiceSetup import Speaker
from bs4 import BeautifulSoup
from queue import Queue
from time import sleep
import webbrowser
import pywhatkit
import requests
import datetime
import re


def hello_fr(speaker, qu):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.talk(qu, "Bonjour !")
    elif hour>= 12 and hour<18:
        speaker.talk(qu, "Bonne après-midi !") 
    else:
        speaker.talk(qu, "Bonsoir !")


def french(speaker, qu):
    #francais       

    def time(speaker, qu):
        time = datetime.datetime.now().strftime('%I:%M %p')
        speaker.talk(qu, "L'heure actuelle est " + time)
        
    
    speaker.setLanguage("fr")
    hello_fr(speaker, qu)
    
    speaker.talk(qu, "Je m'appelle Prestini Chat...")       
    speaker.talk(qu, "Je peux vous parler de:")
    speaker.talk(qu, "Heure, École Pristini , Programmes Pristini , Localisation Pristini , Site Web Pristini")
    speaker.talk(qu, "Que voulez-vous?")
    while True:
        command = speaker.take_command(qu)
        
    
        if command in tim:
            time(speaker, qu)


        elif command in loc:
            url = 'https://www.google.nl/maps/place/Pristini+School+of+AI/@35.8137892,10.5977588,17z/data=!3m1!4b1!4m6!3m5!1s0x12fd8b8eda2f9373:0x3db9b6e75849f637!8m2!3d35.8137849!4d10.5999475!16s%2Fg%2F11jz3d2n5b'
            webbrowser.open(url)
            sleep(2)
        elif command.lower() in web :
            speaker.talk('Pristini website ')
            webbrowser.open("https://www.pristiniaiuniversity.tn/fr")

        elif command.lower() in ["exit", "quitter", "quit", "cancel", "non"]:
            speaker.talk(qu, "Merci d'utiliser notre service, à bientôt!")
            speaker.talk(qu, "exit")
            exit()

        elif "merci" in command:
            speaker.talk("de rien !")

        elif command.lower() in langChange:
            from englishVersion import english
            english(speaker, qu)

        speaker.talk(qu, 'Vous voulez autre chose?')