# Support Vector Machines
- You can think of SVM classifier as fitting the widest possible street between classes. 
- this is called large margin classification.
- ML model capable of perfomring, linear or non-linear classification, regression, and even outlier detection.
- suited for classification of complex, but small- or medium sized datasets.

#### Decision boundary:
- A street that divides the classes.
- Support vectors define the decision boundary.
- Adding more training instances "off the street" will not affect the decision boundary at all: it is fully determined (or "supported") by the instances located on the edge of the street.

**Types:** Hard margin classification and Soft margin classification

#### Hard Margin Classification:
- Strict condition that all instances be off the street - this is hard margin
- **Issues:**
  - it works only if the data is linearly separable.
  - it is quite sensitive to outliers.
  - margin violations: instances that end up in the middle of the street or even on the wrong side.

#### Soft Margin Classification:
- To avoid problems with hard margin classifiers, we use more flexible model.
- Objective is to find a good balance between keeping the street as large as possible and limiting the margin violations.
- This is soft margin classification.

#### Hyperparameter:
- In Scikilt learn's, SVM class you can manage/ control this balance using the `C` hyperparameter.
- Smaller value of C leads to wide street but more margin violations.
- Higher value of C leads to narrow street but less margin violations.
- You can think of C as regularization hyperparameter.

### Things to note:
- SVM is sensitive to the features scales.
- your decision boundary will look much different/ better. (Use scikit learn's `StandardScaler`)

## Linear SVM Classification:
- SVM can be used for linear classification.
- Data should be linearly separable - i.e. data should be linear.

## Non-Linear SVM Classification:
- What if your data is not linearly separable? Use Nonlinear SVM Classifiers.
- Add more features. eg: polynomial features.
- Add features computed using similarity function -- that measures how much each instances resembles a particular landmark.  

**Q** How to handle non-linear datasets/ data? Add more features, such as polynomial features. In some cases, adding some features, daatset can become linearly separable.

## Problem: What is the issues with adding polynomial features?
1. - Adding ploynomial features is simple to implement and can work great with all sorts of ML models (not just SVMs).
- But, at a low polynomial degree SVM can not deal with very complex datasets.
- And, with a high ploynomial degree it creates a huge number of features, making the model too slow.


## How to fix this issue? Use Kernel trick!
- **Kernel Trick:** It makes it possible to get the same result as if you added many polynomial features, even with very high-degree polynomials, without actually having to add them. So, there is no combinattorial explosion of the number of features since you don't actually add any features. This trick is implemented by the SVC class. 
- 
- 

## Hyperparameter:
- In Scikit-learn, `coef0` is the hyperparameter, that controls how much the model is influenced by high-degree polynomials vs lower-degree polynomials.













