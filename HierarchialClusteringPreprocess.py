# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:29:04 2020

@author: Santosh Sah
"""
from sklearn.preprocessing import MinMaxScaler
from HierarchialClusteringUtils import (importHierarchialClusteringDataset, saveHierarchialClusteringDataset, saveHierarchialClusteringMinMaxScaler)

def preprocess():
    
    X = importHierarchialClusteringDataset("Hierarchial_Clustering_Mall_Customers.csv")
    
    hierarchialClusteringMinMaxScaler = MinMaxScaler()
    hierarchialClusteringMinMaxScaler.fit(X)
    saveHierarchialClusteringMinMaxScaler(hierarchialClusteringMinMaxScaler)
    
    X = hierarchialClusteringMinMaxScaler.transform(X)
    saveHierarchialClusteringDataset(X)
    

if __name__ == "__main__":
    preprocess()