import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break

    except ValueError:
        pass

gen_int = random.randint(1,n)

while True:
    try:
        user_guess = int(input("Guess: "))
        
        if user_guess < gen_int:
            print("Too small!")
        elif user_guess > gen_int:
            print("Too large")
        else:
            print("Just right!")

        break

    except ValueError:
        pass

