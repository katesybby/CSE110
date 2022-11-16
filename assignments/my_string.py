my_string = ''
new_string = ''
for letter in my_string:
    if letter == 's':
        new_string += 'z'
    elif letter == 'e':
        new_string += '3'
    else:
        new_string += letter
        
    print(new_string)