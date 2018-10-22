# Hyperparameter Tuning:

1. **Manual Search:**
   - One way to do is to fiddle with hyperparameters manually, untill you find a great combination of hyperparameter values.
   - This is very tedious and you may not have time to explore many combinations.

2. **Grid Search:**
   - Scikit-Learn's provides ```GridSearchCV```.
   - all you need to tell is which hyperparameter you want to experiment and what values to try out, and it will evaluate all possible combinations of hyperparameters values using cross validation.
   - fine to use if you are exploring relatively few combinations and search space is small.
     
3. **Randomized Search:**
   - Use when search space is large.
   - Scikit-Learn's provides ```RandomizedSearchCV```.
   - it evaluates a given number of random combinations by selecting a random value for each hyperparameter at every iteration.
   - Benefits:
     - if you let randomized search run for, say, 1000 iterations, this approach will explore 1,000 different values for each hyperparameter (instead for just few values per hyperparameter with grid search approach)
     - you have more control over the computing budget you want to allocate to hyper-parameter search, simply by setting the number of iterations.
     
     
4. **Bayesian Optimization:**
