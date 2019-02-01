## Agglomerative Hierarchical Clustering:

- Hierarchical clustering algorithms actually fall into 2 categories: top-down or bottom-up. 
- Bottom-up algorithms treat each data point as a single cluster at the outset and then successively merge (or agglomerate) pairs of clusters until all clusters have been merged into a single cluster that contains all data points. Bottom-up hierarchical clustering is therefore called hierarchical agglomerative clustering or HAC. 
- This hierarchy of clusters is represented as a tree (or dendrogram). The root of the tree is the unique cluster that gathers all the samples, the leaves being the clusters with only one sample.

![Agglomerative Hierarchical Clustering](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/hierarchical-clustering.gif)

- We begin by treating each data point as a single cluster(if there are X data points in our dataset then we have X clusters). - We then select a distance metric that measures the distance between two clusters.(eg: average linkage -- distance between two clusters to be the average distance between data points in the first cluster and data points in the second cluster).
- On each iteration we combine two clusters into one. The two clusters to be combined are selected as those with the smallest average linkage. i.e. according to our selected distance metric, these two clusters have the smallest distance between each other and therefore are the most similar and should be combined.
- Keep repeating until we reach the root of the tree i.e we only have one cluster which contains all data points. 
- In this way we can select how many clusters we want in the end, simply by choosing when to stop combining the clusters i.e when we stop building the tree!

### Advantages:
- does not require us to specify the number of clusters and we can even select which number of clusters looks best since we are building a tree. 
- The algorithm is not sensitive to the choice of distance metric; all of them tend to work equally well whereas with other clustering algorithms, the choice of distance metric is critical. 
- A particularly good use case of hierarchical clustering methods is when the underlying data has a hierarchical structure and you want to recover the hierarchy; other clustering algorithms can’t do this. 

### Disdvantages:
- lower efficiency, as it has a time complexity of O(n³), unlike the linear complexity of K-Means and GMM.
