print ("-----------------------------------------------------------------")
print ("Welcome to the Shopping Cart Program!")
print ("-----------------------------------------------------------------")
print ("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit """)
#action = 0?
action = int(input("Please enter an action: "))

#something wrong in here:
# if action != ("1", "2", "3", "4", "5"): 
#     print ("number not listed, try again.")
#     action = int(input("Please enter an action: "))

cart = [ ]
item = None     
total = 0

print ( )
if item == 'home':
    instructions = ("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit """)
    action = int(input("Please enter an action: "))

#-------------------------------------
#-------------------------------------

#ADD ITEM ***
if action == 1:
    while item != 'home':
        item = input("what item would you like to add? ")
        if item != 'home':
            cart.append(item)
            price = input(f"what is the price of '{item}'? ")
            # def sumDigits(price):
            #     total += price
            #total price compution functioning..?
            print (f"'{item}' has been added to the cart")
        
        #if item == 'home':
            #print ({instructions})

#-------------------------------------    
#VIEW CART ***
if action == 2:
    print ("the contents of the cart are: ")
    for item in cart:
        print (item)
    print ( )
    return2 = input(f"enter 'home' to return to options page: ")

#-------------------------------------    
#REMOVE FROM CART 
#first = the_list[0] # gets the first item
#second = the_list[1] # gets the second item
#index = int(input("Which index would you like to get? "))
#user_choice = the_list[index] # gets the item at the index the user typed
# if action == 3:
# the_list.pop(3) # Removes the item at index 3
# the_list.pop() # Removes the last item

#-------------------------------------    
#TOTAL   
if action == 4:
    def sumDigits(price):
        total += price
        #total price compution functioning..?
    print (f"total cost: ${total}")

#-------------------------------------    
#QUIT   
if action == 5:
    print ("please come again! ")

