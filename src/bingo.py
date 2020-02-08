import spotipy
import spotipy.util as util
import sys
import os
from dotenv import load_dotenv

def login():
    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Spotify username: ")

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

def test():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify()

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

def loadPrivateEnvFile(privateEnvFile = 'private.env'):
    if os.path.isfile(privateEnvFile):
        load_dotenv(privateEnvFile)

if __name__ == "__main__":
    loadPrivateEnvFile()
    login()
    test()