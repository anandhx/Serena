import pywhatkit
import webbrowser
import requests
from bs4 import BeautifulSoup
import win32com.client
import speech_recognition as sr
import wikipedia
import datetime
import pyautogui

import random

from time import sleep
from pynput.keyboard import Key,Controller
import win32com.client
keyboard = Controller()
def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def volumeup(percentage):
    number_of_times = percentage/2
    try:
        number_of_times = int(number_of_times)
        for i in range(number_of_times):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)
    except:
        say('Sorry Anandhu,Some error occured ,Please try again')
def volumedown(percentage):
    number_of_times = percentage/2
    try:
        number_of_times = int(number_of_times)
        for i in range(number_of_times):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)
    except:
        say('Sorry Anandhu,Some error occured,Please try again')


def say(script):
    '''This function says out loud whatever string is given to it'''
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    return speaker.Speak(script)
def take_command():
    '''This function takes voice input from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.energy_threshold = 500
        audio = r.listen(source)
        try:
            say('Recognizing')
            query = r.recognize_google(audio, language= 'en-in')
            print(f'User said: {query}\n')
            return query
        except Exception as e:
            return 'Some Error Occurred. Sorry from Jarvis'
def Greet_Me():
    '''This function greets the user'''
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <= 12:
        say('Good morning,Anandhu')
    elif hour > 12 and hour <= 15:
        say('Good Afternoon,Anandhu')
    else:
        say('Good Evening,Anandhu')
    say('Hope you are having a good day,How can I help you?')
def Search_Google(query):
    '''This function searches google for "query" and shows the results.It also speaks out loud a summary of the results'''
    import wikipedia as googleScrap
    query = query.replace('jarvis','')
    query = query.replace('search google for','')
    query = query.replace('google','')
    say('Anandhu ,this is what I found on Google')
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,3)
        say(result)
    except :
        say('Sorry Anandhu there is no speakable output available')
def Search_Youtube(query):
    '''This function searches YouTube for "query" and plays the most popular video/short that it finds.'''
    say('Anandhu this is what I found for your search on Youtube!')
    query = query.replace('jarvis','')
    query = query.replace('search youtube for','')
    query = query.replace('youtube','')
    try:
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        say('Anandhu these are the related videos I found ,Give me a minute I am going to play the most popular one')
        pywhatkit.playonyt(query)
        say('Done Anandhu')
    except:
        say('Sorry Anandhu .Some error occurred I was not able to complete your request')
def Search_Wikipedia(query):
    '''This function searches wikipedia for "query" and speaks out loud the summary that it finds'''
    say('Searching from Wikipedia......')
    query = query.replace('jarvis','')
    query = query.replace('search wikipedia for', '')
    query = query.replace('wikipedia', '')
    try:
        results = wikipedia.summary(query,sentences = 3)
        say('According to Wikipedia ......')
        say(results)
        print(results)
    except:
        say(f'I am sorry,Anandhu Either I heard you wrong or there was no information for {query} on wikipedia')
Greet_Me()
information = False
remember = ''
while True:
    say('Listening')
    print('Listening')
    query = take_command().lower()
    if 'the time'.lower() in query:
        Time = datetime.datetime.now().strftime('%H:%M:%S')
        say(f'Anandhu,the time is {Time}')
    elif 'introduce yourself'.lower() in query:
        say('I am a virtual voice assistant developed by anandhx')
    elif 'go offline' in query or 'shut off' in query or 'shutdown' in query  or 'shut down' in query:
        say('Okay Anandhu.Jarvis is going offline')
        quit()
    elif 'Pause'.lower() in query:
        pyautogui.press('k')
        say('Done,Anandhu.The video has been Paused')
    elif 'Play'.lower() in query:
        pyautogui.press('k')
        say('Done,Anandhu.The video has been Played')
    elif 'mute'.lower() in query:
        pyautogui.press('m')
        say('Done Anandhu,The video has been muted')
    elif 'unmute'.lower() in query:
        pyautogui.press('m')
        say('Done Anandhu,The video has been unmuted')
    elif 'increase the volume' in query:
        say('Anandhu how much percentage would you like the volume to be increase by?Please tell a even number.Only say the percentage value')
        try:
            increase_percentage = take_command()
            increase_percentage = increase_percentage.replace('percent','')
            increase_percentage = increase_percentage.replace('percentage', '')
            increase_percentage = increase_percentage.replace('%','')
            increase_percentage = int(increase_percentage)
            if increase_percentage % 2 != 0:
                while increase_percentage % 2 != 0:
                    increase_percentage += 0.1
            say('Okay Anandhu,Turning up the volume')
            volumeup(increase_percentage)
        except:
            say('Sorry Anandhu ,Some error occurred Please try again')
    elif 'decrease the volume' in query:
        say('Anandhu how much percentage would you like the volume to be increase by?Please tell a even number.')
        try:
            decrease_percentage = take_command()
            decrease_percentage = decrease_percentage.replace('percent', '')
            decrease_percentage = decrease_percentage.replace('percentage', '')
            decrease_percentage = decrease_percentage.replace('%', '')
            decrease_percentage = int(decrease_percentage)
            if decrease_percentage % 2 != 0:
                while decrease_percentage % 2 != 0:
                    decrease_percentage += 1
            say('Okay Anandhu Turning down the volume')
            volumedown(decrease_percentage)
        except:
            say('Sorry Anandhu,Some error occurred please try again')
    elif 'I am fine'.lower() in query:
        say('That is great Anandhu')
    elif 'Thank you'.lower() in query:
        say('You are welcome ,Anandhu')
    elif 'open' in query:
        increase_percentage = take_command()
        from Dictapp import openappweb
        openappweb(query)
    elif 'close' in query:
        from Dictapp import closeappweb
        closeappweb(query)
    elif 'Google'.lower() in query:
        Search_Google(query)
    elif 'Youtube'.lower() in query:
        Search_Youtube(query)
    elif 'Wikipedia'.lower() in query:
        Search_Wikipedia(query)
    elif 'temperature'.lower() in query:

        search = 'temperature in Kottayam'
        if 'in' in query:
            query = query.replace('what is the','')
            query = query.replace('jarvis','')
            search = query
        url = f'https://search.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = getattr(data.find('div', class_ = "BNeawe"), 'text', None)
        say(f'Anandhu the current {search} is {temp}')
    elif 'remember that' in query:
        query = query.replace('jarvis','')
        query = query.replace('i want you to', '')
        query = query.replace('remember that', '')
        query = query.replace('i', 'you')
        remember += query
        say(f'OKay Anandhu,I wil remember {remember}')
    elif 'What do you remember' in query:
        say(f'Anandhu,You told me to remember that {remember}')
    elif 'forget' in query:
        say('Okay Anandhu I am Going to forget whatever you told me')
        remember = ''
    elif 'Hello'.lower() or 'how are you'.lower() in query:
        say('Sorry Anandhu,I could not understand what you just said')
