import spotipy

import spotipy.util as util

class Auth(object):



    #this function must be changed to make it multi-user friendly later..maybe with Flask UI input?
    def creds(self):
        SPOTIPY_CLIENT_ID = "a14eee1e6e4e42d49ca37e9f33776d02"
        SPOTIPY_CLIENT_SECRET = "a3f8bc5b5e044aa2be61ef505b870319"
        SPOTIPY_REDIRECT_URI = "http://localhost:8909/"
        username = "palsmadhu"
        return [SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,username]


    def spotify_auth(self):

        # client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
        # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        cred_list = self.creds()
        scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
        token = util.prompt_for_user_token(cred_list[3], scope,client_id=cred_list[0],
                                           client_secret=cred_list[1],
                                           redirect_uri=cred_list[2])
        if token:
            sp = spotipy.Spotify(auth=token)
            return sp
            # print(sp)
        else:
            print("Can't get token for", cred_list[3])


    def store_tracks(self,tracks):
        global song_info
        # song_info = {}
        if 'song_info' not in globals():
            song_info = {}
            for item in tracks["items"]:
                #print(item["track"]["id"])
                track = item["track"]
                song_info[item["track"]["id"]] = {track["name"]:track["artists"][0]["name"]}
        #return song_info

    def discoverWeelySongs_testset(self):

        sp = self.spotify_auth()
        playlists = sp.current_user_playlists()
        for playlist in playlists['items']:
            #print(playlist['name'])
            if playlist['name'] == "Discover Weekly":
                results = sp.playlist(playlist['id'],
                                      fields="tracks")
                tracks = results['tracks']
                return self.store_tracks(tracks)






x = Auth()
#print(x.spotify_auth('a14eee1e6e4e42d49ca37e9f33776d02','a3f8bc5b5e044aa2be61ef505b870319','http://localhost:8909/',"palsmadhu"))
x.discoverWeelySongs_testset()
print(song_info)