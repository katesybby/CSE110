import random
print ("""WELCOME TO WORDLE 2.0!
--------------------------------------------------------------------------------------------
GAME RULES:
1. Upper-case letter => right letter + right spot 
2. Lower-case letter => right letter + wrong spot
3. A "_" => letter is not in the hidden word
--------------------------------------------------------------------------------------------""")
list = ("plant", "woman", "disco", "lover", "party")

word = random.choice(list)
keep_playing = "yes"

while keep_playing == "yes":
    word = random.choice(list)
    attempt = 0 #10    
    guess = " "
    hint = " "
    while guess != word:  #or attempt > 0:
        attempt += 1 #-= 1
        guess = input("Input your guess: ")
        if len(guess) != 5:
            print('Please enter a 5-letter word!')
        # if attempt > 10:
        #     print("GAME OVER")
        for i in range (len(guess)):
            if guess[i] in word:
                hint += guess[i].upper() + " "
            elif guess[i] in word:
                hint += guess[i].lower() + " "
            else:
                hint += " _ "
        print (f"Your hint is: {hint}")
        # print(f"You have {attempt} attempt(s) remaining")
        hint = " "
    print (f"It took you {attempt} attempt(s)")
    keep_playing = input("Do you wanna play again (yes/no)?  ")
    if keep_playing == "no":
        print ("Goodbye!")