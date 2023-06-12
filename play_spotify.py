from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import webbrowser
from time import sleep
import config

flag = 0
client_id = config.client_id
client_secret = config.client_secret
autor = 'Imagine Dragons' 
searchSong = "Enemy".lower()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
searchResult = sp.search(autor)
songList = searchResult["tracks"]["items"]
for i in range (0, len(songList)):
    nameSong = songList[i]["name"].lower()
    if searchSong in nameSong:
        songURL = songList[i]["uri"]
        webbrowser.open(songURL)
        pprint.pprint(nameSong)