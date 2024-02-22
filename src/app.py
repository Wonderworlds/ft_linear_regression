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


def main(*args, **kwargs):
    mil = validInput()
    print("mil", mil)


if __name__ == "__main__":
    main()
