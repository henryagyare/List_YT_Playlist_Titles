!pip install google-api-python-client  # Install necessary library.

import os
import googleapiclient.discovery

# Function to get video titles from a playlist
def get_video_titles_from_playlist(api_key, playlist_id):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    
    # List to store video titles
    video_titles = []
    
    # Initial request to get videos from the playlist
    next_page_token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        # Extract video titles
        for item in response["items"]:
            title = item["snippet"]["title"]
            video_titles.append(title)
        
        # Check if there is another page of results
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return video_titles

# Main function
if __name__ == "__main__":
    # Your YouTube API Key
    api_key = "YOUR_API_KEY"  # Replace with your Google API key
    
    # Playlist ID (can be extracted from the YouTube playlist URL)
    playlist_id = "PLAYLIST_ID"  # Replace with ID of the desired playlist.
    
    # Get the list of video titles
    video_titles = get_video_titles_from_playlist(api_key, playlist_id)
    
    # Print out the video titles
    print("Video Titles in Playlist:")
    for title in video_titles:
        print(title)  # Prints the titles
