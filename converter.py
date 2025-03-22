import ytmusicapi
import ytmusicapi
import json
import requests

# Update these with instructions from the readme
spotifyID="<<AppID>>"
spotifySecret="<<AppSecret>>"
spotifyPlaylist = "<<PlaylistID>>"

def getSpotifyPlaylist(clientID, clientSecret, playlistId):
    query = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
     "grant_type":"client_credentials",
     "client_id":clientID,
     "client_secret": clientSecret
    }
    response = requests.post(query, headers=headers, data=data)
    token = response.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    query = f"https://api.spotify.com/v1/playlists/{playlistId}"
    response = requests.get(query, headers=headers)
    length = response.json()["tracks"]["total"]
    songs = []
    for i in range(700, length, 100):
        query = f"https://api.spotify.com/v1/playlists/{playlistId}/tracks?offset={i}"
        response = requests.get(query, headers=headers)
        for song in response.json()["items"]:
            songs.append(song["track"]["name"] + " - " + song["track"]["artists"][0]["name"])
    if len(songs) == length:
        print("All songs have been retrieved")
    else:
        print(f"{len(songs)} out of {length} songs have been retrieved")
    return songs
    
def writeYoutubePlaylist(songs):
    ytmusicapi.setup(filepath="browser.json")
    ytmusic = ytmusicapi.YTMusic("browser.json")
    # Change this if you want!
    playlist = ytmusic.create_playlist("Spotify imported songs", "An imported playlist from Spotify")
    counter = 0
    for song in songs:
        counter += 1
        if counter % 10 == 0:
            print(f"{counter} songs have been added")
        try:
            search_results = ytmusic.search(song)
            ytmusic.add_playlist_items(playlist, [search_results[0]["videoId"]])
        except:
            print(f"Somethings went wrong when adding '{song}'")


songs = getSpotifyPlaylist(spotifyID, spotifySecret, spotifyPlaylist)
writeYoutubePlaylist(songs)
