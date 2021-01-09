from perceptron import Perceptron
from char_board import CharBorad
from load_from_folder import LoadAndSaveData

data_set = []


def on_submit(inputs, x):
    data_set.append({'inputs': inputs, 'result': x})


def get_char_name(number):
    if number == -1:
        return 'O'
    elif number == 1:
        return 'X'
    else:
        return 'undefined'


if __name__ == "__main__":
    perceptronNeuron = Perceptron(5*5, 0.1, 0.01)  # initialize neuron
    storage = LoadAndSaveData('./single_data_set')

    # if you want to load from data set just comment this section
    train_board = CharBorad(5, 5, on_submit, True)  # initialize char board
    while train_board.is_open:
        train_board.start()
    # storage.save_data_set() # save your input data

    # if you want to load from data set just uncomment this section
    # data_set = storage.load_data_set()

    perceptronNeuron.train_all(data_set)

    print(perceptronNeuron.weights)

    board = CharBorad(5, 5,
                      lambda inputs, x: print(get_char_name(perceptronNeuron.calculate_one(inputs))), False)  # initialize char board
    while board.is_open:
        board.start()
