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
print (f'\n\nLook at decimals')
from decimal import *
print (Decimal(10))
print (f'\n\nLook at fractions')
from fractions import Fraction
print (f'What is -16/10 in simplest form? {Fraction(16,-10)}')
print (f'What is 2/5 + 3/5?  {(Fraction(2,5)+Fraction(3,5))}')
print (f'\n\ntabulating output')
print ('\t10\t20\t30')
print (f'\n\ntabulating output')
print ('|\t10\t|\t20\t|\t30')
print ('|\t40\t|\t50\t|\t60')
print ('|\t70\t|\t80\t|\t90')
print ('\n\n')
print (rf'unescaping characters ie backslash \ does not escape characters')
print (f'\n\nStrings are arrays')
longString='Here is a long string'
print (f'{longString} which has length {len(longString)}')
print (longString[0])
print (longString[1])
print (longString[2])
print (longString[3])
print (longString[4])
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
# concatanate
list02 = list01 + [50,60,70,80,90]
print(list02)
# append
list02.append(100)
print(list02)
# nested lists
list03=[list01,list02]
print(list03)