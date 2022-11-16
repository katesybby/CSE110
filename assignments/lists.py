print('enter a list of numbers, type 0 when finished: ')

numbers = [ ]
number = -1

while number != 0:
    number = int(input('enter number: '))
    if number != 0:
        numbers.append(number)

sum = 0
for number in numbers:
    sum += number
print()
print('---------------------------------')
print(f"the sum is: {sum}")

count = len(numbers)
average = sum / count
print(f"the average is: {average}")

big = -1
for number in numbers:
    if number > big:
        big = number
print(f'the largest number is: {big}')

small = 9999999999
for number in numbers:
    if number > 0 and number < small:
        small = number
print(f'the smallest positive number is: {small}')

sorted_list = sorted(numbers)
print('the sorted list is:')
for number in sorted_list:
    print(number)
    print('---------------------------------')