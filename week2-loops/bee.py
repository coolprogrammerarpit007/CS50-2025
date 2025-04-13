words = {
    "PAIR" : 4,
    "HAIR":4,
    "CHAIR":5,
    "GRAPHIC":7
}

def main():
    user_score = 0
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C H R G")

    while len(words) > 0:
        print(f"{len(words)} are left!")
        guess = input("Guess a word: ").upper().strip()


        # TODO:- Check if guess is in dictionary
        if guess == "GRAPHIC":
            print(f"Brilliant job you have guessed the super word and you scored {words[guess]} points.")
            user_score += words[guess]
            words.clear()
        if guess in words.keys():
            user_score += words[guess]
            print(f"Good job! you scored {words[guess]} points....")
            words.pop(guess)   # to remove a key from dict


    print("That's the game!")
    print(f"You Scored: {user_score} points.")


if __name__ == "__main__":
    main()