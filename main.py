import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from bs4 import BeautifulSoup
from time import sleep
import webbrowser
import requests
import datetime
import re
from voice import talk,take_command
from chatbotPrest import *



while True:
    command = take_command()
    print(command)

    chatbot(command)