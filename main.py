from pprint import pprint
import sched
import time
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

#Configs
SPOTIPY_CLIENT_ID = credentials.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = credentials.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = credentials.SPOTIPY_REDIRECT_URI
SCOPE = credentials.SCOPE

#Spotify definition of authentication
spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                     client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

def internet_on():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def request(url):
    print("Todo")

url = input("Enter URL of Apple Playlist")