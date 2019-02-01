## Expectation–Maximization Clustering using Gaussian Mixture Models

One of the major drawbacks of K-Means is its naive use of the mean value for the cluster center. We can see why this isn’t the best way of doing things by looking at the image below. On the left hand side it looks quite obvious to the human eye that there are two circular clusters with different radius’ centered at the same mean. K-Means can’t handle this because the mean values of the clusters are a very close together. 
K-Means also fails in cases where the clusters are not circular, again as a result of using the mean as cluster center.
