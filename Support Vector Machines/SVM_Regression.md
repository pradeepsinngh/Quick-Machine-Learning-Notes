# SVM Regression:
- not only supports linear and non-linear classification, but also supports linear and non-linear regression.
- The trick is to reverse the objective: instead of trying to fit the largest possible street between two classes while limiting margin violations, SVM Regression tries to fit as many instances as possible on the street while limiting the margin violations.
- The width of the street is controlled by a hyperparameter - epsilon.

## Linear SVM Regression:
- for linear SVM regression use LinearSVM.
- Use scikit-learn's, LinearSVR class to perform linear SVM Regression.
  ```
  from sklearn.preprocessing import LinearSVR
  svm_reg = LinearSVR(epsilon = 1.5)
  svm_reg.fit(X,y)
  ```
- hyperparameter:
  - epsilon
  
## Non-Linear SVM Regression:
- for linear SVM regression use kernelized SVM model.
- Use scikit-learn's, kernelizedLinearSVR class to perform linear SVM Regression.
  ```
  from sklearn.preprocessing import SVR
  svm_poly_reg = SVR(kernel="poly", degree=2, C=100, epsilon = 0.1)
  svm_poly_reg.fit(X,y)
  ```
- hyperparameter:
  - epsilon
  - kernel
  - degree
  - C
  
