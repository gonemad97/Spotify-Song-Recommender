import DatasetCreation as dc
import Model as m
import pandas as pd


# search for a track and get all its audio features to compare with clusters
def search_for_track(query):
    sp = dc.spotify_auth()
    result = sp.search(query)

    try:
        track_id = result["tracks"]["items"][0]["id"]


        audio_features = sp.audio_features(tracks=[track_id])
        res = {key: audio_features[0][key] for key in
               audio_features[0].keys() & {'danceability', 'energy', 'key',
                                           'loudness', 'mode', 'speechiness',
                                           'acousticness',
                                           'instrumentalness', 'liveness',
                                           'valence',
                                           'tempo', 'id'}}

        track = sp.track(res["id"])
        res["name"] = track["name"]
        res["artist"] = track["album"]["artists"][0]["name"]
        # print(res)
        new_track = []
        new_track.append(res)
        new_searched_song = pd.DataFrame(new_track)
        pd.DataFrame(new_searched_song).to_pickle("./new_searched_track1.pkl")

        # to reorder features correctly
        searched_track = new_searched_song[['id',
                                            'name',
                                            'artist',
                                            'energy',
                                            'danceability',
                                            'acousticness',
                                            'instrumentalness',
                                            'mode',
                                            'liveness',
                                            'key',
                                            'tempo',
                                            'valence',
                                            'loudness',
                                            'speechiness']]

        # to get only required features
        features = searched_track.loc[:, 'energy':'speechiness']
        cols_to_standardize = features.columns.tolist()

        # return searched_track[cols_to_standardize]
        return searched_track[cols_to_standardize]
    except:
        return None

#finds the cluster of the searched track and returns set of 30 songs similar to it
def find_new_track_cluster_songs(query):
    try:
        pca, model, clustered_songs = m.pca_kmeans()
        searched_track = search_for_track(query)
        #std_audio = StandardScaler().fit_transform(searched_track)  # normalizing the data

        # predicting cluster for new track
        principalComponents = pca.transform(searched_track)
        PCA_components = pd.DataFrame(principalComponents)

        # cluster number of the searched song
        track_cluster = model.predict(PCA_components)

        # 10 songs in same cluster
        cluster_songs = clustered_songs[clustered_songs["Segment KMeans PCA"] == track_cluster[0]]
        related_songs = cluster_songs.sample(n=30)
        return related_songs
    except:
        return None


def display_songs(query):
    try:
        song_list = find_new_track_cluster_songs(query).iloc[:, : 3]
        return song_list

    #if song doesn't exist
    except:
        return pd.DataFrame()



#search_for_track("artist:Selena Gomez track:Look At Her Now")