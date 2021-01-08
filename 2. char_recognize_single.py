from perceptron import Perceptron
from char_board import CharBorad

# initialize neuron
perceptronNeuron = Perceptron(5*5, 0.1, 0.1)


def on_submit(raw_inputs, x):
    final_inputs = []
    for row in raw_inputs:
        final_inputs.extend([1 if item else -1 for item in row])

    print(str(final_inputs) + ' ' + str(x))
    perceptronNeuron.train_one(final_inputs, x)
    print(str(perceptronNeuron.weights) + ' ' + str(perceptronNeuron.biace))


# initialize char board
board = CharBorad(5, 5, on_submit, True)

if __name__ == "__main__":

    while board.is_open:
        board.start()
