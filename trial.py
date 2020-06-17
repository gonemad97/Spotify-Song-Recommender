import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

SPOTIPY_CLIENT_ID='a14eee1e6e4e42d49ca37e9f33776d02'
SPOTIPY_CLIENT_SECRET='a3f8bc5b5e044aa2be61ef505b870319'
SPOTIPY_REDIRECT_URI='http://localhost:8909/'
#
cid = "a14eee1e6e4e42d49ca37e9f33776d02"
secret = "a3f8bc5b5e044aa2be61ef505b870319"

#this can be automized for other user's username
username = "palsmadhu"
# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)
if token:
    sp = spotipy.Spotify(auth=token)
    print(sp)
else:
    print("Can't get token for", username)