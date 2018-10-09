# Bill Israel introduction to Python
# sudo code = code in english
# batteries included language - has alot of built in functionality
# compiled and interpreted
# use python 3

"""
A simple calculator to demonstrate some Python features
"""
ADD = 1
SUBTRACT = 2

numbers_string = input('Give me numbers to add:')

numbers = numbers_string.split()

operation = int(input ( """
What do you want to do?
    1) Add
    2) Subtract

Enter a number:
"""))

if operation == ADD:
    total = 0
    for number in numbers:
        try:
            total += int(number)
        except ValueError:
            continue
elif operation == SUBTRACT:
    int_numbers = []
    for number in numbers:
        int_numbers.append(int(number))

    sorted_numbers = sorted(int_numbers, reverse=True)    
    total = sorted_numbers[0]
    for int_num in int_numbers[1:]:
        total -= int_num

else: 
    pass

print(total)

