import os
from dotenv import load_dotenv, dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

app = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def search(artist):
    results = app.search(q=artist, type="track", limit=3)

    songs = []
    for track in results['tracks']['items']:
        songs.append({
            "title": track['name'],
            "link": track['external_urls']['spotify'],
            "cover_art": track['album']['images'][0]['url']
        })

    return songs
