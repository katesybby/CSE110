word = "unicorn"
fave_letter = input("what's ur fave letter? ")

for letter in word:
    if letter.lower() == fave_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == fave_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()