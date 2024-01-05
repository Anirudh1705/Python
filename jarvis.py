import speech_recognition as sr  # pip install speechRecognition
import pyttsx3, wikipedia, webbrowser,smtplib  # pip install wikipedia webbrowser secure-smtplib pyttsx3
import os, datetime #inbuilt module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)#0 for male and 1 for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    a="I am Ak. Please tell me how may I help you sir"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!"+a)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!"+a)
    else:
        speak("Good Evening!"+a)
    
def takeCommand():

    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akgamerzyt4@gmail.com', 'Anirudhk@1705')
    server.sendmail('akgamerzyt4@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir ='C:\\Users\\ANIRU\\Music\\sad'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\code.exe"
            os.startfile(codePath)
        elif 'mail to Ak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Anirudhsharma9893@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ak bhai. I am not able to send this email")
        elif 'exit' in query:
            print("Thank you for using me sir")
            speak("Thank you for using me sir")
            exit()
        elif 'close' in query:
            print("Thank you for using me sir")
            speak("Thank you for using me sir")
            exit()
        else:
            speak('Please say the command again.')
