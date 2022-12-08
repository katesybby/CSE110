min = 900
max = 0
min_yr = ''
max_yr = ''
min_country = ''
max_country = ''
avg_min = 900
avg_max = 0
avg_min_yr = ''
avg_max_yr = ''
avg_min_country = ''
avg_max_country = ''
avg_age = []

input_yr = input("\nEnter the year of interest: ")
with open("life-expectancy.csv") as life: 
    next(life)
    for line in life:
        first_line = line.strip()
        parts = first_line.split(',')   
        country = parts[0] 
        year = int(parts[2]) 
        age = float(parts[3])

        if age < min:
            min = age
            min_yr = year
            min_country = country
        if age > max:
            max = age
            max_yr = year
            max_country= country
        if year == input_yr:
            avg_age = []
            avg_age.append(age)
            avg_age_all = sum(avg_age) / len(avg_age)
            if age > avg_max:
                avg_max = age
                avg_max_country = country
            if age < avg_min:
                avg_min = age
                avg_min_country = country
    
print (f"\nThe overall min life expectancy is: {min} from {min_country} in {min_yr}.")            
print (f"The overall max life expectancy is: {max} from {max_country} in {max_yr}.")

print (f"\nFor the year {input_yr}:") 
print (f"The average life expectancy across all countries was: {avg_age_all}")
print (f"The min life expectancy in {avg_min_country} with {avg_min}.")
print (f"The max life expectancy in {avg_max_country} with {avg_max}.") 


