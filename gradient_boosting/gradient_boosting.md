# Gradient (Tree) Boosting

"*The idea is to use a weak learning method several times to get a sucession of hypotheses, each one refocused on the examples that the previous one found difficult and misclassified*"

The objective is to minimize the loss by adding weak learners using gradient descent like procedure. Note that one new weak learner is added during each iteration and that existing weak learners do not change. So what is this gradient descent like procedure?

#### Algorithm
1. Fit model to the data
2. Fit model to the residuals
3. Create new model
4. Repeat 1 - 3 as needed

###### Parameters
1. Loss Function
2. Weak Learner ([Decision Tree](https://github.com/jimmychimmyy/machine_learning_notes/blob/master/decision_tree/decision_tree.md))
3. Additive Model

###### Hyperparameters
1. Tree Constraints
2. Shrinkage
3. Random Sampling
4. Penalized Learning
5. Number of Iterations

Note that, your weak learner does not always necessarily have to be a decision tree, however, in practice it usually is.

#### Sources
1. https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
2. http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/
