# Spotify-Playlist-To-Youtube-Music

Quick doc on how I moved my Spotify playlists to YouTube Music. I couldn't find an "easy" way of doing this, so I'm writing this to make it as straightforward as possible for anyone following in my footsteps. I've got it done now, so I'm not coming back to this if anything changes or if there's a better way of doing it. You've been warned! If it turns out this is misleading or significantly worse than another way I find, I'll private or delete this repo.

There are a couple things you need to do before you can run this:

# Spotify
The Spotify API docs are here: https://developer.spotify.com/documentation/web-api

To use the Spotify API, you will need to set up a Spotify app. This is free and quick to do. Go to https://developer.spotify.com/dashboard and click the create app button. Give it a name, description, and throw any URL into the Redirect URI field, then save. Then, from the dashboard, select it and go to its settings. We will need the client ID and secret. This is used to get an API key so we can query for the playlist content. 

The last thing we will need for this stage is the playlist ID. We can find this in https://open.spotify.com/playlist/>>2mtlhuFVOFMn6Ho3JmrLc2<<?... this part of the share link.

# YTMusic

I use an unofficial YTMusic API here: https://github.com/sigma67/ytmusicapi

If you use inspect on YTMusic and find a POST request in the 'network' tab to music.youtube.com, right click it and select 'copy request headers'. You will need this when you run the tool.

# Running the tool
Make sure you have run `pip install ytmusicapi`

I haven't bothered making this too nice to use. 

1. You can set the name and description of the new playlist in the script, defaulting to 'Spotify imported songs'.
2. Copy in Soptify info at the top of the script and run the tool. 
3. If all goes well, paste your request headers when prompted, then new line and ctl+d.

Should the tool fail, and you see repeated failures, I recommend trying the tool again with a new cookie and creating a new playlist, then merging these playlists in YouTube Music. You can change the offset of the Spotify playlist that is fetched in the Spotify section of the tool.

# Notes

1. This tool has only been tested in English.

2. The YouTube API will create a browser.json file that I recommend you delete after you are done.

3. YT music playlists have a limit of 5000 songs in a playlist. If you want to copy over more songs, you will need to make multiple playlists. This should be easy to do by modifying the script. 

4. You can use OAuth for YT, which might be more reliable, but you will have to change the authentication method.
