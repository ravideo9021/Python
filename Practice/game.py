

def takeInput():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except:
            pass

def guessTheNumber():
    n = takeInput()

    num = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess > 0:
                if guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too large!")
                else:
                    print("Just right!")
                    return

        except:
            pass

if __name__ == "__main__":
    guessTheNumber()
