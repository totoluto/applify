# applify
This Python Script creates a Spotify Playlist based on an Apple Playlist. But first you need to configure your config file (Paste client ID and secret and configure redirect link). And afterwards you need to create a playlist in Spotify and also copy this ID into your config file. Then you'll be able to paste the link into the console after starting your application.

## How does it work?

Well your application is going to try and reach the website and download the HTML. Afterwards it will search for the JSON Dictonary in the HTML and create one on its own. Now the application is reaching out to the Spotify API and search the Spotify link of the song. When it went through all the songs it will add the songs to the premade playlist.

## Why premade playlist and not a new one?

All my friend are using Spotify exept for this **ONE** person and it annoys me. I want to have all the song this person sends me in one playlist. That's why I didn't even considered creating a new playlist because i want all of the songs which were added by this application in one Playlist.

## Questions?

If you have any questions you are allowed to create an issue.
