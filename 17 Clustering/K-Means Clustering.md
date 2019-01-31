## K-Means Clustering

![K-Means](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/k-means.gif)

- To begin, we first select a number of classes/groups to use and randomly initialize their respective center points. 
- The center points are vectors of the same length as each data point vector.
- Each data point is classified by computing the distance between that point and each group center, and then classifying the point to be in the group whose center is closest to it.
- Based on these classified points, we recompute the group center by taking the mean of all the vectors in the group.
- Repeat these steps for a set number of iterations or until the group centers don’t change much between iterations.

#### Advantage:
- K-Means is pretty fast, as all we’re really doing is computing the distances between points and group centers; very few computations! It thus has a linear complexity O(n).

#### Disadvantage:
- You have to select how many groups/classes there are. 
- K-means also starts with a random choice of cluster centers and therefore it may yield different clustering results on different runs of the algorithm. Thus, the results may not be repeatable and lack consistency. Other cluster methods are more consistent.
