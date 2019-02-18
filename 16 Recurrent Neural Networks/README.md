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

### How to train RNNs?
To train an RNN, the trick is to unroll it through time and then simply use regular backpropagation. This strategy is called *backpropagation through time (BPTT)*

Just like in regular backpropagation, there is a first forward pass through the unrolled network; then the output seq is evaluated using a cost func and the gradients of that cost function are propagated backward through the unrolled network; and finally the model parameters are updated using the gradients computed BPTT. NOTE that gradient flows backward through all the outputs used by the cost function, not just through the final output.


### Difficulty of Training over Many Times Steps:
To train RNN on long seq, it has to run over many time steps, making unrolled RNN a very deep n/w. Just like any deep model, it suffers from the vanishing/ exploding gradients problem and take forever to train.

We can use different ways to speed up training (and reaching a better solution):

    Applying a good intialization strategy for connection weights
    Use a good activation function (ReLu, ELU)
    Using Batch Normalization
    Reusing parts of a pretrained network
    Faster optimization technique (Adam)
    Using better Regularization techniques (Dropout)

But, if RNN needs to handle even moderately long seq (say 100 inputs), then training will still be very slow. So, here are two approaches that you use:

**Problem 1: Long Training Time:**
The simples and most common solution to this problem is to unroll the RNN only over limited number of time steps during training. This is called truncated backpropagation through time.

The problem, of course is that the model will not be able to learn long-term patterns. One workaround could be to make sure that these shortened sequences contain both quality data (old/new etc), so that model learns important patterns/ properties from whatever data is feeded. But this workaround has limits: what is data doesn't capture important info?

**Problem 2: Memory Fades Away:**
Input/data goes through transformations as it transverse through an RNN and some imformation is lost at each time step. After a while, the RNNs state contains virtually no trace of the first/ intial inputs.

For eg: Sentiment Analysis: Say you want to perform sentiment analysis on a long movie review that starts with these 4 letters,"I loved this movie" but the rest of the review lists the many things that could have made the movie even better. If the RNN gradually forgets the first four words, it will completely misinterpret the review.

To solve this problem, we should have a memory element/ cell in our model which is capable of storing memory even 1000s time step back. This is what LSTMs and GRUs is all about.
















