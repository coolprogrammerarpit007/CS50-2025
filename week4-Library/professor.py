import random
import sys


def main():
    get_level()


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isdigit() and level == '1' or level == '2' or level == '3':
                return generate_integer(int(level))

        except ValueError:
            continue


def generate_random_integer(num1, num2):
    rand_number = random.randint(num1, num2)
    return rand_number


def generate_integer(level):
    start_point = None
    end_point = None
    user_score = 0
    wrong_answer = False
    wrong_attempts = 0
    hold_values = []
    index = 0
    if level == 1:
        start_point = 1
        end_point = 9

    elif level == 2:
        start_point = 10
        end_point = 99

    else:
        start_point = 100
        end_point = 999

    while index < 10:
        if not wrong_answer:
            wrong_attempts = 0
            number1 = generate_random_integer(start_point,end_point)
            number2 = generate_random_integer(start_point,end_point)
            hold_values.append(number1)
            hold_values.append(number2)

        try:
            if wrong_attempts != 3:
                answer = int(input(f"{hold_values[0]} + {hold_values[1]} = "))

                if answer == (hold_values[0] + hold_values[1]):
                    user_score += 1
                    index += 1
                    hold_values.clear()
                    continue
                else:
                    wrong_answer = True
                    wrong_attempts += 1
                    continue

            else:
                index += 1
                print(f"{hold_values[0]} + {hold_values[1]} = {hold_values[0] + hold_values[1]} ")
                hold_values.clear()
                wrong_answer = False
                continue




        except ValueError:
            wrong_attempts += 1
            wrong_answer = True
            continue

    print(f"Score: {user_score} ")



if __name__ == "__main__":
    main()