# Clustering

This folder includes essential techniques for clustering, an unsupervised machine learning method used to group similar data points. The document covers two primary clustering techniques: Hierarchical Clustering and K-Means Clustering.

1. Hierarchical Clustering (Agglomerative)
Hierarchical clustering builds a hierarchy of clusters without requiring a predefined number of clusters. The key steps include:

Loading Data: Import and read the dataset.
Data Preprocessing:
Drop unnecessary columns (e.g., 'State').
Normalize numerical values for better distance calculations.
Dendrogram Analysis:
Compute distance using linkage methods (e.g., complete linkage with Euclidean distance).
Generate a dendrogram to visualize the number of potential clusters.
Model Application:
Choose the optimal number of clusters based on the dendrogram.
Fit the Agglomerative Clustering model and assign cluster labels.
Cluster Analysis:
Compute mean values for each cluster to interpret patterns.

2. K-Means Clustering
K-Means clustering partitions data into K clusters, where each data point belongs to the cluster with the nearest mean.

Loading Data: Import and inspect the dataset.
Data Preprocessing:
Normalize numerical features using MinMaxScaler.
Scatter Plot:
Visualize the dataset (e.g., Age vs Income) to understand its structure.
Applying K-Means:
Define the number of clusters (k) and fit the model.
Assign cluster labels to data points.
Choosing Optimal K (Elbow Method):
Compute Total Within Sum of Squares (TWSS) for different values of k.
Plot the Elbow Curve to determine the best number of clusters.
Cluster Visualization:
Plot the clusters with distinct colors.
Mark centroids to identify cluster centers.

3. Understanding K-Means Behavior
Random Data Generation: Create a synthetic dataset to demonstrate how K-Means clustering works.
Model Implementation: Fit the K-Means model and visualize cluster assignments.
Cluster Analysis:
Compare average values within each cluster.
Save and export the clustered data for further insights.
