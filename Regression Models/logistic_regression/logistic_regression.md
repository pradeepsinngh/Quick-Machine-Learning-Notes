# Logistic Regression

- It's an classification algorithm. 
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

#### Algorithm:


###### Parameters:

###### Hyperparameters:

#### What is an Activation Function?

An activation function checks if our output is above a certain decision threshold, if so, our model will classify the instance as true.

For example, if we set our decision threshold to be 0.5, then any instance with 0.5 or greater probability will be classified as true and any less than 0.5 as false.

#### Cost Function

#### How to evaluate performance of Logistic Regression

#### Assumptions of Logistic Regression

#### Things to watch out for

#### Tips and Tricks

#### Sources
1. https://machinelearningmastery.com/logistic-regression-for-machine-learning/
2. http://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html
3. https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0
4. https://stats.stackexchange.com/questions/278771/how-is-the-cost-function-from-logistic-regression-derivated
