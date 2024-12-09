import pyttsx3 as p

#convert speach
import speech_recognition as sr
from selenium_web import Infow
from YT_audio import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text) :
    engine.say(text)
    engine.runAndWait()

# print(voices)

r = sr.Recognizer()

speak("Hello, I'm your voice assistance. How are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, duration=1)

    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good day")
speak("what can i do for you ?")


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, duration=1)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if 'information' in text2:
    speak("You need information related to which topic? ")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak("Searching {} in wikipedia" .format(infor))
    print("Searching {} in wikipedia" .format(infor))

    assist = Infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
    speak('You want me to play which video?')
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on  youtube" .format(vid))
    assist = Music()
    assist.play(vid)
