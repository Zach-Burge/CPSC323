import numpy as np
from sklearn.model_selection import train_test_split

class LinearRegressorModel:
    def __init__(self, slope=None, intercept=None):
        self.slope = slope
        self.intercept = intercept

    def fit(self, X_train, y_train):
        X_train = [x[0] for x in X_train]
        self.slope, self.intercept = self.compute_slope_intercept(X_train, y_train)

    def predict(self, X_test):
        predictions = []
        if self.slope is not None and self.intercept is not None:
            for test_instance in X_test:
                predictions.append(
                    self.slope * test_instance[0] + self.intercept)
        return predictions

    def compute_slope_intercept(self, x, y):
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        m = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))]) / sum([(x[i] - mean_x) ** 2 for i in range(len(x))])
        b = mean_y - m * mean_x
        return m, b
