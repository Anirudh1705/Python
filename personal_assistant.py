import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendgmail(content, to):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS for network security
    s.starttls()
    # User email Authentication
    s.login(" ", password=" ")
    s.sendmail(" ", to, msg=content)


def wish():
    time =  datetime.datetime.now().hour
    if time>=0 and time<12:
        speak("Good Morning Sir!")
    elif time>=12 and time<18:
        speak("Good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("Sir I am Your Assistance Please let me now a command")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User Said:", query)
    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"
    return query

if __name__ == '__main__':
    wish()
    while True:
        query = takecommand().lower()
        command = ["wikipedia", "youtube","close", "hackerrank", "online music", "offline music","time", "mail","blogspot"]
        if  command[0] in query:
            speak("Searching wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 20)
                speak(f"According to wikipedia..")
                speak(results)
            except Exception as e:
                print(e)
                pass
        elif command[1] in query:
            speak("ok I am opening yt")
            webbrowser.open(url="www.youtube.com")
        elif command[2] in query:
            speak("Ok I am quiting Now you Play me again later if you want")
            exit()
        elif command[3] in query:
            speak("ok I am opening Hackerrank site")
            webbrowser.open(url="www.hackerrank.com")
        elif command[4] in query:
            speak("ok i am opening youtube music")
            webbrowser.open(url="https://music.youtube.com/")
        elif command[5] in query:
            music = r"H:\Desi Kalakaar (2014) Honey Singh Mp3 Songs 190Kbps Zip\Desi Kalakaar (2014) Yo Yo Honey Singh 190Kbps"
            songs = os.listdir(music)
            print(songs)
            speak("ok i will play some music")
            import random
            a = random.randint(1,8)
            list1 = (a)
            os.startfile(os.path.join(music, songs[list1]))
        elif command[6] in query:
            speak(datetime.datetime.now())
        elif command[7] in query:
            try:
                speak("input below to whome you want to mail")
                content = input("Enter Here Your Content: ")
                to = input("to whome you want to send this content: ")
                sendgmail(content, to)
                speak("ok done here...")
            except Exception as e:
                print(e)
                speak("let me know again..")
                content = input("Enter Here Your Content: ")
                to = input("to whome you want to send this content: ")
                sendgmail(content, to)
                speak("ok done here...")
        elif command[8] in query:
            speak("ok i am opening blogspot as your wish")
            webbrowser.open(url="https://blogspot.com/")
        elif "printerest" in query:
            speak("Ok I am Opening printerest")
            webbrowser.open(url="https://in.pinterest.com/CramationsDam/")
