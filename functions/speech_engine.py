from datetime import datetime
import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from functions.utils import OPENING_TEXT

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

EXIT_KEY_WORDS = ['exit', 'stop', 'quit', 'cancel', 'shutdown', 'turnoff']

# Configure Speech Engine

engine = pyttsx3.init('sapi5') # sapi5 = Microsoft Speech APiI
# Set Rate
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)
# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text:str) -> None:
    """Speak whaterver text is passed in."""
    engine.say(text)
    engine.runAndWait()

def greet_user() -> None:
    """Greets the user according to the time of day"""
    hour = datetime.now().hour # hour in 24hr time
    if hour < 12:
        speak(f'Good Morning {USERNAME}')
    if hour >= 12 and hour < 16:
        speak(f'Good Afternoon {USERNAME}')
    if hour >= 16 and hour <= 24:
        speak(f'Good Evening {USERNAME}')
    # Offer Assistance
    speak(f'I am {BOTNAME}. How may i assist you?')

def __should_exit_app(query) -> bool: 
    """Check if app should close, return True or False"""
    for word in EXIT_KEY_WORDS:
        if word in query:
            return True
    return False


def take_user_input() -> str:
    """
    Takes user input uses SpeechRecognition Module and converts to text
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, key=None, language="en-AU")
        if not __should_exit_app(query):
            speak(choice(OPENING_TEXT))
            return query
        else:
            speak('Goodbye Sir!')
            exit()
    except sr.RequestError as e:
        print(f"Request error with api, error {e}")
        query = 'none'
        return query
    except sr.UnknownValueError as e:
        print(f"Unable to recognize speech, error {e}")
        query = 'none'
        return query
    
