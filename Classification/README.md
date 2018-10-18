# Classification:

**General Note:** Generally accuracy is not the preferred performace measure for classifiers, especially when you have skewed datasets (i.e. when some classes are much more frequent then others).

## Performance Measure:
Evaluating a classifier is always tricker than regressor. There are following performance measures available:

1. **Measuring Accuracy using Cross-Validation:**
   - A good way to evaluate a model is to use cross-validation.
   - Scikit-learn's ``` cross_val_score()``` function..returns the evaluation score.
   - We can also use StartifiedKFold() to produce folds that contain a represnetative ratio of each class. This function uses Stratified Sampling.
   
2. **Confusion Matrix:**
   - Baisc idea is count number of times class A has been classified as class B. For eg: To know how many times 5s has been classified as 3s, I'll look into the 5th row and 3rd Col of the confusion matrix.
   - sklearn...```conf_matrix()```
   - Eg: 
   ```
   from sklearn.metrics import confusion_matrix
   confusion_matrix(y_train,y_pred)
   array([[53272, 1307],
          [1077,  4344]])
   ```
   - Each row and col in confusion matrix represents an actual class and predicted class respectively.
   - The first row of this matrix considers non-5 images (the negative class): 53,272 of them were correctly classified as non-5s. They are called *True Negative*.
   - While remaining 1307 were wrong classified as 5s. they are called *False Positive*.
   - The second row of this matrix considers 5s images (the positive class): 1077 of them were wrongly classified as non-5s. They are called *False Negative*.
   - While remaining 4344 were correctly classified as 5s. they are called *True Positive*.
   
   - A perfect classifier would have only True Positive and True Negatives, so it's confusion matrix would have nonzero values on its main diagonal (top left to bottom right).
   
   - Eg: for perfect classifier:
   ```
   from sklearn.metrics import confusion_matrix
   confusion_matrix(y_train,y_pred)
   array([[53272, 0],
          [0,  4344]])
   ```

**Precision:** Accuracy of the positive prediction of the classifier. 
  - sklearn fun -- ```precision_score()```
  - Formula: ```Precision  = TP/ (TP + FP)```

**Recall:** Also called Sensitivity OR True Positive Rate. This is the ratio of positive instances that are correctly detected by the classifier.
  - sklearn fun -- ```recall_score()```
  - Formula: ```Recall= TP/ (TP + FN)```
  
**F1 Scoare:** It is often convenient to combine precision and recall into a single metric called F1 scoare.
  - F1 score is the harmonic mean of precision and recall. 
  - Why harmonic mean? Regular mean treates all values equally. the harmonic mean gives much more important to low values. As a result classifier will only get a high F1 score if both recall and precision are high.
  - Formula: ```F1 == 2/ (1/precision + 1/recall)) == TP / (TP + (FN + FP)/2)```
  - F1 score favors classifiers that have similar precision and recall. This is not what you want, in osme case you care more about: precision and in other cases your care about recall.
  
  - **Precision/Recall tradeoff** Increasing precision reduces recall, and vice versa, this is called precision/recall tradeoff.
  - Increasing threshold reduces recall and increases precision.
  - Conversely, lowering threshold increases recall and reduces precision.
  
  #### How to select good precision/recall tradeoff?
  Plot precision directly against recall
  
  
  
3. **ROC Curve:** Receiver operating characteristic 
   - 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
