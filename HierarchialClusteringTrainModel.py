# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:51:30 2020

@author: Santosh Sah
"""

from sklearn.cluster import AgglomerativeClustering
from HierarchialClusteringUtils import (saveHierarchialClusteringMeans, readHierarchialClusteringDataset)

"""
Train KMeanClustering model 
"""
def trainHierarchialClusteringModel():
    
    X = readHierarchialClusteringDataset()
    
    hierarchialClustering = AgglomerativeClustering(n_clusters = 5, affinity = "euclidean",  linkage ="ward")
    hierarchialClusteringMeans = hierarchialClustering.fit_predict(X)

    saveHierarchialClusteringMeans(hierarchialClusteringMeans)

if __name__ == "__main__":
    trainHierarchialClusteringModel()