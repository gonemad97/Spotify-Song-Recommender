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


    playlists = ["spotify:playlist:37i9dQZF1DX2RxBh64BHjQ","spotify:playlist:5PKZSKuHP4d27SXO5fB9Wl",
                 "spotify:playlist:5Xtj5QwZG7WzDY1C5wozcL","spotify:playlist:37i9dQZF1DWWqNV5cS50j6",
                 "spotify:playlist:37i9dQZF1DX4JAvHpjipBk","spotify:playlist:6fO3gSb2WXw6hgqY7nDe2C",
                 "spotify:playlist:37i9dQZF1DXcWxeqLvgOCi","spotify:playlist:65xSncKQzG6Suseh5gfYP1",
                 "spotify:playlist:37i9dQZF1DXc8kgYqQLMfH","spotify:playlist:37i9dQZF1DWWjGdmeTyeJ6",
                 "spotify:playlist:37i9dQZF1DX6mMeq1VVekF","spotify:playlist:37i9dQZF1DXcxvFzl58uP7",
                 "spotify:playlist:37i9dQZF1DX1YPTAhwehsC","spotify:playlist:37i9dQZF1DX0XUsuxWHRQd",
                 "spotify:playlist:37i9dQZF1DWVV27DiNWxkR","spotify:playlist:37i9dQZF1DWT6MhXz0jw61",
                 "spotify:playlist:37i9dQZF1DWVA1Gq4XHa6U","spotify:playlist:37i9dQZF1DWWBHeXOYZf74",
                 "spotify:playlist:37i9dQZF1DWVzZlRWgqAGH","spotify:playlist:37i9dQZF1DXcBWIGoYBM5M",
                 "spotify:playlist:37i9dQZF1DWUa8ZRTfalHk","spotify:playlist:37i9dQZF1DX5gQonLbZD9s",
                 "spotify:playlist:37i9dQZF1DXbYM3nMM0oPk","spotify:playlist:37i9dQZF1DWWvvyNmW9V9a",
                 "spotify:playlist:37i9dQZF1DWTwnEm1IYyoj","spotify:playlist:37i9dQZF1DX1lVhptIYRda",
                 "spotify:playlist:37i9dQZF1DXbIbVYph0Zr5","spotify:playlist:37i9dQZF1DX0bUGQdz5BJG",
                 "spotify:playlist:37i9dQZF1DWTkxQvqMy4WW","spotify:playlist:37i9dQZF1DWYnwbYQ5HnZU",
                 "spotify:playlist:37i9dQZF1DXdxUH6sNtcDe","spotify:playlist:37i9dQZF1DX1gRalH1mWrP",
                 "spotify:playlist:37i9dQZF1DXaTitkvoNNxt","spotify:playlist:37i9dQZF1DX83I5je4W4rP",
                 "spotify:playlist:37i9dQZF1DX0SM0LYsmbMT","spotify:playlist:37i9dQZF1DX3LyU0mhfqgP",
                 "spotify:playlist:37i9dQZF1DX59HcpGmPXYR","spotify:playlist:37i9dQZF1DXcCnXtB0Pp0D",
                 "spotify:playlist:37i9dQZF1DX76Wlfdnj7AP","spotify:playlist:37i9dQZF1DX4UtSsGT1Sbe",
                 "spotify:playlist:37i9dQZF1DX4o1oenSJRJd","spotify:playlist:37i9dQZF1DWTJ7xPn4vNaz",
                 "spotify:playlist:37i9dQZF1DX1rVvRgjX59F","spotify:playlist:37i9dQZF1DX5Ejj0EkURtP",
                 "spotify:playlist:37i9dQZF1DXbTxeAdrVG2l","spotify:playlist:37i9dQZF1DX3rxVfibe1L0",
                 "spotify:playlist:37i9dQZF1DX4fpCWaHOned","spotify:playlist:37i9dQZF1DX7KNKjOK0o75",
                 "spotify:playlist:37i9dQZF1DWSqmBTGDYngZ","spotify:playlist:37i9dQZF1DX7gIoKXt0gmx",
                 "spotify:playlist:37i9dQZF1DX2UgsUIg75Vg","spotify:playlist:37i9dQZF1DX10zKzsJ2jva",
                 "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6","spotify:playlist:37i9dQZF1DWWQRwui0ExPn"]
    def get_playlist_id(self,playlists):
        playlists = []






x = Auth()
#print(x.spotify_auth('a14eee1e6e4e42d49ca37e9f33776d02','a3f8bc5b5e044aa2be61ef505b870319','http://localhost:8909/',"palsmadhu"))
x.discoverWeelySongs_testset()
print(song_info)