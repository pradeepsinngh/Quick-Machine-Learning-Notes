# ROC Curve and AUC

#### What is the ROC Curve?

The ROC Curve is a graph that illustrates the ability of a binary classifier to distinguish between two classes at all classification thresholds.

The ROC Curve plots the **True Positive Rate (TPR)** against the **False Positive Rate (FPR)**.

`TPR = TP / (TP + FN)`

When the actual classification is positive, how often does the classifier predict correctly positive?

`FPR = FP / (FP + TN)`

When the actual classification is negative, how often does the classifier predict incorrectly predict positive?

*To plot the ROC Curve, simply plot the TPR versus the FPR for all possible classification thresholds which range from 0 to 1.*

ROC Curve more beneficial than using misclassification rate because ROC Curve visualizes all possible thresholds whereas misclassification rate only represents error rate for a single threshold.

#### What is AUC?

AUC is **Area Under the ROC Curve** which measures the area underneath the entire ROC Curve.

When AUC = 0.5, it means our model does separates classes poorly, no better than random guessing.

When AUC = 1.0, it means our model is a perfect classifier.

#### When do we use it?

You should always use ROC Curve and AUC when you have a binary classification problem.

#### Things to watch out for?

1. Imbalanced classes
2. Predicted Probabilities are unlikely to have "smooth" distribution

#### Important Notes:

1. AUC is scale-invariance

  AUC is only sensitive to rank-ordering (are the probabilities always in the same order?)

2. AUC is classification-threshold-invariant

3. You can extend ROC Curves for multi-class problems by using a one-versus-all approach


#### Sources
1. https://en.wikipedia.org/wiki/Receiver_operating_characteristic
2. https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
3. https://www.youtube.com/watch?v=OAl6eAyP-yo
