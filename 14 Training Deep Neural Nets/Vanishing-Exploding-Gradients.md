# Vanishing/ Exploding Gradients Problem:

The back-propagation algorithm works by going from the output layer to the input layer, propagating the error gradient on the way. Once the algorithm has computed the gradient of the cost function with regard to each parameter int he network, it uses these gradients to update each parameter with a Gradient Descent step.
