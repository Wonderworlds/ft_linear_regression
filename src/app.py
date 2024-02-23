from load_csv import load_csv
from bonus import showDataFrame
import sys


def validInput() -> float:
    try:
        mil = float(input("Enter the mileage (km): "))
        if mil != mil:
            print("Invalid input. Please enter a number.")
            return validInput()
        return mil
    except ValueError:
        print("Invalid input. Please enter a number.")
        return validInput()


def main():
    # mil = validInput()
    df = load_csv("data/data.csv")
    showDataFrame(df)


if __name__ == "__main__":
    main()
