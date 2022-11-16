print ("----------------------------------------------")
item = [ ]
price = [ ]
total = [ ]
cart = [ ]

while item != 'quit':
    item = input("what item would you like to add? ")
    if item != 'quit':
        cart.append(item)
        price = input(f"what is the price of '{item}'? ")
        #need something to tie price to item
        def sumDigits(price):
            total += price
        print (f"'{item}' has been added to the cart") 

print ( )
print ("the contents of the cart are: ")
for i in range(len(cart)):
    item = cart[i]
    total = price[i]
    #print(f"{item} {price}")
    print(f"{i}. {cart[i]} - ${price}")
    

#COMPUTE TOTAL:
# def sumDigits(price):
#     total += price
