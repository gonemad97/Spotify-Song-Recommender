import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#unload the pickled dataset to create a model and perform analysis
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

#Performing PCA and KMeans CLustering on the dataset
def pca_kmeans():
    full_dataset, feature_data = unload()
    # normalization of the data
    #std_audio = StandardScaler().fit_transform(feature_data)

    # PCA fitting with 2 components for 11 features
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(feature_data)

    # save in a dataframe for further computation
    PCA_components = pd.DataFrame(principalComponents)

    # Kmeans with 3 clusters based on elbow method but we choose 20 to get more varied results
    model = KMeans(n_clusters=20)
    model.fit(PCA_components)

    # adding cluster and component columns to the dataset
    segm_kmeans = pd.concat([full_dataset.reset_index(drop=True)], axis=1)

    segm_kmeans["Segment KMeans PCA"] = model.labels_

    segm_kmeans["Segment"] = segm_kmeans["Segment KMeans PCA"]\
        .map({0:"Cluster 1",1:"Cluster 2",2:"Cluster 3",3:"Cluster 4",4:"Cluster 5",5:"Cluster 6",
              6:"Cluster 7",7:"Cluster 8",8: "Cluster 9",9: "Cluster 10", 10: "Cluster 11",
              11: "Cluster 12",12: "Cluster 13", 13: "Cluster 14", 14: "Cluster 15",15:"Cluster 16",
              16:"Cluster 17",17:"Cluster 18",18:"Cluster 19",19:"Cluster 20"})


    return pca, model, segm_kmeans

