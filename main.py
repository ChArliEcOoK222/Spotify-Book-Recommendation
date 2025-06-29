# How do I run this in a bash script?
# How do I add this to a Alfred workflow?

# Libraries required for functionality
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import openai
from openai import OpenAI
import pyperclip

# Clear the terminal/shell
os.system('clear')

# Creating a new OpenAI client from the API key
client = OpenAI(
    api_key=""
)

# List to store the most listened to artists from the last 30 days
top_artists_list = []
# Variable to store a short description of myself
personality_description = ""

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
    # Appending the top artists to the top artists list
    for idx, artist in enumerate(top_artists['items']):
        top_artists_list.append(f"{idx + 1}.{artist['name']}")

# Calling the function in order to obtain this top artists list
listening_history()

# Using GPT 4.1 to match the user's personality description and the main themes of their most listened to artists to books
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": f"Based on the following list of my top 10 artists and description of my personality, match the main themes of these artists with the main themes of books recommended to my personality. Order these books in a numbered list based on my preference for these. The list should only include the book name and author, no reasons for why it is recommended or the themes of the book in brackets below, also do not add an introductory message, just get straight into the list: {top_artists_list} and {personality_description}."}],
    max_tokens=4096,
    n=1
)

# Accessing the message content of the output and saving it to a variable
response_message = response.choices[0].message.content
# Copying the response_message to clipboard 
pyperclip.copy(response_message)