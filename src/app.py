from load_csv import load_csv
from trainer import MLgradientDescent
import os


def validInput() -> float:
    """Validates the input for the mileage."""
    try:
        mil = float(input("Enter the mileage (km): "))
        if mil != mil or mil < 0:
            print("Invalid input. Please enter a positive number.")
            return validInput()
        return mil
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return validInput()


def programChoice() -> int:
    """main menu for the program."""
    try:
        choice = int(
            input(
                "\nEnter\t1 to estimate a price,\n\
\t2 to train the model, \n\
\t3 to visualize the data.\n\
\t0 to exit the program: "
            )
        )
        if choice != 1 and choice != 2 and choice != 3 and choice != 0:
            print("Invalid input. Please enter 1, 2, 3 or 0.")
            return programChoice()
        return choice
    except ValueError:
        print("Invalid input. Please enter 1, 2, 3 or 0.")
        return programChoice()


def main():
    """main function for the program."""
    os.system("clear")
    try:
        trainer = MLgradientDescent()
        df = load_csv("data/data.csv")
        choice = 1
        while choice:
            choice = programChoice()
            if choice == 1:
                mil = validInput()
                trainer.load_model()
                estimated_price = trainer.estimate_price(mil)
                print("Estimated price:",
                      estimated_price if estimated_price > 0 else 0)
            elif choice == 2:
                trainer.train_model(df)
                trainer.show_model(df)
            elif choice == 3:
                trainer.load_model()
                trainer.show_model(df)
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    main()
