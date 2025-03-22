# Spotify-Playlist-To-Youtube-Music
**WIP**

Quick doc on how I moved my Spotify playlists to YouTube Music. I couldn't find an "easy" way of doing this, so I'm writing this to make it as straightforward as possible for anyone who needs this to get it done pretty painlessly. I've got it done now, so I'm not coming back to this if anything changes or if there's a better way of doing it. You've been warned! If it turns out this is misleading or significantly worse than another way I find, I'll private or delete this repo.

There are a couple things you need to do before you can run this:

# Spotify
The Spotify API docs are here: https://developer.spotify.com/documentation/web-api

To use the Spotify API, you will need to set up a Spotify app. This is free and quick to do. Go to https://developer.spotify.com/dashboard and click the create app button. Give it a name, description, and throw any URL into the Redirect URI field, then save. Then, from the dashboard, select it and go to its settings. We will need the client ID and secret. This is used to get an API key so we can query for the playlist content. 

The last thing we will need for this stage is the playlist ID. We can find this in https://open.spotify.com/playlist/>>2mtlhuFVOFMn6Ho3JmrLc2<<?... this part of the share link.

# YTMusic

We need authorisation to create and add to playlists, so there's something to do here too. 


