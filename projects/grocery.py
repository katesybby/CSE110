print ("\n-----------------------------------------------------------------")
print ("Welcome to the Shopping Cart Program!")
print ("-----------------------------------------------------------------")
print ("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit """)
action = int(input("Please enter an action: "))

# word input instead of number fix 
# if action != ("1", "2", "3", "4", "5"): 
#     print ("number not listed, try again.")
#     action = int(input("Please enter an action: "))

items = []
prices = []
item = []
quit2 = []
quit3 = []
quit4 = []


instructions = ("""Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit """)

#-------------------------------------
#-------------------------------------
#ADD ITEM 
if action == 1:
    print("(Enter 'quit' to return to the options page)")
    while item != "quit":
        item = input("Item? ")
        if item != "quit":
            price = float(input("Price? "))
            items.append(item)
            prices.append(price)
            print (f"'{item}' has been added to the cart") 
        if item == 'quit':
            print()
            print (instructions)
            action = int(input("Please enter an action: "))

#-------------------------------------    
#VIEW CART 
elif action == 2:
    total = 0
    print("\nCart Contents:")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - ${prices[i]:.2}")
        # total += prices[i]
    # print("____________________")
    # print(f"Total: ${total:.2f}")
    quit2 = input("\nEnter 'quit' to return to options page: ")
    
    if item == 'quit':
        print()
        print (instructions)
        action = int(input("Please enter an action: "))

#-------------------------------------    
#REMOVE FROM CART *** 
elif action == 3:
    change = "yes"
    while change == "yes":
        change = input("\nDo you want to change an item (yes/no)? ")

        if change == "yes":
            print("Cart Contents:")
            for i in range(len(items)):
                print(f"{i+1}. {items[i]} - ${prices[i]:.2}")
            index = int(input("What number item do you want to update? "))

            #items.pop({index}) #error: can't be interpreted as an integer

            new_name = input("What is the new item? ") #somehow index this...
            #item[index] = new_name
            new_price = float(input("What is the new price? "))
            prices[index] = new_price
        print("\nCart Contents:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")
        change = input("\nDo you want to change another item? ")
        quit3 = input("Enter 'quit' to return to options page: ")
        if item == 'quit' or 'no':
            print()
            print (instructions)
            action = int(input("Please enter an action: "))
#-------------------------------------    
#TOTAL   
elif action == 4:
    print("/nCart Contents:")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")
        total += prices[i]
    print("____________________")
    print(f"Total: ${total:.2f}")
    quit4 = input("\nEnter 'quit' to return to options page: ")

    if item == 'quit':
        print()
        print (instructions)
        action = int(input("Please enter an action: "))

#-------------------------------------    
#QUIT   
print ("\nPlease come again! ")
#add restart option..?
