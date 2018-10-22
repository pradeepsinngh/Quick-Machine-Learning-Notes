# Decision Tree for Regression:
- DT are also capable of performing regression tasks.
- DT is very much similar to classification problem, the main difference is that instead of predicting a class in each node, it predicts a value.

#### Working Eg:
- For eg: suppose you want to make a prediciton for a new instance with x1 = 0.6. 
- You traverse the tree starting at the root, and you eventually reach the leaf node that predicts value = 0.1106.
- The predcition is simply the average target value of the 110 training instances associated to this leaf node.

NOTE:
- predicited value for each region is always the avergae target value of the instance in that region.
- the algo. splits each region in a way that makes most training instances as close as possible to that predicted value.
- CART algo. works mostly the same way as in classification case, except that instead of trying to split the training set in a way that minimizes impurity, it now tries to split the training set ina way that minimizes the MSE.

