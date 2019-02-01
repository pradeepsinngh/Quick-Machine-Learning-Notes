## Expectation–Maximization Clustering using Gaussian Mixture Models

One of the major drawbacks of K-Means is its naive use of the mean value for the cluster center. What if you have multiple clusters having save mean? K-Means fails at such cases.

### Intuition:
- Gaussian Mixture Models (GMMs) give us more flexibility than K-Means. 
- With GMMs we assume that the data points are Gaussian distributed; this is a less restrictive assumption than saying they are circular by using the mean. That way, we have two parameters to describe the shape of the clusters: the mean and the standard deviation!
- In order to find the parameters of the Gaussian for each cluster (e.g the mean and standard deviation) we will use an optimization algorithm called Expectation–Maximization (EM).

![EM Clustering using GMMs](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/EM%20Clustering%20using%20GMMs.gif)

- We begin by selecting the number of clusters (like K-Means does) and randomly initializing the Gaussian distribution parameters for each cluster.
- Given these Gaussian distributions for each cluster, compute the probability that each data point belongs to a particular cluster. (The closer a point is to the Gaussian’s center, the more likely it belongs to that cluster.)
- Based on these probabilities, we compute a new set of parameters for the Gaussian distributions such that we maximize the probabilities of data points within the clusters. (We compute these new parameters using a weighted sum of the data point positions, where the weights are the probabilities of the data point belonging in that particular cluster.)

To explain this in a visual manner we can take a look at the graphic above, in particular the yellow cluster as an example. The distribution starts off randomly on the first iteration, but we can see that most of the yellow points are to the right of that distribution. When we compute a sum weighted by the probabilities, even though there are some points near the center, most of them are on the right. Thus naturally the distribution’s mean is shifted closer to those set of points. We can also see that most of the points are “top-right to bottom-left”. Therefore the standard deviation changes to create an ellipse that is more fitted to these points, in order to maximize the sum weighted by the probabilities. We repeate these steps iteratively until convergence, where the distributions don’t change much from iteration to iteration.

### Advantages:
- GMMs are a lot more flexible in terms of cluster covariance than K-Means; Due to the standard deviation parameter, the clusters can take on any ellipse shape, rather than being restricted to circles. 
- K-Means is actually a special case of GMM in which each cluster’s covariance along all dimensions approaches 0. 
- GMMs use probabilities, they can have multiple clusters per data point. So if a data point is in the middle of two overlapping clusters, we can simply define its class by saying it belongs X-percent to class 1 and Y-percent to class 2. i.e GMMs support mixed membership.
