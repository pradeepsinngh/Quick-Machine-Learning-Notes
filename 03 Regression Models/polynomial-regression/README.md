# Polynomial Regression:
What if your data is actually more complex than a simple straight line? 
Just use linear models to fit nonlinear data. A simple way to do this is to add powers of each features as new features, then train a linear model on this extended set of features. this is called polynomial regression.

Use sklearn's `PolynomialFeatures` class to transform training data, adding n degree polynomial of each feature in the training as new features.

```
from sklearn.preprocessing import PolynomialFeatures
poly_feature = PolynomialFeatures(degree=2, include_bias=False)
X_poly= poly_features.fit_transform(X)
```
## Assumptions:
1. There must be a linear relationship between the outcome variable and the independent variables. 
   - Scatterplots can show whether there is a linear or curvilinear relationship.
2. Multivariate Normality
   - Multiple regression assumes that the residuals are normally distributed.
3. No Multicollinearity
   - Correlation matrix
   - Solution to Multicollinearity - center the data, substract the mean from each observation.
4. Homoscedasticity
   - Use scatter plot
   -  A scatterplot of residuals versus predicted values is good way to check for homoscedasticity. 
   - There should be no clear pattern in the distribution; if there is a cone-shaped pattern, the data is heteroscedastic.
