# Stacking:
- short for stacked generalization.
- simple idea: instead of using trivial functions (such as hard voting) to aggregate the prediction for all the predictors in an ensemble, why don't train a model to perform this aggregation.
- Bottom line predictors (m in numbers) predcits different values(classes) and then the final predcitor (called meta learner or blender) takes these predictions as inputs and make final prediction.

### How to train Blender and First/ Bottom layer?
- Use hold-out set approach. 
- divide the training set into two subsets.
- Use first subset to train the predcitors in first layer.
- Next, the first layer predictors are used to make predictions on the second (held-out) set.
- This ensures that the predictions are clean, since the predictors never saw these instances during training.
- Now for each instances in held-out set, predcitors from first layer will have some predictions. 
- We will create a new training set using these predictied values from predcitors from first layer using held-out set.
- and, then blender is trained on this new training set, so it learns to predict the target value gievn the first layers predictions.

- We can have multiple layers.
- We can train several different blenders (one using linear regression, another using random forest regression, and so on.)
- Trick is to divided training set into m different subsets (m = number of layers).
- Use 1st subset to train first layers.
- 2nd subset is used to create training set used to train 2nd layer (using prediction made by first layer).
- and 3rd subset is used to create training set used to train 3rd layer (using prediction made by second layer).
- Once all layers are trained, we can go through all layers sequentially to make prediction on a new instance.


- You can parallize training of predcitors in a layer but you can not parallize layers itself, as learning/ training 2nd layer depends on 1st layer. etc.
- Does not scale very well.
