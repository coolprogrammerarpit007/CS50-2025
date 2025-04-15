import sys

# while True:
#     fraction = input("Fractions: ")
#     try:
#         number1 , number2 = fraction.split("/")
#         frac1 = int(number1)
#         frac2 = int(number2)
#         if frac1 > frac2:
#             continue
#         percentage = (frac1/frac2) * 100
#
#     except ValueError:
#         pass
#     except ZeroDivisionError:
#         pass
#
#     else:
#         if percentage >= 99:
#             print("F")
#         elif percentage <= 1:
#             print("E")
#         else:
#             print(f"{int(percentage)}%")
#         break



#  Problem 2

menus = {
"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0
while True:
    new_str = ""
    try:
        items = input("Item: ").strip()
        list_words = [word[0].capitalize() + word[1:] for word in items.split(" ")]
        new_str = " ".join(list_words)
        total_price += menus[new_str]


    except KeyError:
        pass
    except EOFError:
        sys.exit(0)

    else:
        print(f"Total: ${total_price:.2f}")





