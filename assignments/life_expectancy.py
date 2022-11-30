with open("life-expectancy.csv") as f:    #error = can't find file
    for line in f:
        clean_line = line.strip()
        parts = line.split(" ")

        entity = parts[0]
        #code = parts[1]
        year = parts[2]
        life_expect = float(parts[3])
    
# max = -1
# for number in numbers:
#     if number > big:
#         big = number

# min = 9999999999
# for number in numbers:
#     if number > 0 and number < small:
#         small = number

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

print (f"The average life expectancy across all countries was {}") #average life_expect
print (f"The max life expectancy in {entity} with {life_expect}") 
print (f"The min life expectancy in {entity} with {life_expect}") 

