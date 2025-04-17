import random


def main():
    level = int(get_level())
    game_score = 0
    for i in range(0,10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        result =  num1 + num2
        # print(result)

        for index in range(0,3):
            answer = (input(f"{num1} + {num2} = "))
            if answer.isdigit():
                if result == int(answer):
                    game_score += 1
                    break
                if index == 2:
                    print(f"{num1} + {num2} = {result}")
                if result != int(answer):
                    print("EEE")
                    continue
            else:
                print("EEE")
                if index == 2:
                    print(f"{num1} + {num2} = {result}")
                continue

    print(f"Score: {game_score}")





def get_level():
    try:
        while True:
            level = input("Level: ")
            if (level == "1" or level == "2" or level == "3") and int(level) > 0:
                return level

            else:
                continue

    except ValueError:
        print("Invalid Value")






def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0,9)
        elif level == 2:
            return random.randint(10,99)
        elif level == 3:
            return random.randint(100,999)
        else:
            raise ValueError
    except ValueError:
        return -1


if __name__ == "__main__":
    main()
