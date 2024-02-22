import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from linearFunction import LinearFunction


def showDataFrame(df: pd.DataFrame, lfunc: LinearFunction = None):

    price = df.loc[:, "price"]
    km = df.loc[:, "km"]
    plt.figure(figsize=(13, 10))
    plt.plot(km, price, "bo", markersize=15)

    if lfunc is not None:
        m = lfunc.m
        b = lfunc.b
        plt.plot(
            km,
            m * km + b,
            "r",
            linestyle="-",
            linewidth=4,
        )

    plt.title(
        "Price of cars according to mileage",
        fontsize=15,
    )
    plt.xlabel("Mileage (km)", fontsize=15)
    plt.ylabel("Price ($)", fontsize=15)
    plt.xticks(
        range(
            10000,
            math.ceil(km.max() / 100000) * 100000,
            40000,
        ),
        fontsize=15,
    )
    plt.yticks(
        range(
            math.floor(price.min() / 1000) * 1000,
            math.ceil(price.max() / 1000) * 1000,
            500,
        ),
        fontsize=15,
    )
    plt.show()