import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionGD:
    """This my implementation of Linear Regression using Gradient Descent"""

    def __init__(self, learning_rate, n_iters):
        self.learning_rate = learning_rate
        self.n_iters = n_iters

    def fit(self, x: np.array, y: np.array):
        """This function uses Gradient Descend to find the weight(w, or theta_1) and the bias(y_intercept, or theta_0) and prints them according to a certain number of iterations and alpha(learning rate)



        Args:
            x: The x-axis data points
            y: The actual values of y

        Returns:
            The best-fit weight and bias
        """
        x = x[:, np.newaxis] if x.ndim == 1 else x
        sse = []
        w = np.zeros(x.shape[1])
        b = 0
        for _ in range(self.n_iters):
            w_derivative = (2 / len(y)) * (x.T @ ((x @ w) + b - y))
            b_derivative = (2 / len(y)) * (((x @ w) + b - y)).sum()
            w = w - self.learning_rate * w_derivative
            b = b - self.learning_rate * b_derivative
            sse.append(((((x @ w) + b) - y) ** 2).sum())
        return (w, b, sse)

    def predict(self, x, w, b):
        x = x[:, np.newaxis] if x.ndim == 1 else x
        return (x @ w) + b

    def calculate_mse(self, sse, y):
        return sse / y.size

    def normalize(self, x):
        return (x - x.min(axis = 0)) / (x.max(axis = 0) - x.min(axis = 0))

    def plot_training(
        self, sse, iterations, x, y, y_predicted, xscale=None, yscale=None
    ):
        plt.figure(figsize=(5, 5))

        plt.subplot(1, 2, 1)
        plt.plot(
            iterations,
            sse,
            marker="*",
            linestyle="-",
            color="red",
            markerfacecolor="blue",
            markeredgecolor="black",
            label="Sum of Squared Residuls",
        )
        plt.xticks(iterations[::9])
        plt.xlabel("Iterations")
        plt.ylabel("Sum of Squared Residuals")
        plt.title("Minimizing the Sum of Squared Residuals")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.scatter(x, y, label="Data")
        plt.plot(x, y_predicted, color="red", label="Best-fit Line")
        plt.xticks(x)
        plt.yticks(y)
        plt.xlabel("Area of the House")
        plt.ylabel("Price in Thousands")
        plt.title("Houses and best fit line")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def fit_ridge(self, x: np.array, y: np.array, lambda_param = 0.1):
        """This function uses Gradient Descend to find the weight(w, or theta_1) and the bias(y_intercept, or theta_0) and prints them according to a certain number of iterations and alpha(learning rate)



        Args:
            x: The x-axis data points
            y: The actual values of y

        Returns:
            The best-fit weight and bias
        """
        x = x[:, np.newaxis] if x.ndim == 1 else x
        w = np.zeros(x.shape[1])
        b = 0
        for _ in range(self.n_iters):
            w_derivative = (2 / len(y)) * (x.T @ ((x @ w) + b - y)) + (lambda_param * w)
            b_derivative = (2 / len(y)) * (((x @ w) + b - y)).sum()
            w = w - self.learning_rate * w_derivative
            b = b - self.learning_rate * b_derivative
        return (w, b)