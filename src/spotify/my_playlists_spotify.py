import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from unicodedata import normalize
from common.common_functions import clean_input
from time import sleep
import pyautogui

def main(playlist):
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(config.client_id,config.client_secret,'https://developer.spotify.com' ,scope=scope))
    playlist = clean_input(playlist)
    playlist = delete_accent(playlist)
    print(playlist)
    
    results = sp.current_user_playlists(limit=50)
    
    for i, item in enumerate(results['items']):
        print("%d %s" % (i, item['name']))
        print()
        if playlist in item['name'].lower():
            reproduce(item)

def reproduce(playlist):
    webbrowser.open(playlist['uri'])
    sleep(4)
    clickImage('src/img/play_spotify.PNG')

def clickImage(imgSRC):
    location = pyautogui.locateOnScreen(imgSRC)
    pyautogui.click(location)

def delete_accent(playlist):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    return normalize('NFKC', normalize('NFKD', playlist).translate(trans_tab))