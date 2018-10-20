# Random Forest (RF)

- is an ensemble of decision trees, trained via bagging or pasting.
- NOTE: RF algo. introduces extra randomness when growing trees; instead of search for the best feature when splitting node, it search for best feature among random subset of features.
- This result in greater tree diversity, which once again trades a higher bias for lower variance.

# Extra Trees:
When growing a tree in a Random Forest, at each node only a random subset of the feature is considered for splitting. It is possible to make trees even more random by also using random thresholds for each feature rather tahn search for best possible threshold.

A forest of such random trees is simply called *Extremely Randomized Trees* ensemble. Once again, this trades for more bias for a lower variance.

This makes training Extra-Trees much faster then regular Random forest since finding the best possible threshold for each feature at every node is one of the time-consumingt asks of growing a tree.

## Which works better: Random Forest or Extra-Trees ?
- It's hard to tell, which will work or worse better.
- Try both and compare them using cross-validation (and tuning the hyperparameters using grid search)

## Feature Importance:
- Yet another quality of RF is that they make it easy to measure the relative importance of each feature.
- In scikit-learn, we can measure feature importance by looking how much the tree node that use that feature reduces impurity on average (across all trees in the forest).
- More precisely, it is a weighted average, where each node's weight is equal to number of training samples that are associated with it.
