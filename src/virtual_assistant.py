import speech_recognition as sr
import pyttsx4
import pywhatkit
import common.common_functions as common_functions
import datetime
import wikipedia
import spotify.play_spotify as play_spotify
import spotify.my_playlists_spotify as my_playlists_spotify
import pyjokes
import conectOpenAI

name = 'lucía'

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
            rec = rec.replace(name, '')
            flag = run(rec)
    except:
        pass
    return flag

def run(rec):
    print(rec)
    if 'reproduce' in rec or 'pon' in rec:
        musicReplace = ['reproduce', 'pon']
        music = replaceList(musicReplace, rec)
        music = common_functions.clean_input(music)
        print(music)
        if 'playlist' in music or 'playlists' in music or 'la playlist' in music or 'mi playlist' in music:
            playlistReplace = ['playlist', 'playlists', 'mi playlist', 'la playlist']
            playlist = replaceList(playlistReplace, music)
            playlist = common_functions.clean_input(playlist)
            talk('Reproduciendo ' + playlist)
            my_playlists_spotify.main(playlist)
        else:
            try:
                talk('Reproduciendo ' + music)
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
    elif 'chiste' in rec:
        chiste = pyjokes.get_joke("es")
        talk(chiste)
    elif 'salir' in rec or 'cerrar' in rec or 'apagar' in rec:
        flag = 0
        talk("Saliendo...")
    else:
        message = conectOpenAI.processQuestion(rec)
        talk(message)
    return flag

def replaceList(elementReplace, replaceString):
    for i in range (0, len(elementReplace)):
        replaceString = replaceString.replace(elementReplace[i], '')
    return replaceString

talk("Bienvenido mi nombre es Lucía, tu asistente virtual")
while flag:
    flag = listen()
    