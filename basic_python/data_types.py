import math

age = int(input("How old are you? "))
print(f"On your next birthday, you will be: {age + 1}")
print()

eggs = int(input("How many egg cartons do you have? "))
print(f"You have {eggs * 12} eggs")
print()

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
print(f"Each person can have {math.floor(cookies/people)} cookies. With a remainder of {cookies % people} cookies")




