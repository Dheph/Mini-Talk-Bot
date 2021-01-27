import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import time

listener = sr.Recognizer()
engine = pyttsx3.init()  

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
           
            if 'charles' in command:
                command = command.replace('charles','')
                print(command)
            return command
    except:
        pass
    return ''

def run_charles():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'search' in command:
        song = command.replace('search','')
        talk('searching' + song)
        pywhatkit.search(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
        
    elif 'what is' in command:
        el = command.replace('what is','')
        info = wikipedia.summary(el,1)
        print(info)
        talk(info)
        
    elif 'open' in command:
        app = command.replace('open','')
        os.system(app)
        talk('opening ' + app)
        
    elif 'good morning' in command:
        talk('Good morning Dheph')
        os.system('google-chrome https://music.youtube.com/watch?v=l9nh1l8ZIJQ&list=RDAMVMl9nh1l8ZIJQ')
        os.system('google-chrome https://go.botmaker.com/#/home')        
        os.system('lxterminal')        
    else:
        return 
     
# run_charles()
while True:  
    time.sleep(2)
    run_charles()
