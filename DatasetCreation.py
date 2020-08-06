import spotipy
import spotipy.util as util
from itertools import islice
import math
import pandas as pd

'''Spotify account credentials initialized here. Preset values have already been loaded into the 
Dockerfile so application will work if run through Docker Container. You can also authenticate the 
application with your own Spotify account as well by signing into the Developers portal.'''

def creds():
    SPOTIPY_CLIENT_ID = "<Your Client ID>"
    SPOTIPY_CLIENT_SECRET = "<Your Client Secret>"
    SPOTIPY_REDIRECT_URI = "<Your Redirect URI>"
    username = "<Your Username>"
    return [SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, username]

#Account authentication
def spotify_auth():
    cred_list = creds()
    scope = 'user-library-read playlist-read-private playlist-modify-public playlist-modify-private'
    token = util.prompt_for_user_token(cred_list[3], scope, client_id=cred_list[0],
                                       client_secret=cred_list[1],
                                       redirect_uri=cred_list[2])
    if token:
        sp = spotipy.Spotify(auth=token)
        return sp
        # print(sp)
    else:
        print("Can't get token for", cred_list[3])

#Retrieve playlist ids
def get_playlist_id():
    playlists = playlist_creation_from_category()
    playlist_ids = []
    for playlist in playlists:
        playlist_ids.append(playlist[17:])
    return playlist_ids

#Create list of all track ids
def show_tracks(results, uriArray):
    for i, item in enumerate(results["items"]):
        if item["track"]:
            track = item["track"]
            uriArray.append(track["id"])

#Uses show_tracks() to retieve all track ids from all playlists considered
def get_playlist_track_id(playlist_id):
    sp = spotify_auth()
    trackId = []
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    show_tracks(tracks, trackId)
    while tracks["next"]:
        tracks = sp.next(tracks)
        show_tracks(tracks, trackId)
    return set(trackId)

#Using the track ids, retrieve all the tracks from the playlists.
def get_playlist_tracks():
    playlist_ids = get_playlist_id()
    all_tracks = []
    for id in playlist_ids:
        sp = spotify_auth()
        print("...")
        results = sp.playlist_tracks(id)
        tracks = results['items']

        # Loops to ensure I get every track of the playlist
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        all_tracks.extend(tracks)
    return set(all_tracks)


def get_all_track_ids():
    track_ids = []
    all_playlist_ids = get_playlist_id()
    for playlist_id in all_playlist_ids:
        track_ids += get_playlist_track_id(playlist_id)
    return track_ids


def split_calc(tracks, noOfTracks):
    if noOfTracks % 100 != 0:
        last = noOfTracks % 100
        split_list = [100] * (math.floor(noOfTracks / 100))
        split_list.append(last)
    else:
        split_list = [100] * (noOfTracks / 100)

    Input = iter(tracks)
    Output = [list(islice(Input, elem))
              for elem in split_list]

    return Output

#get all audio features of the tracks
def get_audio_features():
    tracks = get_all_track_ids()
    tracks_split = split_calc(tracks, len(tracks))

    audio_features = []
    for track_set in tracks_split:
        sp = spotify_auth()
        results = sp.audio_features(track_set)
        audio_features.append(results)

    audio_features_sets = []

    for feature_set in audio_features:
        for track in feature_set:
            if type(track) == dict:
                res = {key: track[key] for key in track.keys() & {'danceability', 'energy', 'key',
                                                                  'loudness', 'mode', 'speechiness',
                                                                  'acousticness',
                                                                  'instrumentalness', 'liveness',
                                                                  'valence',
                                                                  'tempo', 'id'}}
                audio_features_sets.append(res)

    return audio_features_sets


# final information holding track info and audio features for creating dataset
def get_track_details():
    track_details = []
    audio_feature_sets = get_audio_features()
    for i in audio_feature_sets:
        sp = spotify_auth()
        track = sp.track(i["id"])
        i["name"] = track["name"]
        i["artist"] = track["album"]["artists"][0]["name"]
        track_details.append(i)
    return track_details

#set of all categories in Spotify Browse section to create a set of playlists
def playlist_creation_from_category():
    browse_categories = ["hiphop","summer","pop","country","workout","latin","mood","rock","rnb",
                         "blackhistorymonth","edm_dance","rnb","gaming","focus","chill","at_home",
                         "indie_alt","inspirational","decades","alternative","wellness","pride","party",
                         "sleep","classical","jazz","roots","soul","dinner","romance","kpop","punk",
                         "regionalmexican","sessions","popculture","arab","desi","anime","afro",
                         "metal","reggae","blues","funk","student","family","travel"]
    playlists = set()
    for category in browse_categories:
        sp = spotify_auth()
        category_playlists = sp.category_playlists(category,limit=50)
        for playlist in range(len(category_playlists["playlists"]["items"])):
            playlists.add("spotify:playlist:"+category_playlists["playlists"]["items"][playlist]["id"])

    #around 1462 playlists
    return list(playlists)

# dataset creation
def create_dataset():
    track_records = get_track_details()
    return pd.DataFrame(track_records).to_pickle("./spotify_dataset_new.pkl")

#create_dataset()