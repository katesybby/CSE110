import random
print ("""WELCOME TO WORDLE 2.0!
--------------------------------------------------------------------------------------------
GAME RULES:
1. Upper-case letter => right letter + right spot 
2. Lower-case letter => right letter + wrong spot
3. A "_" => letter is not in the hidden word
4. Make sure your guess is 5 letters before pressing enter
--------------------------------------------------------------------------------------------""")
list = ("plant", "woman", "disco", "macho", "party", "slump", "dance", "ramen", "bread", "cause", "screw", "await", "rural", "ghost")

word = random.choice(list)
keep_playing = "yes"

while keep_playing == "yes":
    word = random.choice(list)
    attempt = 0     
    guess = " "
    hint = " "

    while guess != word:
        guess = input("Input your guess: ")
        attempt += 1 
      
        for i in range (len(guess)):
            if guess[i] == word[i]:
                hint+=guess[i].upper() + " "
            elif guess[i] in word:
                hint+=guess[i].lower() + " "
            else:
                hint += " _ "

        print (f"Your hint is: {hint}")
        hint = " "

        # if len(guess) != 5:
        #     print('Please enter a 5-letter word!')
        #     keep_playing = input("Do you wanna play again (yes/no)?  ")

        if guess == word:
            print (f"You've won! The word was {word}")
            print (f"It took you {attempt} attempt(s)")
            keep_playing = input("Do you wanna play again (yes/no)?  ")
            if keep_playing == "no":
                print ("Goodbye!")