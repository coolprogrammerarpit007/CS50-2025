# score = int(input("Enter Marks Score b/w 1 and 100 "))
#
# if 90 <= score <= 100:
#     print("Grade A")
# elif 80 <= score < 90:
#     print("Grade B")
# elif 70 <= score < 80:
#     print("Grade C")
# elif 60 <= score < 70:
#     print("Grade D")
# else:
#     print("Grade F")
def is_even(number):
    return True if number % 2 == 0 else False

def main():
    number = int(input("Enter Number: "))
    if is_even(number):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()