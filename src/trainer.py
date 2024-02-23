import numpy as np
import pandas as pd
from load_csv import load_csv
from bonus import showDataFrame
from linearFunction import LinearFunction


def estimate_price(km, theta0, theta1):
    return theta0 + theta1 * km


def train_linear_function(km, price, theta0, theta1, lr):
    m = len(km)
    tmp_theta0 = lr * (1 / m) * np.sum(estimate_price(km, theta0, theta1) - price)
    tmp_theta1 = (
        lr * (1 / m) * np.sum((estimate_price(km, theta0, theta1) - price) * km)
    )
    return [tmp_theta0, tmp_theta1]


theta0: np.float64 = 0
theta1: np.float64 = 0
lr = 0.001
num_iterations = 100000

df = load_csv("../data/data.csv")
km = np.asarray(df.loc[:, "km"], np.float64) / 10000
price = np.asarray(df.loc[:, "price"], np.float64) / 10000
print("km", km)
print("price", price)
for _ in range(num_iterations):
    tmp = train_linear_function(km, price, theta0, theta1, lr)
    theta0 -= tmp[0]
    theta1 -= tmp[1]

print("theta0", theta0 * 10000)
print("theta1", theta1)
# km *= 10000
# price *= 10000
# theta1 = (price.max() - price.min()) * (theta1 * 10000) / (km.max() - km.min())
# theta0 = price.min() + ((price.max() - price.min()) * theta0) + theta1 * (1 - km.min())
# print("theta0", theta0)
# print("theta1", theta1)
showDataFrame(df, LinearFunction(theta1, theta0 * 10000))
