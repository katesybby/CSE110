cart = []
prices = []
action = 0
number_item = []

print("\nWelcome to the Shopping Cart Program!")

#As long as the user does not type 5 if will display a list of options to chose from.
while action != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    action = int(input("Please enter an action: "))

    #If the user chooses 1 it will ask for an item to be added to the cart list.
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item.capitalize()}'? "))
        cart.append(item.capitalize())
        prices.append(price)
        print(f"'{item.capitalize()}' has been added to the cart.")
    
    #If the user chooses 2 it will display what items are currently in the cart list.
    elif action == 2:
        print("The contents of the shopping cart are:")

        for i in range(len(cart)):
            item = cart[i]
            price = prices[i]
            print(f"{i + 1}. {item} - ${price:.2f}")

    elif action == 3:
        # for i in range(len(cart)):
        #     index = i + 1
        # remove = int(input("Which item would you like to remove? "))
        # if remove > index:
        #     print("Sorry, that is not a valid item number.")
        # elif remove <= index:
        #     cart.pop(remove - 1)
        #     prices.pop(remove - 1)

        remove = int(input('What item would you like to remove (#)?'))
        if remove-1 in range (number_item):
            convert_base = remove-1
            delete_item = cart.pop(convert_base) 
            delete_item = prices.pop(convert_base)
            print ('Item removed')
        else:
            print('That is not a valid option')     
    
    elif action == 4:
        total = sum(prices)
        print(f"The toal price of the items in the shopping cart is ${total}")

#Wish the user goodbye.
print("Thank you. Goodbye.")