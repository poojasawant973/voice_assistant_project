import pyttsx3 as p
import speech_recognition as sr
from selenium_web import Infow
from YT_audio import *
from News import *
import randfacts
from jokes import *
import requests
import datetime
from ss import key2

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Wishme():
    hour= int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return("Morning")
    elif hour >= 12 and hour < 16:
        return("Afternoon")
    else:
        return("evening")

def temp():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=' + key2
    json_data = requests.get(api_address).json()
    temperature = round(json_data["main"]["temp"] - 273.15)  # Convert from Kelvin to Celsius
    return temperature

def des():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=' + key2
    json_data = requests.get(api_address).json()
    description = json_data["weather"][0]["description"]
    return description

today_date = datetime.datetime.now()
speak("Hello, Good " + Wishme() + ", I'm your voice assistant.")
speak("Today is " + today_date.strftime("%A, %d %B %Y"))
speak("Temperature in New Delhi is " + str(temp()) + " degree Celsius" + " and with " + str(des()))

while True:
    speak("What can I do for you?")

    r = sr.Recognizer()
    r.energy_threshold = 10000

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Could you repeat?")
            speak("Sorry, I didn't catch that. Could you repeat?")
            continue
        except sr.RequestError as e:
            print(f"Error with the Google API request: {e}")
            speak("I encountered an error while processing your request.")
            continue

    text = text.lower()
    if "information" in text:
        speak("You need information related to which topic?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                infor = r.recognize_google(audio)
                speak(f"Searching {infor} in Wikipedia.")
                assist = Infow()
                assist.get_info(infor)
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Can you repeat?")
            except Exception as e:
                speak(f"Error: {e}")

    elif "play" in text and "video" in text:
        speak("You want me to play which video?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                vid = r.recognize_google(audio)
                print(f"Playing {vid} on YouTube.")
                assist = Music()
                assist.play(vid)
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Can you repeat?")
            except Exception as e:
                speak(f"Error: {e}")

    elif "news" in text:
        speak("Sure, now I will read the news for you.")
        try:
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
        except Exception as e:
            speak(f"Error fetching news: {e}")

    elif "fact" in text or "facts" in text:
        speak("Sure, here is a fact.")
        x = randfacts.get_fact()
        print(x)
        speak(f"Did you know that, {x}")

    elif "joke" in text or "jokes" in text:
        try:
            setup, punchline = joke()  

            print(setup)
            speak(setup)
            print(punchline)
            speak(punchline)
        except Exception as e:
            speak(f"Error fetching joke: {e}")

    elif "exit" in text or "quit" in text:
        speak("Goodbye! Have a great day!")
        break

    else:
        speak("I'm sorry, I can't help with that. Please try something else.")
