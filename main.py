from cgi import test
from pprint import pprint
import urllib
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials
import requests
import json
import os

# Configs
SPOTIPY_CLIENT_ID = credentials.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = credentials.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = credentials.SPOTIPY_REDIRECT_URI
SCOPE = credentials.SCOPE

# Spotify definition of authentication
spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                 client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))


def internet_on():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

# Saves a tmp html of the Apple Music Website
def fetchApplePlaylist(url):
    if os.path.exists("tmpWebsite.html"):
      os.remove("tmpWebsite.html")
    f = requests.get(url)
    html = f.text

    g = open("tmpWebsite.html", "a", encoding="utf-8")
    g.write(html)
    g.close()

# Searches the Json with songs in the html file
def searchHtml():
    if os.path.exists("songs.json"):
      os.remove("songs.json")
    with open("tmpWebsite.html", encoding="utf8") as html:
        for line in html:
            if '{"@context"' in line:
                dictionary = line
                break
    json_string = json.loads(dictionary)
    json_object = json.dumps(json_string, indent=4)

    with open("songs.json", "w") as outfile:
        outfile.write(json_object)

# Main

if internet_on():
    url = input("Enter URL of Apple Playlist: \n")
    fetchApplePlaylist(url=url)
    searchHtml()
else:
    print("No Connection")
    exit
