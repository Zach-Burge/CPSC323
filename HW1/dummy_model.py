class DummyModel:
    def __init__(self):
        self.model_const = None

    def fit(self, input, classes):
        self.model_const = max(set(classes), key=classes.count)

    def predict(self, test_input):
        predictions = []
        for val in test_input:
            predictions.append(self.model_const)
        return predictions
    