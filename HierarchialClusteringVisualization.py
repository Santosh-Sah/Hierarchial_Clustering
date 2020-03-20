# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:58:38 2020

@author: Santosh Sah
"""
import matplotlib.pyplot as plt
from HierarchialClusteringUtils import readHierarchialClusteringDataset, readHierarchialClusteringMeans

def hierarchialClusteringVisualizeCluster():
    
    X = readHierarchialClusteringDataset()
    hierarchialClusteringMeans = readHierarchialClusteringMeans()
    
    # Visualising the clusters
    plt.scatter(X[hierarchialClusteringMeans == 0, 0], X[hierarchialClusteringMeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
    plt.scatter(X[hierarchialClusteringMeans == 1, 0], X[hierarchialClusteringMeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
    plt.scatter(X[hierarchialClusteringMeans == 2, 0], X[hierarchialClusteringMeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
    plt.scatter(X[hierarchialClusteringMeans == 3, 0], X[hierarchialClusteringMeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X[hierarchialClusteringMeans == 4, 0], X[hierarchialClusteringMeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    
    plt.savefig("hierarchial_clustering_cluster.png")
    
    plt.show()

if __name__ == "__main__":
    hierarchialClusteringVisualizeCluster()