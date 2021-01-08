class Perceptron:
    def __init__(self, n, theta, alpha):
        self.theta = theta
        self.aplpha = alpha
        self.n = n
        self.biace = 0
        self.weights = [0 for i in range(n)]

    def active_function(self, nIC):
        """
            active function
        """
        if (nIC > self.theta):
            return 1
        elif (-self.theta <= nIC <= +self.theta):
            return 0
        else:
            return -1

    def calculate_one(self, inputs):
        result = 0
        for i in range(len(self.weights)):
            result += self.weights[i] * inputs[i]

        result += self.biace
        return self.active_function(result)

    def new_weight(self, old, x, result):
        return old + x * self.aplpha * result

    def train_one(self, inputs, result):
        # Step.7
        if (self.calculate_one(inputs) == result):
            return True

        for i in range(len(inputs)):
            self.weights[i] = self.new_weight(
                self.weights[i], inputs[i], result)

        self.biace = self.new_weight(self.biace, 1, result)
        return False

    def train_all(self, cases):
        for case in cases:
            if (self.train_one(case['inputs'], case['result'])):
                break

    def get_weights(self):
        return self.weights

    def get_biace(self):
        return self.biace
