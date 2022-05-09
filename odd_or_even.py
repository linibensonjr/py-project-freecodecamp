''' Odd or Even number'''

from timeit import repeat


# repeat_ = False

number = int(input('What number are you thinking?'))
if number%2 == 0:
    print("That's an even number! Have another? ")
else:
    print("That's an odd number! Have another? ")