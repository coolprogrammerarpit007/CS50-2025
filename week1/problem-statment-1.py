from idlelib.replace import replace


#  Problem-Statment 1
# word = input("").lower()
# print(word)

# Problem Statment-2

# word = input("Enter words: ")
# print(word.replace(" ","..."))

 # Problem Statment 3

# def convert(str):
#     updated_str = ""
#     updated_str = str.replace(":)","🙂").replace(":(","🙁")
#     return updated_str
#
# text = input("Enter message: ")
# def main():
#     print(convert(text))
#
#
# if __name__ == "__main__":
#     main()

# Problem 4
# mass = int(input("Enter mass: "))
# Speed_Of_Light = 300000000
# energy = mass * Speed_Of_Light * Speed_Of_Light
# print(f"E: {energy}")


# Problem 5:- Tip Calculator

def dollars_to_float(amount):
    amount = float(amount.replace("$",""))
    return amount

def percent_to_float(percent):
    percent_number = float(percent.replace("%",""))
    return  percent_number

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip?"))
    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()

