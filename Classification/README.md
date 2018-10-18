# Classification:

**General Note:** Generally accuracy is not the preferred performace measure for classifiers, especially when you have skewed datasets (i.e. when some classes are much more frequent then others).

## Performance Measure:
Evaluating a classifier is always tricker than regressor. There are following performance measures available:

1. **Measuring Accuracy using Cross-Validation:**
   - A good way to evaluate a model is to use cross-validation.
   - Scikit-learn's ``` cross_val_score()``` function.
   - We can also use StartifiedKFold() to produce folds that contain a represnetative ratio of each class. This function uses Stratified Sampling.
   
 2. **Confusion Matrix:**
 
   
