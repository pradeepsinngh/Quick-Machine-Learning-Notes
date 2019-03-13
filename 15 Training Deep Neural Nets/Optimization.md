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


--------------------------------------------------------------------------------------------------------------------------

## Momentum Optimization:
**Analogy:** Imagine a ball rolling down a gentle slope on a smooth surface: it will start out slowly, but it qill quickly pick up momentum untill it eventually reaches terminal velocity (if there is some friction or air resistance). This is very simple idea behind *Momentum Optimization*.

In contrast, regular Gradient Descent will simply take small regular steps down the slope, so it will take much more time to reach the bottom.

Gradient descent simply update the weights `theta(0)` by directly subtracting the gradient of the cost function `J(0)` with regards to the weights `(del J(0))` multiplied by learning rate. It does not care about what the earlier gradients were. If the local gradients is tiny, it goes very slowly.

The equation is : `0 = 0 - learning_rate * del J(0)`

**Momemtum optimization** cares a great deal about what previous gradients were: at each iteration, it subtracts the local gradient from the momentum vector m (multiplied by the learning rate), and it updates the weight by simply adding this momentum vector. In other words, the gradient is used as an accelration, not as speed. 

To simulate some sort of friction mechanism and prevent the momentum from growing too large, the algorithm introduces a new hyperparameter called beta, simply called momentum, which must be set between 0 (high friction) and 1 (no friction). A typical value is 0.9.

The equation is : `m = beta * m - learning_rate * del J(0)`
                   `0 = 0 + m`

Due to the momentum, the optimizer may over shoot a bit, then come back, overshoot again, and oscillate like many times before stabilizing at the minimum. This is one of the reason why it is good to have a bit of friction in the system: it gets rid of these osciallations and thus speeds up convergence.

** Drawback:** It adds one more hyperparameter: beta. However, momentum value (beta) of 0.9 usually works well in practice and almost always goes faster then gradient descent.

#### Summary:
- Momentum optimization is faster than gradient descent and escapes from plateaus much faster than gradient descent.
- Gradient descent goes down the steep slope quite fast, but then it takes a very long time to go down the valley.
- In contrast, momentum optimization will roll down the bottom of the valley faster and faster untill it reaches the bottom (the optimum).

--------------------------------------------------------------------------------------------------------------------------

## Nesterov Accelerated Optimization (NAG):
- small tweak to momentum optimization.
- It measures the gradient of cost function not at the local position but slightly ahead in the direction of the momentum.
- The only difference from vanilla momentum optimization is that the gradient is measured at `0 + beta * m ` rather than at `0`.

The equation is : `m = beta * m - learning_rate * del J(0 + beta * m)`
                  `0 = 0 + m`

The small tweak works because in general the momentum vector will be pointing in the right direction, so it will be slightly more acurate to use the gradient measured a bit farther in that direction rather than using the gradient at the orignal position.

- It will almost always speedup the training compared to regular momentum optimization.

--------------------------------------------------------------------------------------------------------------------------

## AdaGrad: (Adaptive Learning)
Consider: Gradient descent starts by quickly going down the steepest slope, then slowly goes down the bottom of the valley. It would be nice if algorithm could detect this early on and correct its direction to point a bit more toward the global optimum.

AdaGrad algorithm achieves this by scaling down the gradient vector along the steepest dimensions. In short, this algorithm decays the learning rate, but it does so faster for steep dimensions than for dimensions with gentler slopes. This is called an adaptive learning rate. It helps point the resulting updates more directly toward the global optimum and requires much less tuning of learning rate hyperparameter.

**Drawbacks:**
- It stops too early for neuran network based models. The learning rates gets scaled down so much that the algorithm ends up stopping entirely before reaching the global optimum.
- Slows down a bit too fast and ends up never converging to the gloabl optimum.

--------------------------------------------------------------------------------------------------------------------------

## RMSProp:
- RMSProp fixes AdaGrad drawback: Slows down a bit too fast and ends up never converging to the gloabl optimum.
- RMSProp fixes this by accumlating only the gradient from most recent iterations (as opposed to all the gradients since the begining of the training).
- It does so by using exponential decay.
- The decay rate beta is typically set to 0.9.
- Yes, it is once again new hyperparameter, but this default value often works well, so you may not need t tune it all.


--------------------------------------------------------------------------------------------------------------------------

## Adam Optimization:
- stands for: Adaptive moment estimation, combines idea of Momentum optimization and RMSProp.
- Just like Momentum optimization it keeps track of an exponentially decaying avergae of past gradients and just like RMSProp it keeps track of an exponentially decaying average of past squared gradients.
- momentum decay hyperparameter (beta 1): is intitalized to 0.9, while the scaling decay hyperparameter (beta 2) is often intialized to 0.999.






