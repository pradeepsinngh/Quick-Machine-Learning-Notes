# Boosting

- refers to ensemble method that can combine several weak learners into a strong learner.
- Idea is to train predictors sequentially, each trying to correct its predecssor.
- There are many boosting methods, by far the most famous are: Adaboost and Gradient Boosting.

# AdaBoost:
- In AdaBoost, predictor focuses more and more on hard case i.e. cases on which it's predecessor underfitted. 
- So, it's like current predictor is correcting it's predecessor by working/ focusing more on cases where it's predecessor failed.

**For Eg:** To build an AdaBoost classifier,
- First base classifier (such as DT) is trained and used to make predcition on the training set. 
- The relative weight of mis-classified training instances is then increased.
- A second classifier is trained using the updated weight and again it make prediction on the training set.
- again weights are updated and so on.

### Similarity with Gradient Descent:
- Gradient Descent:
  - iterative algorithm.
  - tweak single predcitior parameters to minimize cost function.
- AdaBoost:
  - sequential learning algo.
  - AdaBoost adds predcitiors to the ensemble gradually making them better.
  
### Drawbacks:
- Cannot be parallized, since each predcitor can only be trained after the previous predcitor has been trained, evaluated.
- You can only parallize each/ every predcitior themseleves.
- Doesn't not scale very well ( as compare to bagging or pasting).

-----------------------------------------------------------------------------------------------------------------------------

# Gradient Boosting
