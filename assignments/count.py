#count 1-9
for i in range(10):
    print(f'the count is (i)')

#count 1-10
for i in range(1, 11):
    print(f'the count is (i)')

#count even numbers 2-10
for i in range(2, 11, 2):
    print(f'the count is (i)')

#times table 
for i in range(11):
    for j in range(11):
        print(f'{i * j:<4}', end='')
    print()
