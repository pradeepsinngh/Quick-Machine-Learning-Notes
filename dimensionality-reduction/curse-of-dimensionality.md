## The Curse of Dimensionality:

We are so used to living in 3 dimensional space that our intuition fails us when ever we try to imagine a high-dimensional space. Even a 4D hypercube is incredibly hard to picture in our mind, let alone 200-dimensional ellipsoid bent in a 1000 dimensional space.

**NOTE:** 
It turns out many things behave very different in high-dimensional space. For eg: if you pick a randome point in a unite sq (1X1), it will have only about 0.4% chance of being located less than 0.001 from border. In other words, it is very unlikely that a random point will be extreme along any dimension. But, in a 10,000 dimensional unit hypercube (1 X 1 X 1 X....X 1) this probablity is greater than 99.99999%, Most points in high dimensional hypercube are very close of border.

Here is another eg: if you pick two points randomly in a unit sq, the distance between these two points will be, on average, roughly 0.52. If you pick two random point in a unite 3D cube, the avergae distance will be roughly 0.66. 

But what about two points picked randomly in a 1,000,000 dimensional hypercube? Well, the avergae distance will eb about 508.52. This is counterintutive: how can two points be so far when they lie in same unit space.

## Conclusion:
1. high dimensional datasets are at risk of being very sparse.
2. most training instances are likely to be far away from each other.
3. this alos makes new instances will likely be far away from training instances, making predictions much less reliable than lower dimensional space.
4. In short, more dimensions the training set has, the greater the risk of over fitting it.

In theory, one solution to curse of dimensionality could be to increase the size of the training set to reach a sufficient density of training instances. Unfortunately, in pratice, the number of training instances required to reach a given density grows exponentially with the number of dimensions. With just 100 feature, you would need more training instances than atoms in observed universe in order for training instances to be within 0.1 of each other on average, assuming they were spread out uniformly across all dimesnions.
