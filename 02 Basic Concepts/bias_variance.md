# Bias-Variance Tradeoff

The bias-variance tradeoff in machine learning is a property of machine learning where models with high bias have low variance, and models with low bias have high variance.

#### What is Bias?

Bias is error that is a result of assumptions made by the machine learning algorithm.

High bias will cause the algorithm to [underfit]() the data.

High bias algorithms are usually less complex
* Linear Algorithms
* Parametric Algorithms

#### What is Variance?

Variance is error from noise in the training data.

High variance will cause the algorithm to [overfit]() the data.

High variance algorithms are usually more complex
* Non-linear Algorithms
* Non-parametric Algorithms

#### Why do we want to minimize both bias and variance?

`Total Error = bias^2 + variance + irreducible error`

The goal of machine learning is to create models with the least possible amount of error that also generalize well to unseen data. Minimizing bias means reducing the difference between our model's predictions and the actual output. Minimizing variance means reducing our model's sensitivity to noise and preventing it from "memorizing" the training data.

High bias makes for poor predictions because it cannot model complex data.

High variance makes for bad generalizations because it memorizes training data and consequently random noise instead of desired patterns in the data.

#### How do we actually achieve low bias and variance?

There is no possible way to have both low bias and low variance. Instead, we need to find a balance of bias and variance that minimizes total error.

#### How do I know if my model underfits or overfits?

* Dataset Split
* [Cross Validation]()
* Bootstrap

#### Sources
1. https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
2. https://elitedatascience.com/bias-variance-tradeoff
3. https://stats.stackexchange.com/questions/256141/mathematical-intuition-of-bias-variance-equation
4. https://stats.stackexchange.com/questions/81576/how-to-judge-if-a-supervised-machine-learning-model-is-overfitting-or-not
5. https://www.quora.com/How-do-we-detect-overfitting-and-under-fitting-in-Machine-Learning
