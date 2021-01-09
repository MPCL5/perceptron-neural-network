from perceptron import Perceptron
from char_board import CharBorad

# initialize neurons
perceptron_neuron_x = Perceptron(5*5, 0.1, 0.1)
perceptron_neuron_o = Perceptron(5*5, 0.1, 0.1)


def on_submit(raw_inputs, x):
    final_inputs = []
    for row in raw_inputs:
        final_inputs.extend([1 if item else -1 for item in row])

    if x == -1:
        perceptron_neuron_x.__train_one(final_inputs, 1)
        perceptron_neuron_o.__train_one(final_inputs, -1)
    elif x == 1:
        perceptron_neuron_x.__train_one(final_inputs, -1)
        perceptron_neuron_o.__train_one(final_inputs, 1)


# initialize char board
board = CharBorad(5, 5, on_submit, True)

if __name__ == "__main__":
    while board.is_open:
        board.start()
