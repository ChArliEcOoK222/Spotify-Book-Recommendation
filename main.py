# Libraries required for functionality
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Clear the terminal/shell
os.system('clear')

# Function to get the listening history of users from Spotify
def listening_history():
    # Clear the terminal/shell again
    os.system('clear')

    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='',
        client_secret='',
        redirect_uri='http://127.0.0.1:3000/callback',
        scope='user-top-read'
    ))

    # Getting the top artists and saving them to a variable
    top_artists = sp.current_user_top_artists(limit=10, time_range="short_term")
    # Outputting the top artists
    for idx, artist in enumerate(top_artists['items']):
        print(f"{idx + 1}. {artist['name']}")

listening_history()