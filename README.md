# List_YT_Playlist_Titles
This Python script allows you to extract and display the titles of all videos from a YouTube playlist using the YouTube Data API v3.

## Requirements

To run this script, you'll need:

- Python 3.x
- **Google API Python Client**: This library is required to interact with the YouTube Data API.
  
You can install the necessary Python library by running:

```bash
pip install google-api-python-client
```

## Getting Started

1. **Get a Google API Key**:
   - Go to the [Google Developer Console](https://console.developers.google.com/).
   - Create a new project.
   - Enable the **YouTube Data API v3**.
   - Create an API key under **Credentials**.

2. **Obtain the Playlist ID**:
   - The **Playlist ID** can be found in the URL of the playlist on YouTube. For example:
     - If the URL is `https://www.youtube.com/playlist?list=PLD5S3VjL2Do3lb7P8tBC8XB4Kw_7_24hX`, the Playlist ID is `PLD5S3VjL2Do3lb7P8tBC8XB4Kw_7_24hX`.

3. **Update the Script**:
   - Replace `"YOUR_API_KEY"` in the script with your generated Google API Key.
   - Replace `"PLAYLIST_ID"` with the actual playlist ID.

4. **Run the Script**:
   - Execute the Python script, and it will print out the titles of all videos in the specified YouTube playlist.

## Usage

### Example:

```bash
python playlist_titles.py
```

The script will output a list of video titles from the specified playlist:

```
Video Titles in Playlist:
1. Title of Video 1
2. Title of Video 2
3. Title of Video 3
...
```

## Script Breakdown

- **`get_video_titles_from_playlist(api_key, playlist_id)`**: This function interacts with the YouTube API to fetch video titles from the provided playlist ID. It handles pagination to ensure that all videos are retrieved, even if the playlist contains more than 50 videos.
  
- **Main Execution Block**: 
  - The script takes the API key and playlist ID as inputs.
  - It calls the `get_video_titles_from_playlist()` function and prints each video title.

