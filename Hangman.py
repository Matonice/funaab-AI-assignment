from random import randint
def hangman():
    print("welcome to this hagman game")

    choose_level = input("Choose a level between beginners/intermediate/master: ")

    if choose_level == "beginners":
        random_number = randint(1, 50)
        print("I CHOOSE A NUMBER BETWEEN 1 AND 50, GUESS RIGHT MY NUMBER")
    elif choose_level == "intermediate":
        random_number = randint(1, 100)
        print("I CHOOSE A NUMBER BETWEEN 1 AND 100, GUESS RIGHT MY NUMBER")
    elif choose_level == "master":
        random_number = randint(1, 200)
        print("I CHOOSE A NUMBER BETWEEN 1 AND 200, GUESS RIGHT MY NUMBER")
    else:
        print("invalid input")
        return


    guess_limit = 0
    user_guess = ""
    print("You have 7 trials to get the correct number")
    while user_guess != random_number and guess_limit < 7:
        guess_limit += 1

        while True:
            if guess_limit > 1:
                user_guess = input("Enter another guess: ")
            else:
                user_guess = int(input("Enter your guess: "))

            try:
                int(user_guess)
                guess_left = 7 - int(guess_limit)
                if int(user_guess) <0:
                    print("input cannot be less than zero")
                    print(f"\n you have {guess_left} guess left")
                if int(user_guess) > random_number:
                    print('Your guess is higher than my number')
                    print(f"\n you have {guess_left} guess left")
                elif int(user_guess) < random_number and int(user_guess) >0:
                    print('your guess is lower than my number ')
                    print(f"\n you have {guess_left} guess left")
                elif int(user_guess) == random_number and guess_limit < 7:
                    print("You win")
                elif int(user_guess)!= random_number and guess_limit == 7:
                    print("you lost")
                    print(f"The number you are trying to guess is {random_number}")
                break
            except:
                print("invalid input, input should be an integer")
                continue

hangman()
