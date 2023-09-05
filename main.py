import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import datetime


def say(query):
    engine = pyttsx3.init()
    engine.say(query)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said {query}")
            return query
        except Exception as e:
            return "Some error as Occord. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis a I am the assistant of Manish and I am designed for to make life easier just try to give me command Open Whitehat")

    while True:
        print(f"Listening......")
        query = takeCommand()
        # todo: Add more websites
        sites = [["whitehat", "https://code.whitehatjr.com/"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["youtube", "https://www.youtube.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                # todo: add more songs
            if "open music" in query:
                music_path="C:/Users/manis/Downloads/128-Phir Aur Kya Chahiye - Arijit Singh 128 Kbps.mp3"
                os.startfile(music_path)

            if "the time".lower() in query.lower():
                Hours = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"sir the time is {Hours}  hours {min} minute ")

            if "open code".lower() in query.lower():
                code = "C:/Users/manis/AppData/Local/Programs/Microsoft VS Code.exe"
                os.startfile(code)



