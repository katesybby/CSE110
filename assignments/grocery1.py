# mini grocery cart game

print ("----------------------------------------------")
print("Enter items and prices(type: quit when done)")

items = []
prices = []
item = None

while item != "quit":
    item = input("Item? ")
    if item != "quit":
        price = float(input("Price? "))
        items.append(item)
        prices.append(price)
        print (f"'{item}' has been added to the cart") 

total = 0
print()
print("Cart Contents:")
for i in range(len(items)):
    print(f"{i}. {items[i]} - ${prices[i]}")
    total += prices[i]

print()
print(f"Total: ${total:.2f}")
