# Linear Regression

#### Hello, Linear Regression
Linear regression is one of the best starting points to learn machine learning. It is a supervised regression algorithm, meaning it learns some mapping from a set of input variables to some continuous output variable. Linear regression learns this mapping by fitting coefficients in a linear equation that reduces error in estimating some desired output.

Below are links to see linear regression in action

* [from scratch](https://github.com/jimmychimmyy/machine_learning_notes/blob/master/linear_regression/linear_regression.ipynb)
* [using sklearn]()

#### How does it work?

**Think:** `h(x) ≈ y = (b) + (ϴ)(x)`

* `h(x) = predicted output (dependent variable)`
* `y = output (dependent variable)`
* `x = input (independent variable)`
* `b = bias`
* `ϴ = weight`

The input and output, x and y, are given by our training data. The data is typically fed into our model in the form of a 2D matrix where each column corresponds to a different variable and each row is an instance (or example).

To learn our data, we need to find the values of b and ϴ. Once we know the values of b and ϴ, we plug them into h(x) to predict y for a new x. In other words, our model learns our bias and weight and is then able to make new predictions.

#### Algorithm:
1. Initialize b and ϴ to 0
2. Perform gradient descent to update b and ϴ
3. Repeat step 2 for some number of iterations

###### Parameters:
* X - vector where each element is an instance
* Y - vector where each element is an instance

*It might be easier to think of X and Y as column vectors where m = the number of instances (total number of rows), n = number of features (total number of columns). Also note that X and Y must have the same number of rows.*

###### Hyperparameters:
* learning rate
* epochs (number of iterations)

While the algorithm is straightforward, there is a lot going on during step 2: gradient descent.

Before performing gradient descent, it is helpful to visualize the error we are trying to minimize. To calculate error, we first find squared error for each instance: we plug b and 0 into h(x), find the difference between h(x) and y, then square the difference. We repeat this m times (once for every instance), keeping the sum of each difference, then take the mean of the total squared error which gives us MSE.

Now, actually performing gradient descent, we start by taking the partial derivative of our cost function with respect to each dependent variable. Which in the case of simple linear regression are b (bias) and ϴ (weight). We use these two new equations to find the mean gradient (which is the slope of our cost function) by plugging in each instance, summing, then averaging. The resulting gradients tell us how much to change b and ϴ by, respectively.

Before we update b and ϴ, we need to multiply both our gradients by some learning rate so that we control how fast we change b and ϴ. This is important because if we take large steps in updating b and ϴ, we may overshoot the minimum which would result in an increased MSE.

Once we've applied our learning rate to both gradients, we simply subtract these values from b and ϴ, respectively. We repeat this process some number of times until we are satisfied that we cannot reduce our MSE.

...

###### need to add math to show how it works

For a more detailed explanation of gradient descent click [here](https://github.com/jimmychimmyy/machine_learning_notes/blob/master/gradient_descent/gradient_descent.md).

#### What if we have more than 1 variable?

Remember that, by definition, simple linear regression has a single independent variable and a single dependent variable. As your data becomes more complex, you have more independent variables (features), you will need to use multivariable linear regression.

**Think:** `h(x) ≈ y = (b) + (ϴ1)(x1) + (ϴ2)(x2) + ... + (ϴn)(xn)`

* `h(x) = predicted output (dependent variable)`
* `y = output (dependent variable)`
* `b = bias`
* `(ϴ1, ..., ϴn) = weights from 1 to n (where n is the total number of features)`
* `(x1, ..., xn) = features (a.k.a input or independent variables)`

*On a side note, I have found it helpful to consistently use theta to represent the weights when I do machine learning*

#### Algorithm:
1. Initialize b and (ϴ1, ..., ϴn) to 0
2. Perform gradient descent to update b and all (ϴ1, ..., ϴn) simultaneously
3. Repeat step 2 for some number of iterations (You decide number of iterations)

##### Parameters:
* X - 2D matrix where each row (m) is an instance, each column (n) is a feature
* Y - vector where each element is an instance

*For multivariable linear regression, X usually takes the form of a matrix where the number of rows m is the number of instances and the number of columns n is the number of features or variables. Y is still a vector where each element corresponds to an instance. You should think of each row of X corresponding to an element in Y.*

##### Hyperparameters:
* learning rate
* epochs (number of iterations)

*Note that m = the number of instances (number of rows), n = number of features (number of columns)*

Multivariable linear regression is

#### Cost Function

There are many choices of cost functions for linear regression, I will be going over one of the most popular cost functions: **Mean Squared Error (MSE)**.

What exactly is MSE? Imagine we have an arbitrary set of points [1, 2, 3, 4, 5, 6, 7]. The mean of this set is 4. Error tells us how far away from the mean each of the points in the set are. For example, there is a difference of 3 between 1 (the first element) and the mean. MSE is simply the square of the difference, which for the case of 1 is 9 (since 3^2 = 9). Basically, the farther the points lie from the mean, the larger our MSE will be. The goal of linear regression is to find a best fit line with the smallest possible MSE.

What is the point of squaring the error? We square the error for two reasons:
1. to ensure that the difference is always positive
2. to emphasize larger differences (similar reasoning behind log scale)

###### TODO: add image

#### Gradient Descent

###### TODO: add math behind gradient descent


#### How to evaluate performance of Linear Regression

#### Assumptions of Linear Regression

Linear Regression makes five key assumptions about your data:
1. Linear relationship
2. Multivariate normality (are your variables distributed normally?)
3. Little to no multicollinearity (multicollinearity occurs when the independent variables are too highly correlated with each other)
4. No Auto-Correlation
5. Homoscedasticity

#### When should I use linear regression?

When you are faced with a regression problem, needing to map some variables to some continuous feature, I highly recommend starting with linear regression to establish some sort of base line of performance. It is a simple algorithm to implement and is widely available in open source libraries.

#### Things to watch out for

#### Tips and Tricks

* Linear Regression works best when your input features share a similar scale so it is in your best interest to do some feature scaling and normalization before using linear regression.
* If you are going to implement linear regression yourself, I highly recommend that you vectorize your input. By doing so, you can avoid using lots of loops and write cleaner code. Some knowledge of [linear algebra](https://github.com/jimmychimmyy/machine_learning_notes) required.

#### Sources
1. https://www.youtube.com/watch?v=ZkjP5RJLQF4 <- this is an amazing source to really grasp the concept of linear regression
2. http://www.statisticssolutions.com/assumptions-of-linear-regression/
3. http://ml-cheatsheet.readthedocs.io/en/latest/linear_regression.html#id3
4. http://www.holehouse.org/mlclass/04_Linear_Regression_with_multiple_variables.html
5. http://www.statisticshowto.com/mean-squared-error/
