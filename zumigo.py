import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
from requests import get
import pywhatkit as kit
# from sys import platform
import sys
# from keyboard import press_and_release
import pyjokes
import time


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

# print(voices[0].id)
# print(voices[1].id)
# print(voices[2].id)

engine.setProperty('voice', voices[1].id)



def speak(audio):
       print(audio)
       engine.say(audio)  
       engine.runAndWait() #Without this command, speech will not be audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt= time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak("its "+tt)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  
        speak("its "+tt)

    else:
        speak("Good Evening!") 
        speak("its "+tt) 

    speak("I am Zumigo, a voice assistant made by Gautam. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,10)  #C:\Python310\Lib\site-packages\speech_recognition\__init__.py file to understand functionality
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='hi')
        # print(f"User said: {query}\n")   #f means formated string and it is used if we want to use a variable in between a String.

    except Exception as e:
       #  print(e)    
        speak("Say that again please...")   
        return "None"
    
    query = str(query).lower()
    return query
      
def TranslationHinToEng(Text):
    line=str(Text)
    translate = Translator()
    result = translate.translate(line)
    data=result.text
    print(f"User said: {data}\n")
    return data

def MicExecution():
    query=takeCommand()
    data=TranslationHinToEng(query)
    return data


if __name__=="__main__" :   #main method to use and test speak function 
       wishMe()
       while True:
    # if 1:
        query = MicExecution()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play songs' in query:
            music_dir = 'C:\\Users\\USER\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            rd = random.choice(songs)
            # os.startfile(os.path.join(music_dir, songs[2]))
            os.startfile(os.path.join(music_dir, rd))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "%windir%\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # elif 'close cmd' in query:
        #     speak("okay sir, closing command prompt")
        #     os.system("taskkill /f /im commandprompt.exe") 

        elif 'open cmd' in query:
            os.system("start cmd")

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # elif 'open camera' in query:
        #     cap =cv2.VideoCapture(0)  #0 means internal camera and 1 is for external camera
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('camera',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv2.destroyAllWindow()


        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif 'music on youtube' in query:
            kit.playonyt("Hanuman ashtak")

        elif 'shutdown' in query:
                os.system('shutdown /p /f')

        elif 'restart the system' in query:
                os.system('shutdown /r /t 5')

        elif 'sleep the system' in query:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
           
        elif 'quit' in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        # elif 'new tab' in query:
        #     press_and_release('ctrl+t') #press and release with press two buttons simultaneously

        # elif 'close tab' in query:
        #     press_and_release('ctrl+w')

        # elif 'new window' in query:
        #     press_and_release('ctrl+n')

       