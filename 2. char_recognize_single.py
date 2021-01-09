from perceptron import Perceptron
from char_board import CharBorad

data_set = []


def on_submit(raw_inputs, x):
    final_inputs = []
    for row in raw_inputs:
        final_inputs.extend([1 if item else -1 for item in row])

    data_set.append({'inputs': final_inputs, 'result': x})


if __name__ == "__main__":
    perceptronNeuron = Perceptron(5*5, 0.1, 0.1)  # initialize neuron
    train_board = CharBorad(5, 5, on_submit, True)  # initialize char board

    while train_board.is_open:
        train_board.start()

    perceptronNeuron.train_all(data_set)
    board = CharBorad(5, 5, on_submit, False)  # initialize char board
    board.start()
