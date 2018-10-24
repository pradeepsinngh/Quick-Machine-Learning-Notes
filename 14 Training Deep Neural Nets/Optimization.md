# Optimization Technquies:

Training a very large deep neural network can be painfully slow. So far we have seen four ways to speed up training:
- Applying a good intialization strategy for connection weights
- Use a good activation function (ReLu, ELU)
- Using Batch Normalization
- Reusing parts of a pretrained network

Another huge speed boost comes from using a faster optimizer than the regular Gradient Descent optimizer. We have following optimizers which can help us to speed up training:

1. Momentum Optimization:
2. Nesterov Accelerated Optimization:
3. AdaGrad:
4. RMSProp:
5. Adam Optimization:

## Momentum Optimization:
**Analogy:** Imagine a ball rolling down a gentle slope on a smooth surface: it will start out slowly, but it qill quickly pick up momentum untill it eventually reaches terminal velocity (if there is some friction or air resistance). This is very simple idea behind *Momentum Optimization*.

In contrast, regular Gradient Descent will simply take small regular steps down the slope, so it will take much more time to reach the bottom.

Gradient descent simply update the weights `theta(0)` by directly subtracting the gradient of the cost function `J(0)` with regards to the weights `(del J(0))` multiplied by learning rate. It does not care about what the earlier gradients were. If the local gradients is tiny, it goes very slowly.
`0 = 0 - `



