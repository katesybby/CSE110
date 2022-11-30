people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

min_age = 200
min_name = []

for person in people:
    parts = person.split()
    name = parts[0]
    age = int(parts[1]) 

    if age < min_age:
        min_age = age
        min_name = name

print(f"The minimum age is: {min_age}")
print(f"The youngest person is: {min_name}")