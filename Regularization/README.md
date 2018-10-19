# Regularization:

- it means adding some constraints to your model.
- it is used to avoid over-fitting. the few degree of freedoms it has, the harder it will be for it to overfilt the data.
- For eg: a simple way to regularize a polynomial model is to reduce the number of polynomial degrees.
- For a linear model, regularization is achieved by constraining the weights of the model.

### Ridge (L2) Regularization:
- adds “squared magnitude” of coefficient as penalty term to the loss function.
- it forces the algorithm to not only fit the data but also keep the model weights as small as possible.
- regularization term should only be added to the cost function during training, once model is trained, you should evaluate the performance using unregualrized performace measure.
- hyperparamter: alpha, controls how much you want to regualirze the model. if alpha = 0, then there is no regularization and if alpha is very large, then all weights end up very close to zero and result in no learning.
- NOTE: bias term is not regularized


### Lasso (L1) Regularization:
- adds “absolute value of magnitude” of coefficient as penalty term to the loss function.
- it uses the L1 norm of the weight vector instead of the half the sqaure of the L2 norm.
- Lasso shrinks the less important feature’s coefficient to zero.
- In short, it performs feature selection and outputs a sparse model.

### Elastic Net:
- simple mix of Ridge and Lasso regularization.

### Early Stopping:
- a different way to regularize iterative learning algorithms such as Gradient descent is to stop training early as soon as the validation error reaches a minimum. this is calle stopping early.
- As epochs go by, algorithm learns, and its prediction error (RMSE) on the training set naturally goes down, and so does its prediction error on the validation set. However, after a while the validation error stops decreasing and actually starts to go back up.
- This indicates that the model has started to overfit the training data. And, you should stop training at this point.
