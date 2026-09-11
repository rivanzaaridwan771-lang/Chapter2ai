import math

print('Input a list of numbers: ')
x = input()
numbers = x.split()

for number in numbers:
    number = float(number)
    y = math.sin(number)
    print('The sine of ' + str(number) + ' is ' + str(y))