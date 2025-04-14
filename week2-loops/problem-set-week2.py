# Week 2  Problem Set

# Problem 1
# camel case

# new_str = ""
# user_input = input("camelCase: ").strip()
# for char in user_input:
#     if char.isupper():
#         new_str = new_str + "_"
#     new_str += char.lower()
#
# print(f"snake_case:{new_str}")

# Problem 2
# coke machine

# amount_due = 50
# while amount_due > 0:
#     print(f"Amount Due: {amount_due}")
#     insert_amount = int(input("Insert Coin: "))
#     if insert_amount == 25 or insert_amount == 10 or insert_amount == 5:
#         amount_due -= insert_amount
#     else:
#         pass
#
# print(f"Change Owed: {abs(amount_due)}")


# problem 3

# twttr problem

# vowel_list = ('a','e','i','o','u')
# user_input = input("Input: ").strip()
# new_str = user_input.lower()
#
# for char in new_str:
#     if char in vowel_list:
#         user_input = user_input.replace(char,'')
#     else:
#         pass
#
# print(f"Output: {user_input}")

# Vanitty Plates


# Problem 4
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
#
# import sys
#
def is_valid(s):
    is_valid_plate = True
    digits = []

    # to check if plate starts with 2 letters and min of 2 and max of 6 chars.
    if 2 <= len(s) <= 6 and s[:2].isalpha():
        # to check if digit is in middle of char
        for index,letter in enumerate(s):
            if letter.isdigit():
                if  (index < len(s) - 1) and (letter[(index + 1)].isalpha()):
                    is_valid_plate = False
                if (index > 0 and (letter[index - 1]).isalpha()) and (index < len(s) - 1) and (letter[(index + 1)].isalpha()):
                    is_valid_plate = False
                else:
                    pass
            else:
                pass



    return is_valid_plate



main()

# Nutrition Problem 5

# calories = {
#     "apple":130,
#     "avocado":50,
#     "banana":110,
#     "cantaloupe":50,
#     "grapefruit":60,
#     "grapes":90,
#     "honeydew":50,
#     "kiwifruit":90,
#     "lemon":15,
#     "lime":20,
#     "nectarine":60,
#     "orange":80,
#     "peach":60,
#     "pear":100,
#     "pineapple":50,
#     "plums":70,
#     "strawberries":50,
#     "sweet cherries":100,
#     "tangerine":50,
#     "watermelon":80,
# }
#
#
# user_input = input("Item: ").lower()
# calory_value = calories.get(user_input,"")
#
# if calory_value != "":
#     print(f"Calories: {calory_value}")
# else:
#     pass
