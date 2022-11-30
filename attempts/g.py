items = ("cheese", "bread", "milk")
prices = ("1.99", "2.36", "2.20" )
item = []
quit3 = [] #see if u actually need this
instructions = ("3. Remove item")



change = "yes"
while change == "yes":
    change = input("\nDo you want to change an item (yes/no)? ")

    if change == "yes":
        print("Cart Contents:")
        for i in range(len(items)):
            index = i + 1
            print(f"{i+1}. {items[i]} - ${prices[i]:.2}")
        remove = int(input("What number item do you want to update? "))

        if remove <= index:
            items.pop(remove - 1)
            prices.pop(remove - 1)

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