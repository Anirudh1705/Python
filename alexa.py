import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import keyboard

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty("rate")
engine.setProperty('rate', 180)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #command.
            command = command.lower()
            if command in ['alexa']: 
                command = command.replace('alexa', '')
                print(command)
    except:
        command = None
    return command



def run_alexa():
    command = take_command()
    #print(type(command))
    print(command)
    if command in ["exit", 'quit']:
        talk("thank you for using me sir")
        exit()
    elif command in ['play']:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif command in ['time']:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif command in ['who the heck is']:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif command in ['date']:
        talk('sorry, I have a headache')
    elif command in ['are you single']:
        talk('I am in a relationship with wifi')
    elif command in ['joke']:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

ak = True

while ak != False:
    if keyboard.is_pressed('q'):
        ak = False
    run_alexa()
