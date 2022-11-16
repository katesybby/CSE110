quote = ""
run_again = "y"

while run_again == "y":
    user_numb = int(input("please input number: "))

    for i, letter in enumerate(quote):
        if i % user_numb == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    print()

    run_again = input("wanna enter another number? ")
    
print ("goodbye!")
