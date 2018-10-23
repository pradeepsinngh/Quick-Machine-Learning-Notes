# Vanishing/ Exploding Gradients Problem:

The back-propagation algorithm works by going from the output layer to the input layer, propagating the error gradient on the way. Once the algorithm has computed the gradient of the cost function with regard to each parameter in the network, it uses these gradients to update each parameter with a Gradient Descent step.

Unfortunately, gradients often gest smaller and smaller as the algorithm progresses down to the lower layers. As a result, the Gradient Descent update leaves the lower layer connections weights virtually unchanged, and trining never converges to a good solution. This is called **vanishing gradient problem*.

In some cases, the oppoiste can happen: the gradient can grow bigger and bigger, so many layers get insanely larger weight updates and the algorithm diverges. This is called **exploding gradient problem*.

More generally, deep neural networks suffer from unstable gradients; different layers may learn at widely different speeds.

### Why does this happen?
In 2010, A paper titled "*Understanding the Difficulty of Training Deep Feedforward Neural Networks *", discussed few suspects, including the combination of logistic sigmoid activation function and the weight initialization using a normal distribution with mean 0 and S.D. of 1.

In short, they showed that with this activation function and initialization scheme, the variance of the outputs of each layer is much greater than the variance of its inputs. Going forward in the network, the variance keeps increasing after each layer unitil the activation function staurates at the top layers.

This is actually made worse by the fact that the logistic function has a mean of 0.5, not 0 (the hyperboloc tangent function has mean 0 and behaves slighlty better than the logistic function in deep networks).

You can see Logisitic activation function, when input becomes large (negative or positive), the function staturates at 0 or 1, with a derivative extermely close to 0. Thus when we backpropagate, it has virtually no gradient to go back and update weights. Whatever little gradient is left used to update top layers, as we go back (to wards lower layers) there is nothingleft for lower layers.

### How to tackle Vanishing/ Exploding Gradients Problem?
