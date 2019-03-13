# Logistic Regression

- It's an classification algorithm.
- It's a binary classifier.
- It transforms its input using the sigmoid function (a.k.a the logistic function) to produce probability values as output. 
- These resulting probability values are used to sort instances into discrete classes based on some user-supplied threshold.
- for eg: what is the prob of email being spam? If the estimated prob is greater then 50%, then the model instance belongs to that class (called positive class, labelled as 1) or else it predicts that it does not (i.e.  it belongs to negative class, labelled 0). this makes it a binary classifier.

#### How does it work?
Just like linear regression, logisitic regression computes the weighted sum of input features (plus a bias term), but instead of outputing the result directly like linear regression model does, it outputs the logistic of the result.

The logistic - also called logit, is a sigmoid function (i.e. S-shaped) that outputs a number between 0 and 1.

#### How is it trained?
The objective of training is to set the parameter vector 0 so that model estimates high probabilities for positive instances (y=1) and low probablities for negative instances (y=0). 

#### Cost Function:
```
C(0) = -log(p_hat)   if y = 1
C(0) = -log(1-p_hat) if y = 0
```
This cost function makes sense because -log(p_hat) grows very large when (p_hat) approaches 0, so the cost will be larger if the model estimates a probability close to 0 for a positive instance, and it will also be very large if the model estimates a probability close to 1 for negative instance.

On the other hand, -log(p_hat) is close to 0 when t is close to 1, so the cost will be close to 0 if the estimated probability is close to 0 for a negative instance or close to 1 for a positive instances, which is precisely what we want.

The cost function over the whole trainning set is simply the average cost over all training instances -- also called as **log loss**.

- It's convex in nature, so Gradient descent (or any other optimization algorithm) is graunted to find the global minimum (if the learning rate is not too large and you wait long enough).

###### Hyperparameters:
- hyperparameter controlling the regularization strength of a logiditc regression is not alpha (as in other linear models), but its inverse: **C**
- higher the value of C, the less the model is regualrized.

#### What is an Activation Function?

An activation function checks if our output is above a certain decision threshold, if so, our model will classify the instance as true.

For example, if we set our decision threshold to be 0.5, then any instance with 0.5 or greater probability will be classified as true and any less than 0.5 as false.

#### How to evaluate performance of Logistic Regression

#### Assumptions of Logistic Regression
1. does not need a linear relationship between the dependent and independent variables.
   - can handle all sorts of relationships, because it applies a non-linear log transformation to the predicted odds ratio.
2. the independent variables do not need to be multivariate normal – although multivariate normality yields a more stable solution. Also the error terms (the residuals) do not need to be multivariate normally distributed.
4. Thirdly, homoscedasticity is not needed.
5. Lastly, it can handle ordinal and nominal data as independentvariables.

However some other assumptions still apply.
- Binary logistic regression requires the dependent variable to be binary and ordinal logistic regression requires the dependent variable to be ordinal.
- the error terms need to be independent.  Logistic regression requires each observation to be independent.
- logistic regression assumes linearity of independent variables and log odds. Whilst it does not require the dependent and independent variables to be related linearly, it requires that the independent variables are linearly related to the log odds. 


## Softmax Regression:
- logisitc regression is generalized to support multiple classes directly,  without having to train multiple binary classifiers -- and this is called *Softmax Regression, or Multinomial Logistic Regression*.
- It is multiclass and not multioutput.
- It predicts only one class at a time, so it should be used only with mutually exclusive classes such as different types of plants. You cannot use it to recognize multiple people in one picture.

**IDEA:** Idea behind Softmax Regression is quite simple:
  - When given an instance X, the softmax regression model first computes a score S(X) for each class k.
  - then estimates the probability of each class by applying the softmax function to the each score.
  - NOTE: each class has its own dedcidated parameter vector 0(k). All these vectors are stored as rows ina  parameter matrix.
  - Once you have computed scores for every class for given instance X, you can estimate the probability p_hat that the instance belongs to class k by runnning the scores through the softmax function.
  
  - *What softmax function does?* It computes the exponential of every score, then normalizes them by the sum of all exponentials.
  
  - Just like logisitc regression classifier, the softmax regression classifier predicts the class with the highest estimated probability - which is simply the class with the highest score.

## Cost/ Objective Function: Cross Entropy
- The objective is to have a model that estimates a high probability for the target class (and consequently a lower prob for other classes). 
- Minimizing the cost function, called Cross Entropy, should lead to this objective because it penalizes the model when it estimates a low probablitity for target class.
- Cross Entropy: is frequently used to measure how well a set of estimated class probabilities match the target class.

#### Sources
1. https://machinelearningmastery.com/logistic-regression-for-machine-learning/
2. http://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html
3. https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
4. https://stats.stackexchange.com/questions/278771/how-is-the-cost-function-from-logistic-regression-derivated
