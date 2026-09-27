import numpy as np

class MyPerceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.epochs = n_iterations
        self.w = None

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1] + 1)

        X_bias = np.insert(X, 0, 1, axis=1)

        for _ in range(self.epochs):
            for idx, x_i in enumerate(X_bias):
                linear_output = np.dot(x_i, self.w)
                y_pred = 1 if linear_output > 0 else -1

                if y[idx] != y_pred:
                    self.w += self.lr * y[idx] * x_i

    def predict(self, X):
        X_bias = np.insert(X, 0, 1, axis=1)
        linear_output = np.dot(X_bias, self.w)
        return np.where(linear_output > 0, 1, -1)