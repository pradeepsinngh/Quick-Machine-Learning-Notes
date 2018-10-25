# Recurrent Neural Networks:

A class of nets that can predict the future (well, up to a point, of course). They can analyze time series data such as stock prices, and tell you when to buy or sell. They can anticipate the car trajectories and help avoid accidents. More generally, they can work on sequences of arbitrary lengths, rather than on fixed size inputs like FNN/ CNNS.

### Recurrent Neurons:
- In FNN, activation flow is only in one direction, from input layer to the output layer.
- In RNN, is pretty much like FNN, but it also has connections pointing backward.
- So, at each time step t, this recurrent neuron receives this inputs X(t) as well as its own output from the previous time step Y(t-1).
- Each recurrent neuron has 2 set of weights: one for the inputs X(t) and the other for the outputs of the previous time step, Y(t-1).
- Let's call these weights vectos for a recurrent neuron as W(x) and W(y). If we consider whole recurrent layer with n neurons, then we can place all weight vectors in two weight matrices, W(x) and W(y). 
- Then the output vector of the whole layer is computed as: `Y(t) = phi(W(x) * x(t) + W(y) * y(t-1) + b)`
- NOTE: Many people prefer to use tanh activation func in RNNs rather than ReLU activation func.

### Memory Cells:
A part of neural network that preserves some state across time step is called a memory cells (or simple cell).

### Input and Output Sequences:
1. Seq to Seq: A RNN can simultaneously take a sequence of inputs and produce a sequence of outputs. 
          - For eg: predicting time series suc as stock price.
2. Seq to Vector: feed the network a sequence of inputs, and ignore all outputs except for the last one. 
             - For eg: Feed a movie review and model will give you a sentiment score.
3. Vector to Seq: Feed single input at the first time step (and 0 at all other time steps) and let it output a seq.
             - For eg: Input a image and output could be a caption for that image.
4. Seq to Vector is called Encode and Vect to Seq is called Decoder. And these both are used Machine translation tasks. And, this two-step model is called Encode-Decoder model.

#### How do you handle variable length Input and Output Sequences?
- **Input Sequences:** Padd with zero
- **Output Sequences:** Define a special output called an end-of-sequence token (EOS token). And, any output past the EOS should be ignored.

