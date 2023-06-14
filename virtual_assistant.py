import speech_recognition as sr
import pyttsx4
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia
import play_spotify

name = 'Lucia'

# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

engine = pyttsx4.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    flag = 1
    try:
        sr.Microphone.list_microphone_names()
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            flag = run(rec)
    except:
        pass
    return flag

def run(rec):
    if 'reproduce' in rec or 'pon' in rec:
        music = rec.replace('reproduce', '') or rec.replace('pon', '')
        talk('Reproduciendo ' + music)
        try:
            song, author = music.split('de', 2)
            author, noAuthor = author.split('sin', 2)
            play_spotify.main(song, author, noAuthor)
        except:
            pywhatkit.playonyt(music)
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'salir' in rec or 'cerrar' in rec or 'apagar' in rec:
        flag = 0
        talk("Saliendo...")
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

talk("Bienvenido mi nombre es Lucía, tu asistente virtual")
while flag:
    flag = listen()