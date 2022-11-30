#practice for changing items in a list
print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = None

while item != "quit":
    item = input("Item: ")
    if item != "quit":
        shopping_list.append(item)

print("\nShopping list:")
for item in shopping_list:
    print(item)

print("\nNumbered shopping list:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nNumbered shopping list:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

