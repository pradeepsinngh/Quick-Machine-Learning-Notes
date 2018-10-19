# Polynomial Regression:
What if your data is actually more complex than a simple straight line? 
Just use linear models to fit nonlinear data. A simple way to do this is to add powers of each features as new features, then train a linear model on this extended set of features. this is called polynomial regression.

Use sklearn's `PolynomialFeatures` class to transform training data, adding n degree polynomial of each feature in the training as new features.

```
from sklearn.preprocessing import PolynomialFeatures
poly_feature = PolynomialFeatures(degree=2, include_bias=False)
X_poly= poly_features.fit_transform(X)
```
