# Bagging and Pasting

- Use same training algorithm, but train it on different random subsets of the training set.
- When sampling is performed with replacement, this is called as bagging. (also called bootstrap aggregating)
- When sampling is performed without replacement, this is called as pasting.

- Both bagging and pasting allow training instances to be sampled several times across multiple predictors.
- But it is only bagging that allows training instances to be sampled several times for same predictor. 
- Once all predictors are trained, the ensemble can make a prediction for a new instance by simply aggregating the prediction of all predictiors. 
