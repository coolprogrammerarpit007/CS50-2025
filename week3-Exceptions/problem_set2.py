
while True:
    fraction = input("Fractions: ")
    try:
        number1 , number2 = fraction.split("/")
        frac1 = int(number1)
        frac2 = int(number2)
        if frac1 > frac2:
            continue
        percentage = (frac1/frac2) * 100

    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    else:
        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E")
        else:
            print(f"{int(percentage)}%")
        break
