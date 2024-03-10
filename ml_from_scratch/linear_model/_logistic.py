import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None
        self.loss = None

    def sigmoid(self, z): 
        return 1 / (1 + np.exp(-z))
    
    def log_loss(self, y, y_hat):
        epsilon = 1e-15
        y_hat = np.clip(y_hat, epsilon, 1 - epsilon)
        loss = -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        return loss

    def fit(self, X, y):
        # initialize weights and bias
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        # gradien descent (optimization)
        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_hat = self.sigmoid(linear_model)

            # gradient calculation
            dw = (1 / num_samples) * np.dot(X.T, (y_hat - y))
            db = (1 / num_samples) * np.sum(y_hat - y)

            # parameter update
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
        self.loss = self.log_loss(y, y_hat)

    def predict_proba(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        proba = self.predict_proba(X)
        return (proba >= threshold).astype(int)
