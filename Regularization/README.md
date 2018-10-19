# Regularization:

- it means adding some constraints to your model.
- it is used to avoid over-fitting. the few degree of freedoms it has, the harder it will be for it to overfilt the data.
- For eg: a simple way to regularize a polynomial model is to reduce the number of polynomial degrees.

- For a linear model, regularization is achieved by constraining the weights of the model.

### Ridge Regression:
- It is a regularized version of linear regression: a regularization term is added to the cost function.
- it forces the algorithm to not only fit the data but also keep the model weights as small as possible.
- regularization term should only be added to the cost function during training, once model is trained, you should evaluate the performance using unregualrized performace measure.

