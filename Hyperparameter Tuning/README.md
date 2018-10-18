# Hyperparameter Tuning:

1. **Manual Search:**
   - One way to do is to fiddle with hyperparameters manually, untill you find a great combination of hyperparameter values.
   - This is very tedious and you may not have time to explore many combinations.

2. **Grid Search:**
   - Scikit-Learn's provides ```GridSearchCV```.
   - all you need to tell is which hyperparameter you want to experiment and what values to try out, and it will evaluate all possible combinations of hyperparameters values using cross validation.
