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

## How to tackle Vanishing/ Exploding Gradients Problem?
What we need is the signal to flow properly in both directions: in forward direction when making predictions, and in the reverse directions when back propgating gradients. We don't want singal to die out, nor do we want it to explode and staturate.

### **Xavier and He Initialization:**
- We want variance of of the outputs of each layer eqyal to variances of inputs.
- We also want gradients to have equal variance before and after flowing through a layer in the reverse direction.
- It is actually not possible to have this, unless you have equal no of inputs and outputs connections.
- A good compromise: the connections weights must be initialized randomly.
- If you have roughly equal n_inputs and n_outputs, you get s.d. = 1/sq_root(n_inputs) and mean 0.
- Xavier initialization can speed up the training process.

- The initialization startegy for ReLu activation fnction (and ELU activation) is called **He Initialization**.
- s.d. = sq_root(2) * sq_root(2/(n_inputs + n_outputs)) and mean 0

**Analogy:**
- If you set a microphones amplifier's knob too close to zero, people won't be able to hear anything.
- If you set a microphones amplifier's knob too close to max, voice witll explode/ saturate, people won't be able to understand anything.
- Now, imagine a chain of such amplifiers: they need to set propely in order to for your voic to come out loud and clear at the end of chain.
- Your voide has to come out of each amplifier at the same amplitude as it came in.



### **Nonsaturating Activation Functions:**
- Vanishing gradient problems were in part due to a poor choice of activation function.
- For very long people thought, if sigmoid activation function is used in biological neurons, they must be excellent choice.
- But, it turns out other activation functions like ReLu works much better.
- ReLu in particular, becuase it does not saturate for positive values (and also because it's fast to compute).

##### Problems with ReLu?
- suffers from dying ReLu problem.
- during training some neurons die, meaning they stop outputing anything other than 0.
- In some cases, you may find more than half the neurons are dead, esp if you are using large learning rate.
- During training, if a neuron's weight get updated such that the weighted sum of the neurons is negative, it will start outputting 0.
- when this happens the neuron is unlikely to come back to life since the gradient of the ReLu func is 0 when input is negative.

- To slove this problem, use can use variant of the ReLu function, such as *Leaky ReLu*.
- Leaky ReLu is defined as LeakyReLu = max(alpha * z, z)
- hyperparameter alpha define how much the func leaks.
- for z < 0 it is the slope of function and is typically set to 0.001.
- This small slope ensures that leaky ReLu never dies; they can go into long comma, but they have a chance to eventually wake up.


#### ELU: Exponential Linear Unit:
- better than ReLu and performs better.
- ELU (z) = alpha(exp(z) - 1) if z < 0
- ELU (z) = z                 if z >= 0

- It looks like ReLu, with few major changes:
  - has non zero gradient for z< 0, which avoides dying units issue.
  - func is smooth everywhere, including at z = 0
  - it takes on negative value when z <0 which allow unit to have an average output closer to 0. this helps in alleviating vanishing gradient problem.
  
**Problems:**
  - slower to compute than ReLu and it's variants due to use of exponential function.
 

##### What activation function to choose for hidden layers?
- general ELU > Leaky ReLu > ReLu > tanh > logistic 
- if you care about runtime performance: you may use Leaky ReLu over ELUs

### Batch Normalization:

**Internal Covariate shift**
Covariate shift refers to the change in the input distribution to a learning system. In the case of deep networks, the input to each layer is affected by parameters in all the input layers. So even small changes to the network get amplified down the network. This leads to change in the input distribution to internal layers of the deep network and is known as internal covariate shift.

It is well established that networks converge faster if the inputs have been whitened (ie zero mean, unit variances) and are uncorrelated and internal covariate shift leads to just the opposite.

The technique consists of adding an opration in the model just before the activation func of each layer, simply zero-centering and normalizing the inputs, then scaling and shifting the result using two new parameters per layer. In other words, this operation lets the model learn the optimal scale and mean of the inputs for each layer.

During traiing time, in order to zero-center and normalize the inputs, the algorithm needs to estimate the input mean and std. dev. It does so by evaluating the mean and std. dev. by evaluating mean and std. dev. of the inputs over the current mini batch.

During test time, the normalization is done using the population statistics instead of mini-batch statistics to ensure that the output deterministically depends on the input.

**Advantages Of Batch Normalization**
- Reduces internal covariant shift.
- Reduces the dependence of gradients on the scale of the parameters or their initial values.
- Regularizes the model and reduces the need for dropout, photometric distortions, local response normalization and other regularization techniques.
- Allows use of saturating nonlinearities and higher learning rates.

