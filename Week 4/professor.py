import random


def main():
    level = get_level()
    score = 0

    try:
        for _ in range(10):
            x = generate_integer(level)
            y = generate_integer(level)
            answer = x + y
            fail_count = 0


            while True:
                try:
                    user_guess = int(input(f"{x} + {y} = "))
                except ValueError:
                    fail_count += 1

                    if fail_count == 3:
                        print(f"{x} + {y} = {answer}")
                        break
                    else:
                        print("EEE")
                        continue
                    
                
                if user_guess == answer:
                    score += 1
                    break
                else:
                    fail_count += 1

                    if fail_count == 3:
                        print(f"{x} + {y} = {answer}")
                        break
                    else:
                        print("EEE")

        print(f"Score:{score}")
                        

    except ValueError:
        pass

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0 and n < 4:
                return n

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num = random.randint(0,9)

    elif level == 2:
        num = random.randint(10,99)

    elif level == 3:
        num = random.randint(100,999)
    else:
        raise ValueError

    return num



if __name__ == "__main__":
    main()