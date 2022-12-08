ages = []
max = -1
min = 99999
min_yr = []
max_yr = []
min_country = ''
max_country = ''


with open("life-expectancy.csv") as life: 
    next(life)          #could be useless..?
    for line in life:
        first_line = line.strip()
        parts = first_line.split(',')   
        country = parts[0] 
        year = int(parts[2]) 
        age = float(parts[3])

if age < min: 
    min = min_country = country
    min_yr = year
    # min_country = country
    # min = age  

  
# for age in life:
#     if age > max:
#         max = age

#     if age > 0 and age < min:
#         min = age

input_year = input("Enter the year of interest: ")
print (f"The overall max life expectancy is: {max} from {max_country} in {max_yr}")
print (f"The overall min life expectancy is: {min} from {min_country} in {min_yr}")

print (f"\nFor the year {input_year}:") 

# sum = 0
# for number in numbers:
#     sum += number
# count = len(numbers)
# average = sum / count

print (f"The average life expectancy across all countries was: ")
print (f"The max life expectancy in {country} with {age}") 
print (f"The min life expectancy in {country} with {age}")


