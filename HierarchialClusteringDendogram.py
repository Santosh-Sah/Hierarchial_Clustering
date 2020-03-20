# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:47:24 2020

@author: Santosh Sah
"""
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from HierarchialClusteringUtils import readHierarchialClusteringDataset

def hierarchialClusteringDendogram():
    
    X = readHierarchialClusteringDataset()
    
    sch.dendrogram(sch.linkage(X, method = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    
    plt.savefig("hierarchial_clustering_dendogram.png")
    
    plt.show()


if __name__ == "__main__":
    hierarchialClusteringDendogram()
