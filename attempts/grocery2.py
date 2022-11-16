print ("---------------------------------------------------")
print ("Welcome to the Shopping Cart Program!")
print ("---------------------------------------------------")

cart = [ ]
item = [ ]
return1 = []
# total = 0

print ( )
if item == 'home':
    print ("""Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit """)
    action = int(input("Please enter an action: "))

#make into a while loop function:
if action == 1:
    while item != 'home':
        item = input("what item would you like to add? ")
        cart.append(item)
        price = input(f"what is the price of '{item}'? ")
        # total += price..?
        print (f"'{item}' has been added to the cart")

if action == 2:
    print ("the contents of the cart are: ")
    for item in cart:
        print (item)
    print ( )
    return1 = input(f"enter 'home' to return to options page: ")

# if action == 3:
#     remove item from list...


# if action == 4:
#     print (f"total cost: ${total}")
#     math function to add everything together
# def sumDigits(price):
#         total += price


if action == 5:
    print ("please come again! ")

