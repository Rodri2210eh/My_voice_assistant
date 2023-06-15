from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import webbrowser
import config

def main(searchSong, author = '', noAuthor =  ''):
    client_id = config.client_id
    client_secret = config.client_secret
    
    searchSong = clean_input(searchSong)
    author = clean_input(author)
    noAuthor = clean_input(noAuthor)
    print(searchSong)
    print(author)

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    searchResult = sp.search(searchSong)
    songList = searchResult['tracks']['items']
    if author:
        for i in range (0, len(songList)):
            artists = songList[i]['artists']
            if check_artists(author, artists, noAuthor):
                reproduce(songList, i)
                pprint.pprint(songList[i]['name'])
                break
    else:
        reproduce(songList, 0)
        
def clean_input(input):
    input = input.lower()
    if input[0] == " ":
        input = input[1:]
    if input[len(input) -1] == " ":
        input = input[:len(input)-2]
    return input

def check_artists(author, artists, noAuthor):
    flag = 0
    for i in range (0, len(artists)):
        if not flag:
            if author in artists[i]['name'].lower():
                flag = 1
        else:
            if noAuthor and (noAuthor in artists[i]['name'].lower()):
                flag = 0
    return flag

def reproduce(songList, i):
    songURL = songList[i]['uri']
    webbrowser.open(songURL)