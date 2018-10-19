# Support Vector Machines:

## How does SVM make prediction and how their training algorithms work?

#### Starting with linear SVM classifier.
- The linear SVM classifier model predicts the class of a new instance x by simply computing the decision function: `w(transpose). x + b `.
- If the result is positive, the predicted class y_hat is positive class (1) or else it is the negative class (0).

```
(y_hat) = 0 if w(transpose) . x + b < 0,
(y_hat) = 1 if w(transpose) . x + b >= 0,
```
### Descion Boundary: 
- Descion boundary is the set of points where the decision function is equal 0. it is the intersection of two planes, which is a straight line.
- Dashed lines represents the points where the decision function is equal to 1 0r -1. 
  - They are parallel and at equal distance to the decision boundary, forming a margin around it.
- Training SVM means finding the value of w and b that makes the margin as wide as possible while avoiding margin violations (hard margin) or limiting them (soft margin).
