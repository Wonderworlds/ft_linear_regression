import numpy as np
import pandas as pd
from bonus import showDataFrame
from linearFunction import LinearFunction
import time


class MLgradientDescent:
    """class containing the model and the methods to train and use it."""

    theta0: np.float64 = 0
    theta1: np.float64 = 0

    def __init__(self, path="./data/model.csv") -> None:
        """Initializes the class."""
        self.path = path

    def save_model(self):
        """Saves the model to a csv file."""
        df = pd.DataFrame(
            {
                "key": ["theta0", "theta1"],
                "value": [self.theta0, self.theta1],
            }
        )
        df.to_csv(self.path, index=False, sep=",")

    def load_model(self):
        """Loads the model from a csv file."""
        if (self.theta0 != 0) and (self.theta1 != 0):
            return
        try:
            df = pd.read_csv(self.path, index_col=0)
            self.theta0 = df.loc["theta0", "value"]
            self.theta1 = df.loc["theta1", "value"]
        except FileNotFoundError:
            print("Model not found")

    def estimate_price(self, km: float) -> np.float64:
        """Estimates the price of a car given its mileage.

        uses the current theta0 and theta1 to estimate the price.
        """
        return self.theta0 + self.theta1 * km

    def gradient_descent(self, km, price, lr):
        """Performs a gradient descent to update theta0 and theta1."""
        m = len(km)
        tmp_theta0 = lr * (1 / m) * np.sum(self.estimate_price(km) - price)
        tmp_theta1 = lr * (1 / m) *\
            np.sum((self.estimate_price(km) - price) * km)
        return [tmp_theta0, tmp_theta1]

    def train_model(self, df: pd.DataFrame):
        """Trains the model using the gradient descent algorithm."""
        print("Training model...")
        tic = time.perf_counter()
        lr = 0.001
        num_iterations = 100000
        km = np.asarray(df.loc[:, "km"], np.float64) / 10000
        price = np.asarray(df.loc[:, "price"], np.float64) / 10000
        for _ in range(num_iterations):
            tmp = self.gradient_descent(km, price, lr)
            self.theta0 -= tmp[0]
            self.theta1 -= tmp[1]
        self.theta0 *= 10000
        print(f"training time: {time.perf_counter() - tic:0.4f} seconds")
        self.accuracy_model(df)
        self.save_model()

    def resolveRMSE(self, df: pd.DataFrame):
        """Calculates the Mean Squared Error of the model."""
        km = np.asarray(df.loc[:, "km"], np.float64)
        price = np.asarray(df.loc[:, "price"], np.float64)
        rmse = ((1 / len(km)) *
                np.sum((self.estimate_price(km) - price) ** 2)) ** 0.5
        return rmse

    def resolveMeanLinearFunc(self, df: pd.DataFrame):
        """Calculate the mean linear function from the dataset"""
        km = np.asarray(df.loc[:, "km"], np.float64)
        price = np.asarray(df.loc[:, "price"], np.float64)
        x_mean = np.mean(km)
        y_mean = np.mean(price)

        # Calculate slope (m) and y-intercept (b) of the regression line
        m = np.sum((km - x_mean) * (price - y_mean)) / np.sum((km - x_mean)**2)
        b = y_mean - m * x_mean
        return LinearFunction(m, b)

    def accuracy_model(self, df: pd.DataFrame):
        """print accuracy information"""

        m_lfunc = self.resolveMeanLinearFunc(df)
        rmse = self.resolveRMSE(df)
        print("\nAccuracy Info:\n")
        print(f"My model: y = {self.theta1} * km + {self.theta0}")
        print(f"mean Lfunc: y = {m_lfunc.m} * km + {m_lfunc.b}")
        print(f"Root Mean Squared Error: {rmse}")
        print(f"diff:\tm: {abs(abs(m_lfunc.m) - abs(self.theta1)) * 100} %\
\n\tb: {abs(abs(m_lfunc.b) - abs(self.theta0)) * 100} %")

    def show_model(self, df: pd.DataFrame):
        """Shows the model and the data in a graph."""
        showDataFrame(df, LinearFunction(self.theta1, self.theta0))
