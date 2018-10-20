# Bagging and Pasting

- Use same training algorithm, but train it on different random subsets of the training set.
- When sampling is performed with replacement, this is called as bagging. (also called bootstrap aggregating)
- When sampling is performed without replacement, this is called as pasting.
- Both bagging and pasting allow training instances to be sampled several times across multiple predictors.
- But it is only bagging that allows training instances to be sampled several times for same predictor. 
- Bagging and Pasting scale really well

## How it make prediction?
- Once all predictors are trained, the ensemble can make a prediction for a new instance by simply aggregating the prediction of all predictiors. 
- The aggregation function for classification is typically the statitical mode (i.e. the most frequent predcition, just like hard voting classifier).
- The aggregation function for regression is typically the average.

**NOTE:** Each indiviual predictor predictor has a higher bias than if it were trained on the orgnal training set, but aggregation reduces both bias and variance.

### Out-of-Bag Evaluation:
- With bagging, some instances may be samples several times, and other might not sampled at all.
- Bagging sample m samples with remplacement, where m in the size of training set.
- this means that only about 63% of the training instances are sampled on average for each predictor. 
- The remaining 37% of the training instances that are not sampled are called out-of-bag (oob) instances. NOTE, this 37% is not same for all predictors.

**Cool Stuff:**
- Since, the predictor never see these Out-of-Bag instances during training, it can be evaluated on these instances, without the need for a separate validation set or cross-validation.

### Random Patched and Random Subspaces:
- You can sample sample features as well (in scikitlearn).
- This is controlled by 2 hyperparameters: `max_features` and `bootstrap_features`.
- This usefull, particulary when you are dealing with high-dimensional inputs (such as images).

- Sampling both training instances and features is called **Random Patches method**.
- Keeping all features and but sampling features is called **Random Subspace method**

- Sampling features results in even more predictor diversity, trading a bit more for bias for a lower variance.



