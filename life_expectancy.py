parts = []
max = -1
min = 99999
min_yr = []
max_yr = []
min_country = []
max_country = []

with open("life-expectancy.csv") as life: 
    for line in life:
        clean_line = line.strip()
        parts = clean_line.split(',')     #used to be 'line.split(",")'
        entity = parts[0]   #add strip func?
        code = parts[1]   #add strip func?
        year = int(parts[2]) 
        life_expect = float(parts[3])
    
# if life_expect < life:
#      min = life_expect
#     min_yr = year
#     min_country = entity
        
# for life_expect in life:
#     if life_expect > max:
#         max = life_expect

#     if life_expect > 0 and life_expect < min:
#         min = life_expect

input_year = input("Enter the year of interest: ")
# first = the_list[0] #gets the first item
# second = the_list[1] #gets the second item
# index = int(input("Which index would you like to get? "))
# user_choice = the_list[index] # gets the item at the index the user typed


#FOR GENERAL MAX AND MIN 
print (f"The overall max life expectancy is: {life_expect} from {entity} in {year}")
print (f"The overall min life expectancy is: {life_expect} from {entity} in {year}")

#FOR SPECIFIC YEAR
print (f"\nFor the year {year}:") 

# sum = 0
# for number in numbers:
#     sum += number
# count = len(numbers)
# average = sum / count

print (f"The average life expectancy across all countries was: ") #average life_expect { }
print (f"The max life expectancy in {entity} with {life_expect}") 
print (f"The min life expectancy in {entity} with {life_expect}")


