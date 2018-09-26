# Cross-Validation
How well will my model perform on unseen data? (How well does my model generalize?)

If a model sees the entire dataset during training it will undoubtedly perform exceedingly well on the same dataset. This is why before learning a model, it is important to partition our dataset into training and testing data. Cross-validation takes this idea one step further.

Cross-Validation tells us how well the model will generalize on unseen data. The high level idea of cross-validation is to partition part of the training set into a validation set. The training set allows us to see how well our model has fitted our parameters. We then make predictions on the validation set which allows us to fine tune the hyperparameters.

###### Remember:
1. The model's parameters are fitted using the training set.
2. We evaluate the fitted model's predictions using the validation set (we tune hyperparameters here accordingly).
3. We evaluate the final fitted model's predictions using the test set.

#### Types of Cross-Validation
* Holdout Method
* K-Fold Cross Validation
* Stratified K-Fold Cross Validation
* Leave-P-Out Cross Validation

#### Holdout Method

Partition data into 3 subsets: training, validation (holdout), testing.

Train your model using the training set. Use the validation set to see how well the model performs on unseen data. Use testing set for final estimate of the model's performance.

Typically, you will split your training and testing data into 80% and 20% respectively. To obtain your holdout set, you split your training set further.

###### Pros:
* runs once

###### Cons:
* higher variance since training data size is reduced

#### K-Fold Cross Validation

The high-level idea of k-fold cross-validation is to partition the training data into **k** folds (subsets). We then train our model using **(k - 1)** folds of the data while saving the **kth** fold as a validation set to evaluate our model's performance. We repeat this process **k** times, using each fold of the training data as the validation set once. The error we get from the evaluation of the **kth** fold is an approximation of our model's generalization error. We sum and divide the error by **k** in order to get the average error.

###### Pros:
* has lower variance than holdout method
* good to use if you have limited data

###### Cons:
* model is trained k separate times

#### Stratified K-Fold Cross Validation

Similar to k-fold cross validation, the difference is that in stratified k-fold the folds are partitioned carefully to ensure that each fold contains an approximately equal number of class labels (target class). In other words, we want to keep the proportion of classes constant across all folds.

Basically, you can think of this as k-fold cross validation for classification problems.

#### Leave-One-Out Cross Validation

In leave-one-out (LOO-XVE), we use all the training data, save one instance, to train the model. Like k-folds, we repeat this process **M** times, where **M = total number of instances**. We sum the error and get an average.

#### When should I use Cross-Validation?

#### What is the ideal ratio of Training:Validation:Testing?



#### Sources
1. https://towardsdatascience.com/cross-validation-in-machine-learning-72924a69872f
2. https://www.quora.com/What-is-cross-validation-in-machine-learning
3. https://www.kdnuggets.com/2017/08/dataiku-predictive-model-holdout-cross-validation.html
4. https://www.datarobot.com/wiki/training-validation-holdout/
5. https://cimentadaj.github.io/blog/2017-09-06-holdout-and-crossvalidation/holdout-and-crossvalidation/
6. https://machinelearningmastery.com/k-fold-cross-validation/
