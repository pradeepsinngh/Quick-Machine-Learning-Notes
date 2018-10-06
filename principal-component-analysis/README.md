## Principal Component Analysis (PCA)

1. Step 1: Identify the hyperplan that lies closest to the data.
2. Step 2: Project the data onto it.

### Preserving the variance
Before you project the training set onto a lower-dimensional hyperplane, you first need to choose the right hyperplane. Choosing the plane that preserves the maximum amount of variance will most likely lose less information than the other projections. Another way to justify this is, choose the axis/ hyperlane that minimize the mean squared distance between the orignal dataset and its projection onto the axis.

### Principal Components
PCA indetifies the axis that account for largest amount of variance in the training set. It also finds, a second axis orthogonal to first one, that accounts for the largest amount of remaining variance. If there are d dimensiona, it can find d axes in the datasets. Mathematically, the unit vector that defines ith axis is called the ith principal component.


**NOTE:** The direction of principal component is not stable: if you perturb the trainng set slightly and run PCA again, some of the new PC may point in opposite direction of the orignal PC. However, they will generally lie on the same axes.

### Assumption
PCA assumes that dataset is centerted around the orignin.

### How to find PCs?
Using Singular Value Decomposition (SVD) that can decompose the training set matrix X into the dot product of three matrices U . Summation . V transpose, where V contain all the PCs.

### How to project training set to the hyperplane?
Compute the dot product b/w training set matrix **X** by the matrix **W**, which contain the first d principal components (i.e. matrix composed of the first d columns of **V**).

### How to choose dimensions?
Instead of arbitrarily choosing the number of dimensions to reduce down to, it is good to choose the no of dimensions that add up to a sufficiently large portion of the variance (e.g. 95%). but, for viz you mostly choose dimensions to be 2 or 3.

Another approach would be to, plot the explained variance as a function of the number of dimensions. There will usually be an elbow in the curve, where the explained variance stops growing fast.

### Explained Variance Ratio of each PC:
-- proprotion of the datasets variance that lies along the axis of each principal component.


