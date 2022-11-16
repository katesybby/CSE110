import random
playing = "y"

while playing == "y":
    number = random.randint(1, 100)

    count = 0
    guess = -1

    while guess != number:
        guess = int(input("what is your guess? "))
        count = count + 1

        if guess < number:
            print("higher")
        elif guess > number:
            print("lower")
        else:
            print("you guessed it!")

    print (f"it took you {count} guesses")
    playing = input("play again (y/n)? ")

print ("thanks for playing! ")