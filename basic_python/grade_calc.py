grade = int(input("what is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Stretch Challenge 2
if grade >= 93:
    sign = ""

# Stretch Challenge 3
if letter == "F":
    sign = ""

print(f"your grade is: {letter}{sign}")


if grade >= 70:
    print("yay! you passed the class!")
else:
    print("yikes! you need to get ur grades up gurl!")