import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid = ""
secret = ""

os.environ['SPOTIPY_CLIENT_ID']= cid
os.environ['SPOTIPY_CLIENT_SECRET']= secret
os.environ['SPOTIPY_REDIRECT_URI']='http://localhost:8888/callback'

username = "thepother"
Yclient_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=10,offset=0,time_range='short_term')
    for song in range(10):
        list = []
        list.append(results)
        with open('top10_data.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
else:
    print("Can't get token for", username)