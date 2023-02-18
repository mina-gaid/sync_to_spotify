import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
import pandas as pd

# Ask the user to enter their Spotify API key
client_id = input("Enter your Spotify API key: ")

# Set up the Spotify API authentication and permissions
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, scope="user-library-modify"))

# Ask the user to enter a directory path
directory = input("Enter the directory path: ")

# Create an empty DataFrame to store the failed track syncs
failed_tracks = pd.DataFrame(columns=["File Name", "Song Name", "Album Name", "Artist Name", "Reason"])

# Loop through all files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if file_name.endswith(".mp3"):
        # Load the ID3 tags from the MP3 file using the Mutagen library
        tags = EasyID3(file_path)
    elif file_name.endswith(".flac"):
        # Load the tags from the FLAC file using the Mutagen library
        tags = FLAC(file_path)
    else:
        # Skip the file if it is not an MP3 or FLAC file
        continue

    # Extract the song, album, and artist names from the tags
    song_name = tags.get("title", [""])[0]
    album_name = tags.get("album", [""])[0]
    artist_name = tags.get("artist", [""])[0]
    
    # Use the Spotify API search endpoint to find the first track that matches the song, album, and artist names
    query = f"{song_name} album:{album_name} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=1)
    if len(results["tracks"]["items"]) > 0:
        track_id = results["tracks"]["items"][0]["id"]
        
        # Use the Spotify API add-to-library endpoint to add the track to the user's Spotify library
        sp.current_user_saved_tracks_add([track_id])
        
        # Print a message indicating that the track was added
        print(f"Added {song_name} by {artist_name} to your Spotify library.")
    else:
        # Add a row to the failed tracks DataFrame
        failed_tracks = failed_tracks.append({
            "File Name": file_name,
            "Song Name": song_name,
            "Album Name": album_name,
            "Artist Name": artist_name,
            "Reason": "Could not find a match on Spotify"
        }, ignore_index=True)
        
        # Print a message indicating that the track was not found
        print(f"Could not find a match for {song_name} by {artist_name} on Spotify.")

# Write the failed tracks DataFrame to an Excel file
failed_tracks.to_excel("failed_tracks.xlsx", index=False)
