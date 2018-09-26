class NeuralNetwork(object):

    def __init__(self, x, y, num_layers=2):
        self.input = x
        self.y = y
        self.output = np.zeros(y.shape)
        for layer in num_layers:
            self.weight

    def train(self):
        raise NotImplementedError

    def backpropagate(self):
        raise NotImplementedError
