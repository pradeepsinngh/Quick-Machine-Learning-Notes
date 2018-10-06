## Locally Linear Embedding

It's an non-linear dimensionality reduction technique. It is a Manifold Learning technique that does not rely on projections. It owks by first measuirng how each training instance linearly relates to its closest neighbors and then looking for a low-dimesnional representation of the training set where these local relationship are best preserved.

- It's good for unrolling twisted manifolds, especially when there is not too much noise.

** Algorithm: **
- for each training instance x, identifiy it's k closet neighbour.
- then reconstruct x as a linear function of these neighbour.
- more spcefically find weights W such that the squared distance between x and x * w is as small as possible.
- now, map training instances into a d-dimensional space (d<n) while preserving the local relationship as much as possible.


## Some other dimensionality reduction techniques:
** t-Distributed Stochastic Neighbour Embedding (t-SNE)** 
reduces dimensionality while trying to keep similar instances close and disimilar instances apart. mostly used to visualize clusters of instances in high-dimensional soace.
** Linear Discrimant Analaysis ** 
1. is actually a classification algorithm, but during training it learns the most discriminative axes between the classes, and these axes can be used to define hyperplane onto which to project the data.
2. benifit of LDA is that the projection will keep classes as far as possible, so LDA is a good tech to reduce dimensionality before running another classification algorithm such as an SVM classifier.
- Isomap
- Multidimensional scaling.
