from chatOptions import loc, tim, langChange,web,sch
from sentence_splitter import SentenceSplitter
from deep_translator import GoogleTranslator
from voiceSetup import Speaker
from bs4 import BeautifulSoup
from queue import Queue
from time import sleep
import webbrowser
import pywhatkit
import requests
import datetime
import re

def hello_en(speaker, qu):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speaker.talk(qu, "Good morning!")
    elif hour>= 12 and hour<18:
        speaker.talk(qu, "Good afternoon!") 
    else:
        speaker.talk(qu, "Good evening!")


def english(speaker, qu):
    #anglais

    def time(speaker,qu):
        time = datetime.datetime.now().strftime('%I:%M %p')
        speaker.talk(qu, 'Current time is ' + time)
        

    
    speaker.setLanguage("en")
    hello_en(speaker, qu)

    speaker.talk(qu, "My name is Prestini Chat ... ")
    speaker.talk(qu, "I can tell you about:")
    speaker.talk(qu, "Time, Pristini School , Pristini programs , Pristini localisation , Pristini website   ")
    speaker.talk(qu, "what do you want?")
    while True:
        command = speaker.take_command(qu)

        if command.lower() in tim:
            time(speaker, qu)
      
        elif command.lower() in loc:
            url = 'https://www.google.nl/maps/place/Pristini+School+of+AI/@35.8137892,10.5977588,17z/data=!3m1!4b1!4m6!3m5!1s0x12fd8b8eda2f9373:0x3db9b6e75849f637!8m2!3d35.8137849!4d10.5999475!16s%2Fg%2F11jz3d2n5b'
            webbrowser.open(url)
            sleep(2)

        elif command.lower() in  web:
            speaker.talk('Pristini website ')
            webbrowser.open("https://www.pristiniaiuniversity.tn/fr")
        
        elif "thank you" in command:
            speaker.talk("Welcome !")

        
        elif command.lower() in sch :
            print("Welcome ! \n - Pristini School Of AI Breaks Down The Boundaries Between IT, Business And Ethics. Those who operate at Pristini - to learn, research, teach, or work - join a community invested in the quest for knowledge and a human-centered world. \n -  2022 : Year of creation of Pristini School of AI \n - 13000 m2 : premises dedicated to innovation & creativity \n - 10: Areas of specialization \n - 40 % International teachers ")
            speaker.talk("Welcome ! \n - Pristini School Of AI Breaks Down The Boundaries Between IT, Business And Ethics. Those who operate at Pristini - to learn, research, teach, or work - join a community invested in the quest for knowledge and a human-centered world. \n -  2022 : Year of creation of Pristini School of AI \n - 13000 m2 : premises dedicated to innovation & creativity \n - 10: Areas of specialization \n - 40 % International teachers ")
            
       

        elif command.lower() in ["exit", "quitter", "quit", "cancel", "no"]:
            speaker.talk(qu, "Thank you for using our service, see you soon!")
            speaker.talk(qu, "exit")
            break
            
        elif command.lower() in langChange:
            from frenchVersion import french
            french(speaker, qu)

        speaker.talk(qu, 'Want something else?')
