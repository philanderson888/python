# variable
variable = 'variable as a string'

# integer
number = 200
print(f'this is a python statement with a "{variable}" and number {number+1}')
print(f'strings can have single \' or double \" quotes' + " - just like this")

# multiple
print('\n\nprinting multiple items')
a,b,c = 1,2,3

# print multiple items
print(a,b,c)

# test to see if a number is an integer
print('\n\nIs a number an integer')
if isinstance(number,int):
    print ('number is an integer')

# float
number = 200.0

# test to see if a number is an integer
if isinstance(number,int):
    print ('number is an integer')
else:
    print ('number is a float')


# convert to an integer
print ('\n\nparse string to integer')
number = int('500')
print (number)

# convert to a float
print ('\n\nparse string to a floating point number')
number = float('500.223')
print (number)

# division

print ('\n\nlooking at division')
print ('17 divided by 3 yields a) exact b) whole number c) remainder')

# decimal division
print (17/3)

# integer division
print (17//3)

# remainder after division
print (17%3)
print (f'so 17/3 is {17/3} which can be written {17//3} remainder {17%3}')
print ('\n\nm to the nth power')

# 5 squared
print (f'5 to the power 2 is {(5**2)}')

# Decimal type
print (f'\n\nLook at decimals')
from decimal import *
print (Decimal(10))

# Fraction type
print (f'\n\nLook at fractions')
from fractions import Fraction
print (f'What is -16/10 in simplest form? {Fraction(16,-10)}')
print (f'What is 2/5 + 3/5?  {(Fraction(2,5)+Fraction(3,5))}')

# Tabulating output
print (f'\n\ntabulating output')
print ('\t10\t20\t30')
print (f'\n\ntabulating output')
print ('|\t10\t|\t20\t|\t30')
print ('|\t40\t|\t50\t|\t60')
print ('|\t70\t|\t80\t|\t90')
print ('\n\n')
print (f'unescaping characters ie backslash \ does not escape characters')

# formatting
print ('\n\nprinting a number to a given format')
longNumber = 1.23456
print (f'1.23456 is {longNumber:.3f} to 3 decimal places')


# printing columns
print ('\n\nprinting fixed columns')
print (f'{10:10}{20:10}{30:10}')
print (f'{40:10}{50:10}{60:10}')
print (f'{70:10}{80:10}{90:10}')






# Strings as character arrays
print (f'\n\nStrings are arrays')
longString='Here is a long string'
print (f'{longString} which has length {len(longString)}')
print (longString[0])
print (longString[1])
print (longString[2])
print (longString[3])
print (longString[4])

# Lists
print (f'\n\nLists')
list01 = [10,20,30,40]
print (list01)
# first item
print (list01[0])
# last item
print (list01[len(list01)-1])
# also last item
print (list01[-1])
# slice from 3rd item (2nd index)
subList01 = list01[2:]
print (subList01)
# slice from 3rd last item
subList02 = list01[-3:]
print (subList02)
# concatenate
list02 = list01 + [50,60,70,80,90]
print(list02)
# append
list02.append(100)
print(list02)
# nested lists
list03=[list01,list02]
print(list03)

# finding strings in strings
print ('\n\nusing the "in" keyword')
myString='h'
longString = 'hello'
if myString in longString:
    print('true')
else:  
    print('false')
print('named parameters')

# tuples
print ('\n\nTuples')
tuple01 = 10, True , 'a string'
print(tuple01)
print(tuple01[0])
print(tuple01[1])
print(tuple01[2])

# sets
print ('\n\nSets')
set01 = { 'a', 'b', 'c'}
print (set01)
print (f"is 'a' in set01? {'a' in set01}")


# dictionaries
print ('\n\nDictionaries')
dictionary01 = { 1: 'one', 2: 'two', 3: 'three' }
dictionary01[4] = 'four'
print (dictionary01)
# remove item
del dictionary01[2]
print (f'after removing index 2 the dictionary shows {dictionary01}')
# list the indexes
print (f'listing the indexes with {list(dictionary01)}')
# is item in dictionary
print (f'is item 3 in the dictionary? {3 in dictionary01}')
# with a constructor
dictionary02 = dict ( [ (1,'one'), (2, 'two'), (3, 'three')  ])
print (dictionary02)
# automatically build a dictionary
print ('\n\nAutomatically build a dictionary')
dictionary03 = { x:x**2 for x in (1,2,3,4,5) }
print (dictionary03)
# iterate
print ('\n\nIterate over a dictionary')
for key,value in dictionary01.items():
    print (key,value)
print ('\n\nIterate over a dictionary using the index')
for index,value in enumerate(dictionary01):
    print (index,value)