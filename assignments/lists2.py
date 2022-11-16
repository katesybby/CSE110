
#HOW TO SELECT LIST ITEMS
first = the_list[0] # gets the first item
second = the_list[1] # gets the second item
index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

#LENGTH OF LIST
#number_of_books = len(books) 

#PRINT LIST
for i in range(len(books)):
    book = books[i]
    print(book) # prints each book to the screen.
    #other option:  print(f"{i}. {book}")    to create a numbered list items

#TWO CORRESPONDING LISTS AT ONCE
names = [ ]
numbers = [ ]
for i in range(len(names)):
    name = names[i]
    number = numbers[i]
    print(f"{name} - {number}")

#REMOVE LIST ITEMS
the_list.pop(3) # Removes the item at index 3
the_list.pop() # Removes the last item