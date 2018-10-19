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

#### Computational Complexitiy:
- it's training time complexity is roughly, O(m * n).
- algorithm takes longer if you need very high precision. This is controlled by tolerance hyperparameter -- called tol in Scikit-learn. It is set to fine by default.

## Non-Linear SVM Classification:
### What if your data is not linearly separable? 
1. Use Nonlinear SVM Classifiers.
2. Add more features. eg: polynomial features.
3. Add features computed using similarity function -- that measures how much each instances resembles a particular landmark.  

**Q** How to handle non-linear datasets/ data? Add more features, such as polynomial features. In some cases, adding some features, daatset can become linearly separable.

#### Problem: What is the issues with adding polynomial features?
- Adding ploynomial features is simple to implement and can work great with all sorts of ML models (not just SVMs).
- But, at a low polynomial degree SVM can not deal with very complex datasets.
- And, with a high ploynomial degree it creates a huge number of features, making the model too slow.

#### How to fix this issue? Use Kernel trick!
- **Kernel Trick:** It makes it possible to get the same result as if you added many polynomial features, even with very high-degree polynomials, without actually having to add them. So, there is no combinattorial explosion of the number of features since you don't actually add any features. This trick is implemented by the SVC class. 

### Hyperparameter:
- In Scikit-learn, `coef0` is the hyperparameter, that controls how much the model is influenced by high-degree polynomials vs lower-degree polynomials.
- degree
- C


## Adding Similarity Function:
- it helps tackling nonlinear problems.
- Add features computed using similarity function - that measures how much each instances resembles a particular landmark.
- Eg: Similarity function -- Gaussian Radial Basis Function (RBF)
  - RBF is a bell-shaped function varying from 0(very fra from the landmark) to 1 (at the landmark).
 - Adding new fatures using similarity function can transform the datasets, with newer dataset being linearly seprable.
 
 - **How to select landmark?**
 - Simple Approach:
   - Create landmark at the location of each and every instance in the dataset. This creates many dimensions and thus increase the chance that the transformed training set will be linearly seprable.
 
#### Problem: What is the issues with adding features using similarity function (Gaussian RBF)?
 - A training set with m instances and n features get transformed into a training set with m instances and m features.
 - So, if your training set is large you end with up an equally large number of features.
 - So, it is computationally expensive. Computing all the additional features, especially on large training sets.
  
#### How to fix this issue? Use Kernel trick!
- **Kernel Trick:** it makes it possible to obtain a similar results as if you had added many similarity features, without actually having to add them.

#### Hyperparameter:
- C
- Gamma: 
  - increasing gamma makes the bell-shape curve narrower and as a result each instance's range of influence is smaller, the decision boundary ends up being more irregular, wiggling around individual instances.
  - conversely, a small gamma value makes the bell-shaped curve wider, so instances have a larger range of influence, and the decision boundary ends up smoother. 
  - So, gamma acts like a regularization hyperparameter.
     - If you model is overfitting, reduce gamma.
     - If your model is underfitting, increase the gamma.
 

### Which kernel to choose and how?
- There are so many kernels to choose from. For eg: string kernels.
- There are specialized kernels for specific data structures.
- **Thumb Rule:**
  - Always try linear kernel first.(esp, if training set is large OR if it has plenty of features.)
  - If training set is not too large, go with Gaussian RBF kernel.
  - Try some other kernels, using cross-validation and grid search.


### Computaional Complexity:
- the training time complexity is usually between O(m2 * n) and O(m3 * n).
- this means it gets slower when the training instances gets large
- this algorithm is perfect for complex but small or medimum datasets.




