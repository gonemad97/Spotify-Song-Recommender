import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def unload():
    with open('spotify_dataset_new.pkl', 'rb') as f:
        data = pickle.load(f)
        data_reordered = data[['id',
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
        features = data_reordered.loc[:, 'energy':'speechiness']
        cols_to_standardize = features.columns.tolist()
        return data_reordered, data_reordered[cols_to_standardize]


def pca_kmeans():
    full_dataset, feature_data = unload()
    # normalization of the data
    std_audio = StandardScaler().fit_transform(feature_data)

    # PCA fitting with 11 components for 11 features
    pca = PCA(n_components=11)
    principalComponents = pca.fit_transform(std_audio)

    # save in a dataframe for further computation
    PCA_components = pd.DataFrame(principalComponents)

    # Kmeans with 3 clusters based on elbow method
    model = KMeans(n_clusters=5)
    model.fit(PCA_components.iloc[:, :2])

    # adding cluster and component columns to the dataset
    segm_kmeans = pd.concat([full_dataset.reset_index(drop=True)], axis=1)

    segm_kmeans["Segment KMeans PCA"] = model.labels_
    segm_kmeans["Segment"] = segm_kmeans["Segment KMeans PCA"]\
        .map({0: "Cluster 1", 1: "Cluster 2", 2: "Cluster 3", 3: "Cluster 4", 4: "Cluster 5"})

    return pca, model, segm_kmeans

