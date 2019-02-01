## DBSCAN
### Density-Based Spatial Clustering of Applications with Noise

![DBSCAN](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/DBSCAN.gif)

- DBSCAN begins with an arbitrary starting data point that has not been visited. 
- The neighborhood of this point is extracted using a distance epsilon ε (All points which are within the ε distance are neighborhood points).
- If there are a sufficient number of points (according to minPoints) within this neighborhood then the clustering process starts and the current data point becomes the first point in the new cluster. 
- Otherwise, the point will be labeled as noise (later this noisy point might become the part of the cluster). In both cases that point is marked as “visited”.
- For this first point in the new cluster, the points within its ε distance neighborhood also become part of the same cluster. - This procedure of making all points in the ε neighborhood belong to the same cluster is then repeated for all of the new points that have been just added to the cluster group.
- This process is repeated until all points in the cluster are determined i.e all points within the ε neighborhood of the cluster have been visited and labelled.
- Once we’re done with the current cluster, a new unvisited point is retrieved and processed, leading to the discovery of a further cluster or noise. 
- This process repeats until all points are marked as visited. Since at the end of this all points have been visited, each point well have been marked as either belonging to a cluster or being noise.

### Advantages:
- It does not require a pe-set number of clusters at all. 
- It identifies outliers as noises unlike mean-shift which simply throws them into a cluster even if the data point is very different. 
- It is able to find arbitrarily sized and arbitrarily shaped clusters quite well.

### Disadvantages:
- It doesn’t perform as well as others when the clusters are of varying density. This is because the setting of the distance threshold ε and minPoints for identifying the neighborhood points will vary from cluster to cluster when the density varies.
- This drawback also occurs with very high-dimensional data since again the distance threshold ε becomes challenging to estimate.
