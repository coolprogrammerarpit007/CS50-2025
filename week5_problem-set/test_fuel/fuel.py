import sys


def main():
    while True:
        fraction = input("Fractions: ")
        percentage = convert(fraction)
        if percentage is not None:
            return gauge(percentage)

        continue


def convert(fraction):
    try:
        number1, number2 = fraction.split("/")
        frac1 = int(number1)
        frac2 = int(number2)

        if frac2 == 0:
            raise ZeroDivisionError

        if frac1 > frac2:
            raise ValueError

        percentage = (frac1 / frac2) * 100

        return int(round(percentage))

    except ValueError:
        raise ValueError


    except ZeroDivisionError:
        raise ZeroDivisionError




def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    else:
        return f"{(int(round(percentage)))}%"



if __name__ == "__main__":
    print(main())


