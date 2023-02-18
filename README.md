# Python Script to Sync Audio Files to Spotify

This is a Python script that reads all audio files in a directory and syncs the songs to a user's Spotify library using the Spotify API.

## Requirements

To use this script, you will need:

- Python 3.x
- The following Python packages:
  - `os`
  - `spotipy`
  - `pandas`
  - `mutagen`

## Usage

To use this script, follow these steps:

1. Create a Spotify Developer Account by going to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and clicking the "Log in" button. If you don't have a Spotify account, you'll need to create one.

2. Once you're logged in to the Spotify Developer Dashboard, click the "Create an App" button and fill in the necessary information to create a new Spotify Application. This will give you a client ID and client secret that you will need to use the Spotify API.

3. Install the necessary Python packages by running the following command in your terminal:

```
pip install spotipy pandas mutagen
```

4. Download the Python script to your local machine.

5. Open a command prompt or terminal and navigate to the directory where the script is saved.

6. Run the script using the following command:

```
python sync_to_spotify.py
```

7. When prompted, enter your Spotify API client ID and the directory path where your audio files are saved.

8. The script will search for each audio file on Spotify and add it to your Spotify library if a match is found. If a match is not found, the script will add the file to a separate Excel file that lists all failed track syncs.

## Setting up the Spotify API

To use the Spotify API, you'll need to create a new Spotify Application and obtain a client ID and client secret. Follow these steps to set up the Spotify API:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.

2. Click the "Create an App" button and fill in the necessary information to create a new Spotify Application.

3. Once your application is created, you'll be taken to the application dashboard. Here, you'll see your client ID and client secret. Make note of these, as you'll need them to authenticate your session with the Spotify API.

4. Under "Settings" in the left sidebar, click "Edit Settings" and add a "Redirect URI" for your application. This is the URL that Spotify will use to redirect users after they authenticate with your application.

5. You're now ready to use the Spotify API with your application.
