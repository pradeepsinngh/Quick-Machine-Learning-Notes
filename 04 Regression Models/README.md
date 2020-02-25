# Regression Models
- Regression means, a measure of the relation between one variable (e.g. output) and corresponding values of other variables (eg input variables)
- We fit a curve / line to the data points, in such a manner that the differences between the distances of data points from the curve or line is minimized.

### Types of Regression:
- number of independent variables
- type of dependent variables 
- shape of regression line

1. Linea Regression
2. Logistic Regression
3. Polynomial Regression
4. Stepwise Regression
5. Ridge Regression
6. Lasso Regression
7. ElasticNet Regression

### Linear Regression:
In this technique, 
  - the dependent variable is continuous, 
  - independent variable(s) can be continuous or discrete,
  - nature of regression line is linear.

Linear Regression establishes a relationship between dependent variable (Y) and one or more independent variables (X) using a best fit straight line (also known as regression line).

It is represented by an equation ```Y=a+b*X + e```, where *a* is intercept, *b* is slope of the line and *e* is error term. This equation can be used to predict the value of target variable based on given predictor variable(s).

The **difference between simple linear regression and multiple linear regression** is that, multiple linear regression has (>1) independent variables, whereas simple linear regression has only 1 independent variable. 

We can evaluate the model performance using the metric [R-square](https://www.analyticsvidhya.com/blog/2019/08/11-important-model-evaluation-error-metrics/). 

#### How do we obtain best fit line?
##### Least Square Method:
- It is the most common method used for fitting a regression line. 
- It calculates the best-fit line for the observed data by minimizing the sum of the squares of the vertical deviations from each data point to the line. 
- Because the deviations are first squared, when added, there is no cancelling out between positive and negative values.


#### Assumptions for Linear Regression:
- There must be linear relationship between independent and dependent variables
- Multiple regression suffers from multicollinearity, autocorrelation, heteroskedasticity.
- Linear Regression is very sensitive to Outliers.
- Multicollinearity can increase the variance of the coefficient estimates and make the estimates very sensitive to minor changes in the model. The result is that the coefficient estimates are unstable.
- In case of multiple independent variables, we can go with forward selection, backward elimination and step wise approach for selection of most significant independent variables.

### Logistic Regression:
- Logistic regression is used to find the probability of event=Success and event=Failure. It is used when dependent variable is binary (0/ 1, True/ False, Yes/ No) in nature.


```
odds = p/ (1-p) = probability of event occurrence / probability of not event occurrence
ln(odds) = ln(p/(1-p))
logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk
```
Above, p is the probability of presence of the characteristic of interest. 

### Why have we used log in the equation?.
Since we are working here with a binomial distribution (dependent variable), we need to choose a link function which is best suited for this distribution. And, it is logit function. In the equation above, the parameters are chosen to maximize the likelihood of observing the sample values rather than minimizing the sum of squared errors (like in ordinary regression).

### Importnat Notes:
- Logistic regression doesn’t require linear relationship between dependent and independent variables. It can handle various types of relationships because it applies a non-linear log transformation to the predicted odds ratio.
- To avoid over fitting and under fitting, we should include all significant variables. A good approach to ensure this practice is to use a step wise method to estimate the logistic regression
- It requires large sample sizes because maximum likelihood estimates are less powerful at low sample sizes than ordinary least square.
- The independent variables should not be correlated with each other i.e. no multi collinearity.  

## Polynomial Regression:
A regression equation is a polynomial regression equation if the power of independent variable is more than 1. The equation below represents a polynomial equation:

```y = a + b * x^2```
- In this regression technique, the best fit line is not a straight line. 
- It is rather a curve that fits into the data points.

### Important Points:
- While there might be a temptation to fit a higher degree polynomial to get lower error, this can result in over-fitting. - Always plot the relationships to see the fit and focus on making sure that the curve fits the nature of the problem. 
- Especially look out for curve towards the ends and see whether those shapes and trends make sense. 
- Higher polynomials can end up producing wierd results on extrapolation.

## Stepwise Regression:
- This form of regression is used when we deal with multiple independent variables. 
- In this technique, the selection of independent variables is done with the help of an automatic process, which involves no human intervention.

- This feat is achieved by observing statistical values like R-square, t-stats and AIC metric to discern significant variables. - Stepwise regression basically fits the regression model by adding/dropping co-variates one at a time based on a specified criterion.

Some of the most commonly used Stepwise regression methods are listed below:
- Standard stepwise regression does two things. It adds and removes predictors as needed for each step.
- Forward selection starts with most significant predictor in the model and adds variable for each step.
- Backward elimination starts with all predictors in the model and removes the least significant variable for each step.

- The aim of this modeling technique is to maximize the prediction power with minimum number of predictor variables. It is one of the method to handle higher dimensionality of data set.



## Ridge Regression
 - Ridge Regression is a technique used when the data suffers from multicollinearity (independent variables are highly correlated). 
 - In multicollinearity, even though the least squares estimates (OLS) are unbiased, their variances are large which deviates the observed value far from the true value. 
 - By adding a degree of bias to the regression estimates, ridge regression reduces the standard errors.

Above, we saw the equation for linear regression. Remember? It can be represented as:

```y=a+ b*x```

This equation also has an error term. The complete equation becomes:

```y=a+b*x+e (error term),  
e: error term is the value needed to correct for a prediction error between the observed and predicted value
```

```y=a+y= a+ b1x1+ b2x2+....+e, for multiple independent variables.```

In a linear equation, prediction errors can be decomposed into two sub components.
 - bias
 - variance
 
Ridge regression solves the multicollinearity problem through shrinkage parameter λ (lambda). Look at the equation below.

![Ridge Regression](https://github.com/pradeepsinngh/Quick-Machine-Learning-Notes/blob/master/misc/figures/Ridge2.png)

In this equation, we have two components:-
- First one is least square term and 
- other one is lambda of the summation of β2 (beta- square) where β is the coefficient. This is added to least square term in order to shrink the parameter to have a very low variance.

### Important Notes:
- The assumptions of this regression is same as least squared regression except normality is not to be assumed.
- Ridge regression shrinks the value of coefficients but doesn’t reaches zero, which suggests no feature selection feature.
- This is a regularization method and uses l2 regularization.


## Lasso Regression:
![LAsso Regression](https://github.com/pradeepsinngh/Quick-Machine-Learning-Notes/blob/master/misc/figures/Lasso.png)

*Lasso (Least Absolute Shrinkage and Selection Operator)* also penalizes the absolute size of the regression coefficients. It is capable of reducing the variability and improving the accuracy of linear regression models.  

- Lasso regression differs from ridge regression in a way that it uses absolute values in the penalty function, instead of squares. 
- This leads to penalizing (or equivalently constraining the sum of the absolute values of the estimates) values which causes some of the parameter estimates to turn out exactly zero. 
- Larger the penalty applied, further the estimates get shrunk towards absolute zero. This results to variable selection out of given n variables.

#### Important Points:
- The assumptions of lasso regression is same as least squared regression except normality is not to be assumed
- Lasso Regression shrinks coefficients to zero (exactly zero), which certainly helps in feature selection
- Lasso is a regularization method and uses l1 regularization
- If group of predictors are highly correlated, lasso picks only one of them and shrinks the others to zero.

## ElasaticNet Regression:
- ElasticNet is hybrid of Lasso and Ridge Regression techniques. 
- It is trained with L1 and L2 prior as regularizer. 
- Elastic-net is useful when there are multiple features which are correlated. 
- Lasso is likely to pick one of these at random, while elastic-net is likely to pick both.

![LAsso Regression](https://github.com/pradeepsinngh/Quick-Machine-Learning-Notes/blob/master/misc/figures/Elastic_Net.png)

A practical advantage of trading-off between Lasso and Ridge is that, it allows Elastic-Net to inherit some of Ridge’s stability under rotation.

#### Important Points:
- It encourages group effect in case of highly correlated variables
- There are no limitations on the number of selected variables
- It can suffer with double shrinkage

