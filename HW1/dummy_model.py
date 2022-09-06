class DummyModel:
    """This is a dummy classifier that makes predictions based only on what the most frequent class label is in the dataset
    
    Attributes:
        model_const: This is the most frequent class label which then becomes the prediction for every instance in the dataset
    """
    def __init__(self):
        self.model_const = None

    def fit(self, input, classes):
        """Fits the dummy model 
        
        input: This is the input data that the model would train on, but since it simply chooses the most frequent label, it ignores this training data
        classes: This is the list of class labels that the model uses to find the most frequent class label
        """
        self.model_const = max(set(classes), key=classes.count)

    def predict(self, test_input):
        """Makes predictions for each instance in the dataset
        
        test_input: The data of the table, which is processed and then ignored
        """

        predictions = []
        for val in test_input:
            predictions.append(self.model_const)
        return predictions
    