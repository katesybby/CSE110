#ADVENTURE GAME
print("-------------------------------------------------------------------------------")
print("WELCOME TO THE GAME OF THE CENTURY!")
print("-------------------------------------------------------------------------------")
print("good luck traveler!")
print( )

doors = input("You're walking, and you come upon two doors. One is made of candy and the other is plain except for a teeny tiny sign on it that says: 'beware'. Which door will you choose? CANDY or PLAIN? ")
print( )

#candy door
if doors == "candy":
    candy = input("You cautiously turn the lollipop handle and pull the door open. The door opens to an enormous world made entirely of candy. You immediately run in. As you are admiring the candy world, you cluelessly walk into a trap. Suddenly you're hanging upside down from a licorice tree. Do you try to ESCAPE or CALL FOR HELP? ")
    print( )

    if candy == "escape": 
        escape = input("You reach up in an attempt to untie the licorice vine entrapping you and a giant chocolate squirrel skitters down the rope and begins to chew it. In minutes you are back on the ground. You want to thank the squirel for saving you. Will you TAKE HIM with you on your journey or HELP him rebuild his roof? ")
        print( )

        if escape == "take him":
                print ("The chocolate squirrel graciously accepts your offer of companionship and you both stroll down the red brick road into the sunrise. ")
                print ("BRAVO! YOU'VE GAINED A NEW COMPANION! YOU'VE STILL LOST THO. START OVER. ")

        if escape == "help":
                print ("He thanks you and leads you back to his house. After a long hike, you finally arrive at Mr. squirrels house. He asks you to start by cleaning the oven. You gleefully oblige as you climb into the surprisingly large appliance. Suddenly, Mr.Squirrel slams the oven door closed and eats you for dinner. ")
                print ("DEAD. TRY AGAIN!")
    
    if candy == "call for help":
        call = input("You scream help at the top of your lungs. No response. A faint marching sound begins to echo through the licocice forest and 23 seconds later a giant army of skittle people appear and they begin worshiping you. Will you become their LEADER, LEAVE them, or ?  ")
        print( )

        if call == "leader":
                print ("You are now the ruler of the skittle people. You live a life of immense luxury. You are a God among skittles. ")
                print ("CONGRATULATIONS! YOU'VE WON")
        if call == "leave":
                print ("You turn your back on the skittle people and hours later you are squished by a skittle rainbow. ")
                print ("YOU'RE DEAD. DUMMY, YOU COULD HAVE BEEN KING.")


#plain door
if doors == "plain":
    plain = input("You cautiously turn the cold metal handle and pull the door open. The door opens to complete darkness. You reach for your back pocket to pull out your phone to use the flashlight, but your pocket is empty. Will you continue to SEARCH your pockets, or will you GO IN BLIND? ")
    print( )

    if plain == "search": 
        follow = input("You pat each of your pockets down, quickly discovering your entire outfit is covered in pockets. Your fingers feel a warm slimy substance in the depths of your third breast pocket. You slowly remove your fingers from your pockets, tears streaming down your cheeks. Will you LICK the substance or LEAVE YOUR HAND in your pocket forever? ")
        print( )
        
        if follow == "lick":
                print ("You stick your fingers in your mouth. A tingling sensation immidiately engulfs your mouth in flames. You swallow, hoping it will reduce the pain. It doesn't. You scream out like a little girl. All of the sudden, the pain evaporates.")
                print ("CONGRATULATIONS! YOU HAVE SUPER POWERS NOW!")
        if follow == "leave your hand":
                print ("You slide your hand back into your pocket, believing if you cannot see the problem it will cease to exist. You are wrong. The liquid begins to get hotter and hotter until it has melted its way through your pocket and onto your skin.")
                print ("YOU HAVE UNLOCKED CANCER. GAME OVER ")
    
    if plain == "go in blind":
        go = input("You wave your feet and hands in front of yourself, hoping to protect yourself from any oncoming obstacles. Suddenly your foot smacks against something on the floor. Will you CONTINUE or INVESTIGATE? ")
        print( )
        
        if go == "continue":
                print ("As you go deeper and deeper into the room, you begin to hear a soft beeping coming from somewhere in front of you. You continue to slowly walk forward as the beeping grows louder and faster. Abruptly, the beeping stops. BOOOOOOOM! ")
                print ("YOU HAVE DIED. GAME OVER")
        if go == "investigate":
                print ("You pick up the object and return to the light of the room you began in. Once you return to the light, you are able to see that the object is an enourmous diamond!")
                print ("CONGRATULATIONS! YOU'RE RICH!")