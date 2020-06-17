import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

class Auth(object):

    def spotify_auth(self,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,username):

        # client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
        # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
        token = util.prompt_for_user_token(username, scope,client_id=SPOTIPY_CLIENT_ID,
                                           client_secret=SPOTIPY_CLIENT_SECRET,
                                           redirect_uri=SPOTIPY_REDIRECT_URI)
        if token:
            sp = spotipy.Spotify(auth=token)
            #return sp
            print(sp)
        else:
            print("Can't get token for", username)

x = Auth()
print(x.spotify_auth('a14eee1e6e4e42d49ca37e9f33776d02','a3f8bc5b5e044aa2be61ef505b870319',
                     'http://localhost:8909/',"palsmadhu"))