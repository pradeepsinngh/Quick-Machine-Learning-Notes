## Expectation–Maximization Clustering using Gaussian Mixture Models

One of the major drawbacks of K-Means is its naive use of the mean value for the cluster center. What if you have multiple clusters having save mean? K-Means fails at such cases.

### Intuition:
- Gaussian Mixture Models (GMMs) give us more flexibility than K-Means. 
- With GMMs we assume that the data points are Gaussian distributed; this is a less restrictive assumption than saying they are circular by using the mean. That way, we have two parameters to describe the shape of the clusters: the mean and the standard deviation!
- In order to find the parameters of the Gaussian for each cluster (e.g the mean and standard deviation) we will use an optimization algorithm called Expectation–Maximization (EM).

![EM Clustering using GMMs](https://github.com/pradeepsinngh/Machine-Learning-Notes/blob/master/17%20Clustering/data/EM%20Clustering%20using%20GMMs.gif)

