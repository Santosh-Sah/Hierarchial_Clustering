# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:55:55 2020

@author: Santosh Sah
"""

import pandas as pd
import pickle

"""
Import dataset and read specific column.
"""
def importHierarchialClusteringDataset(hierarchialClusteringDatasetFileName):
    
    hierarchialClusteringDataset = pd.read_csv(hierarchialClusteringDatasetFileName)
    X = hierarchialClusteringDataset.iloc[:, [2, 3]].values
    
    return X

def saveHierarchialClusteringDataset(X):
    
    #Write X in a picke file
    with open("X.pkl",'wb') as X_Pickle:
        pickle.dump(X, X_Pickle, protocol = 2)

"""
read X from pickle file
"""
def readHierarchialClusteringDataset():
    
    #load X
    with open("X.pkl","rb") as X_pickle:
        X = pickle.load(X_pickle)
    
    return X

"""
Save HierarchialClusteringMeans as a pickle file.
"""
def saveHierarchialClusteringMeans(hierarchialClusteringMeans):
    
    #Write HierarchialClusteringMean as a picke file
    with open("HierarchialClusteringMeans.pkl",'wb') as HierarchialClusteringMeans_Pickle:
        pickle.dump(hierarchialClusteringMeans, HierarchialClusteringMeans_Pickle, protocol = 2)

"""
read HierarchialClusteringMeans from pickle file
"""
def readHierarchialClusteringMeans():
    
    #load HierarchialClusteringMeans model
    with open("HierarchialClusteringMeans.pkl","rb") as HierarchialClusteringMeans:
        hierarchialClusteringMeans = pickle.load(HierarchialClusteringMeans)
    
    return hierarchialClusteringMeans

"""
Save HierarchialClustering as a pickle file.
"""
def saveHierarchialClustering(hierarchialClustering):
    
    #Write HierarchialClustering as a picke file
    with open("HierarchialClustering.pkl",'wb') as HierarchialClustering_Pickle:
        pickle.dump(hierarchialClustering, HierarchialClustering_Pickle, protocol = 2)

"""
read HierarchialClustering from pickle file
"""
def readHierarchialClustering():
    
    #load HierarchialClustering model
    with open("HierarchialClustering.pkl","rb") as HierarchialClustering:
        hierarchialClustering = pickle.load(HierarchialClustering)
    
    return hierarchialClustering

"""
Save HierarchialClusteringMinMaxScaler as a pickle file.
"""
def saveHierarchialClusteringMinMaxScaler(hierarchialClusteringMinMaxScaler):
    
    #Write HierarchialClusteringMinMaxScaler as a picke file
    with open("HierarchialClusteringMinMaxScaler.pkl",'wb') as HierarchialClusteringMinMaxScaler_Pickle:
        pickle.dump(hierarchialClusteringMinMaxScaler, HierarchialClusteringMinMaxScaler_Pickle, protocol = 2)

"""
read HierarchialClusteringMinMaxScaler from pickle file
"""
def readHierarchialClusteringMinMaxScaler():
    
    #load HierarchialClusteringMinMaxScaler model
    with open("HierarchialClusteringMinMaxScaler.pkl","rb") as HierarchialClusteringMinMaxScaler:
        hierarchialClusteringMinMaxScaler = pickle.load(HierarchialClusteringMinMaxScaler)
    
    return hierarchialClusteringMinMaxScaler
