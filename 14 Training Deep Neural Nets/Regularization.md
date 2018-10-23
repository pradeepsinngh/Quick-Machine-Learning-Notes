# Regularization:

Deep neural networks typically have tens of thousands of parameters, sometimes even millions. With so many parameters, the network has an incredible amount of freedom and can fit a huge variety of complex datasets. But this great flexi bility also means that it is prone to overfitting the training set.

1. Early Stopping
2. L1 and L2 Regularization
3. Dropout
4. Max-Norm Regularization
5. Data Augmentation

## Early Stopping:
To avoid overfitting the training set, a great solution is early stopping: just interrupt training when its performance on the validation set starts dropping.

## L1 and L2 Regularization:
#### L1 Regularization:
- a regularization term is added to the cost function.
- adds “absolute value of magnitude” of coefficient as penalty term to the loss function.
- it uses the L1 norm of the weight vector instead of the half the sqaure of the L2 norm.
- Lasso shrinks the less important feature’s coefficient to zero.
- In short, it performs feature selection and outputs a sparse model.


#### L2 Regularization:
- adds “squared magnitude” of coefficient as penalty term to the loss function.
- it forces the algorithm to not only fit the data but also keep the model weights as small as possible.
- regularization term should only be added to the cost function during training, once model is trained, you should evaluate the performance using unregualrized performace measure.
- hyperparamter: alpha, controls how much you want to regualirze the model. if alpha = 0, then there is no regularization and if alpha is very large, then all weights end up very close to zero and result in no learning.
-  NOTE: bias term is not regularized

## Dropout:
Baisc idea behind dropout is that at every training iteration/ step, every neuron has a probability p being temporarily dropped out, meaning it will be entirely ignored during this training step, but it may be active during next step. The hyperparameter p is called drop out and it is typically set to 50%. After training neurons don't get dropped anymore.

## Max-Norm Regularization:
Baisc idea behind max-norm regularization is that for each neuron, it constrains the weight w of the incoming connections such that || w || <= r, where r is the max-norm hyperparameter and ||.|| is the L2 norm.

Reducing r (i.e. keeping weight of the incoming connection low) increases the amount of regularization and helps reduce overfitting. Max-norm regularization can also help alleviate the vanishing/ exploding gradients problems.

## Data Augmentation:
Idea behind data agumentation is to generate more images by artificaaly boosting the size of the images in your training set - this will help you in two ways; you will have more training instances and your training instances will be more diverse.

**For eg:** If your model is meant to classify picture as mushrooms, you can slightly shift, rotate and resize every picture in the training set by various amounts and add the resulting pictures to the training set. This forces the model to be more tolerant to the position, orientation, and the size of the mushrooms in the picture. If you want model to be tolerant to the lighting conditions, you can similarly generate many images with various contrasts. 





