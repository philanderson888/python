# Learn Python

## Contents

- [Learn Python](#learn-python)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Reference](#reference)
  - [Python Manual Overview And Summary](#python-manual-overview-and-summary)
  - [Installation](#installation)
  - [Background](#background)
  - [pip Library Manager](#pip-library-manager)
  - [Installing libraries](#installing-libraries)
  - [Simple Commands](#simple-commands)
    - [Hello World](#hello-world)
    - [Comments](#comments)
    - [Printing To The Screen](#printing-to-the-screen)
    - [Ending a program](#ending-a-program)
    - [sleep.py](#sleeppy)
  - [Best Practice](#best-practice)
  - [are we on windows or linux](#are-we-on-windows-or-linux)
    - [clear screen](#clear-screen)
  - [variables](#variables)
    - [declaring](#declaring)
    - [integers](#integers)
    - [floats](#floats)
    - [Decimal](#decimal)
    - [Fractions](#fractions)
    - [parse string to integer](#parse-string-to-integer)
- [parse string to a float](#parse-string-to-a-float)
    - [input](#input)
    - [if statement](#if-statement)
    - [division and modulus operator](#division-and-modulus-operator)
    - [powers](#powers)
    - [tabulating output](#tabulating-output)
- [formatting numbers to a given number of decimal places](#formatting-numbers-to-a-given-number-of-decimal-places)
- [printing columns](#printing-columns)
    - [Not Escaping \](#not-escaping-)
    - [Strings Are Arrays](#strings-are-arrays)
    - [Strings are immutable](#strings-are-immutable)
    - [String length](#string-length)
  - [Lists](#lists)
    - [lists as queue](#lists-as-queue)
  - [coding](#coding)
    - [while](#while)
    - [fibonnaci](#fibonnaci)
    - [for](#for)
    - [range](#range)
    - [break out of loop](#break-out-of-loop)
    - [for loop variants](#for-loop-variants)
  - [iterating is another way to loop over objects](#iterating-is-another-way-to-loop-over-objects)
    - [pass](#pass)
    - [function](#function)
      - [function named parameters](#function-named-parameters)
    - [in](#in)
    - [lambda](#lambda)
  - [tuples](#tuples)
  - [Sets](#sets)
  - [Dictionaries](#dictionaries)
- [in and not in](#in-and-not-in)
- [is and is not](#is-and-is-not)
  - [modules](#modules)
  - [python scripts](#python-scripts)
  - [standard modules](#standard-modules)
    - [dir() lists modules in an import](#dir-lists-modules-in-an-import)
    - [dir(builtins) lists built in modules](#dirbuiltins-lists-built-in-modules)
    - [__main__ and main()](#main-and-main)
  - [packages](#packages)
  - [input and output](#input-and-output)
    - [str()](#str)
  - [formatting number](#formatting-number)
- [where is current working directory](#where-is-current-working-directory)
  - [reading from files](#reading-from-files)
  - [JSON](#json)
  - [Get JSON](#get-json)
  - [Exceptions](#exceptions)
  - [OOP](#oop)
  - [Class](#class)
  - [extending a method](#extending-a-method)
    - [built in methods](#built-in-methods)
    - [multiple inheritance](#multiple-inheritance)
  - [private instance variables](#private-instance-variables)
  - [adding instance members](#adding-instance-members)
  - [Web Scraping](#web-scraping)

## Introduction

This is a learning repository for learning python.

In this repository are single, standalone files which each intoduce a small piece of learning about python.

Happy learning!

## Reference

All you need to ever know about python in one page

https://docs.python.org/3/contents.html

Tutorial

https://docs.python.org/3/tutorial/index.html

## Python Manual Overview And Summary

```
pip library manager
pip install
x=1
no semicolons
tab 4 spaces for indent
no braces
for loop etc finish with a colon
a,b,c=1,2,3
if():
while():
for()
number is integer, float, decimal or fraction

```


## Installation

Download and install the latest version from `python.org`

Path at /usr/local/python 

## Background

Python is `interpreted` and not compiled

Python uses indentation instead of brackets

Python does not declare variables

Named after Monty Python!

Encoding is UTF8 

## pip Library Manager

Upgrading pip Library Manager To Latest Version

```
python -m pip install --upgrade pip
```

## Installing libraries

```py
pip install paramiko requests
```

## Simple Commands

### [Hello World](HelloWorld.py)

```py
print("Hello World")
```

### Comments

```py
# this is a python comment
```

### Printing To The Screen

```python
print('this was my first ever python application')
```



### Ending a program

Control-D on Linux
Control-Z on Windows
quit()


### sleep.py

```py
from time import sleep 
print ('starting')
sleep(2) 
print ('ending')
```



## Best Practice

```py
Use `PEP8`
Use 4 spaces
Dont use tabs
Wrap lines 
Use docstrings which give a description of functions
use spaces around operators x = 1
use space after comma a, b, c
MyClassNamedLikeThis
my_variable_named_like_this
my_method_named_like_this
my_function_named_like_this
self is the name of the first function argument
use utf8 
```

## are we on windows or linux

```py
# import only system from os 
from os import system, name 

# for windows 
if name == 'nt': 
    print ('we are on Windows')

# for mac and linux(here, os.name is 'posix') 
else: 
    print ('we are on Linux')
```

### clear screen

```py
import os
# for windows 
if os.name == 'nt': 
    os.system('cls')  # For Windows
    print ('we are on Windows')
# for mac and linux(here, os.name is 'posix') 
else: 
    os.system('clear')  # For Linux/OS X    
    print ('we are on Linux')   
```


## [variables](variables.py)

### declaring

```python
variable = 'this is a variable'
print(f'this is a python statement with a {variable}')
print(f'strings can have single \' or double \" quotes' + " - just like this")
# note : variables can be declared but cannot be used until their value has been assigned
n
print (n) # n is not defined
# multiple
print('\n\n printing multiple items')
a,b,c = 1,2,3
# print multiple items
print(a,b,c)
```

### integers

```py
number = 200
if isinstance(number,int):
    print ('number is an integer')
else:
    print ('number is a float')
```

### floats

```py
number = 200.0
if isinstance(number,int):
    print ('number is an integer')
else:
    print ('number is a float')
```

### Decimal

```py
print (f'\n\nLook at decimals')
from decimal import *
print (Decimal(10))
```

### Fractions

```py
print (f'\n\nLook at fractions')
from fractions import Fraction
print (f'What is -16/10 in simplest form? {Fraction(16,-10)}')
```

### parse string to integer

```py
number = int('500')
```

# parse string to a float

```py
number = float('500.223')
```

### input

```py
x = int(input('Enter a number: '))
if(x>10)
    print('Large')
elif(x>5)
    print('medium')
else
    print('small')

```

### [if statement](if_01.py)

```py
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
print('\n\nInputting a number')
x = int(input('Enter a number: '))
if (x>10):
    print('Large')
elif(x>5):
    print('medium')
else:
    print('small')

```

### division and modulus operator

```py
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
```

### powers

```py
print ('\n\nm to the nth power')
# 5 squared
print (f'5 to the power 2 is {(5**2)}')
```

### tabulating output

```py
print (f'\n\ntabulating output')
print ('\t10\t20\t30')
print (f'\n\ntabulating output')
print ('|\t10\t|\t20\t|\t30')
print ('|\t40\t|\t50\t|\t60')
print ('|\t70\t|\t80\t|\t90')
```

# formatting numbers to a given number of decimal places

```py
print ('\n\nprinting a number to a given format')
longNumber = 1.23456
print (f'1.23456 is {longNumber:.3f} to 3 decimal places')
```


# printing columns

```py
print ('\n\nprinting fixed columns')
print (f'{10:10}{20:10}{30:10}')
print (f'{40:10}{50:10}{60:10}')
print (f'{70:10}{80:10}{90:10}')
```



### Not Escaping \

```py
print (rf'unescaping characters ie backslash \ does not escape characters')
```

### Strings Are Arrays

```py
longString='Here is a long string'
print (longString[0])
print (longString[1])
print (longString[2])
print (longString[3])
print (longString[4])
```

### Strings are immutable

Cannot replace the nth item in an array with another character

### String length

```py
longString='Here is a long string'
print (f'{longString} which has length {len(longString)}')
```

## Lists

```py
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
# extend which is similar to concatenate
# insert 2000 at index i
list02.insert(i,2000)
# remove item which matches value
list02.remove(2000)
# remove item at given index
list02.del(0)
# remove last item
list02.pop()
# clear
list02.clear()
# count
list02.count()
# sort
list02.sort()
# reverse
list02.reverse()
# copy
list02.copoy
# nested lists
list03=[list01,list02]
print(list03)
```

*Note that to use a list as a stack, use append() and pop() methods where in list [1,2,3] item 3 is on the `top` so to speak of a stack*


### lists as queue

```py
from collections import deque
myqueue = deque(["a","b","c"])
myqueue.append("d")
myqueue.append("e")
# remove first item ie 'a'
myqueue.popleft()
# myqueue holds b,c,d,e
```



## coding

### while

```py
print ('\n\nwhile loop')
a,b = 0,1
while a<10:
    print(a)
    a,b = b, a+b

print('\n\nbreak out of a loop and also continue when value is 3')
counter=-1
while True:
    counter+=1
    if(counter==3):
        print ('not printing this number')
        continue
    print (counter)
    if(counter>10):
        break 


```

### [fibonnaci](fibonnaci.py)

```py
a,b = 0,1
while a<10:
    print(a)
    a,b = b, a+b
```

### for

```py
print ('\n\nfor loop')
myArray = [10,20,30]
for item in myArray:
    print(item)
```

### range

```py
print('\n\niterate over a sequence of numbers')
for i in range(10):
    print(i)
print('\n\niterate over a sequence of numbers')
for i in range (5,10):
    print(i)
print('\n\niterate in steps')
for i in range (0,20,5):
    print(i)
```

### break out of loop

```py
print('\n\nbreak out of a loop and also continue when value is 3')
counter=-1
while True:
    counter+=1
    if(counter==3):
        print ('not printing this number')
        continue
    print (counter)
    if(counter>10):
        break 
```


### for loop variants

```py
for item in [1,2,3]:

for item in (1,2,3):

for key in { 1:'one',2:'two'}:

for char in "abc":

for line in open("myfile.txt"):
```


## iterating is another way to loop over objects

```py
print('\n\niterating')
long_string = 'abcdef'
my_iterator = iter(long_string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
```








### pass

pass can be used as a null placeholder instead of code, note that in OOP programming we might use empty curly braces in such a scenario

### function

```py
print('functions')
# declare
def doThis(n):
    print (n)
def alsoDoThis(n):
    print(n)
    return n
# call
doThis(100)
print('\n\nreturning nothing')
print(doThis(200)) 
print('\n\nreturning something')
print(alsoDoThis(300))
print('\n\nFunction with default values')
def doThat(n=1000):
    print (n)
doThat()
doThat(2)
```

#### function named parameters

```py
print('\n\nCalling Named Parameters')
def doThis(a,b=1,c=2,d=3):
    print(f'a,b,c,d is {a,b,c,d}')
doThis(a=1) 
```



### in

```py
myString='h'
longString = 'hello'
if myString in longString:
    print('true')
else    
    print('false')
```


### lambda

lambda functions are just synctatic sugar for regular functions

```py
# declare a function using the lambda syntax
print('\n\nsimple lambda with one input')
doThis = lambda input : input + 10
print(doThis(15))

print('\n\nsimple lambda with two inputs')
doThat = lambda a,b : a*b 
print(doThat(10,20))

# lambda in a function
print('\n\nuse a multiplier with a lambda')
def alsoDoThis(fixedMultiplier):
    return lambda b,c : fixedMultiplier*b*c 
functionMultiply=alsoDoThis(3)
print(functionMultiply(10,2))
```



## tuples

Tuples are immutable

```py
print ('\n\nTuples')
tuple01 = 10, True , 'a string'
print(tuple01)
print(tuple01[0])
print(tuple01[1])
print(tuple01[2])
```


## Sets

Sets are `unordered` collections with `uniquely indexed items`

```py
# sets
print ('\n\nSets')
set01 = { 'a', 'b', 'c'}
print (set01)
print (f"is 'a' in set01? {'a' in set01}")
```


## Dictionaries

Dictionaries are indexed by a `key` which is `unique`

```py
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
```



# in and not in

Is an item present?

# is and is not

are two objects equal?


## modules

create a file and save it `module_name.py`

in the python program import the module with

```py
import module_name
```

## python scripts

to run python code as a script don't put the code in a function



```py
# script.py
print ('this is a script')
```

```py
import script
```


## standard modules

Python has built into it 'standard' modules which are described in the `Python Library Reference`.

### dir() lists modules in an import

```py
import thisModule
dir(thisModule)
```

### dir(builtins) lists built in modules

```py
import builtins
dir(builtins)
```

### __main__ and main()

The main() method can be defined so when a module is imported all of the code does not run, only the main() method runs


## packages



## input and output

```py
variable = 'variable
print (f'some text with a {variable} here)1
```

### str() 

str() generates a string from the input

## formatting number

to print to 3 decimal places

```py
longNumber = 1.23456
print (f'number is {longNumber:.3f})
```

# where is current working directory

```py
import os
print (os.getcwd())
```

## reading from files

w = overwrite

r = read

a = append

r+ = read and write

```py
# where is current working directory?
import os
print (os.getcwd())

# print file
with open('data.txt') as data_file:
    print ('\n\nRead the complete file')
    data = data_file.read()
    print (data)

# print part of file
with open('data.txt') as data_file:
    print ('\n\nRead only 10 characters')
    smalldata = data_file.read(10)
    print (smalldata)

# loop over lines in a file
print ('\n\nRead line by line in a loop until done')
with open ('data.txt') as data:
    counter=0
    for line in data:
        counter += 1
        print (counter,line, end='')

# loop over lines in a file with formatting
print ('\n\nRead line by line in a loop until done')
with open ('data.txt') as data:
    counter=0
    for line in data:
        counter += 1
        # not printing a blank line
        # must include slice and not include the final character
        # which is a newline character
        print (f'{counter:>10}{line[:-1]:>30}')
# write
print('\n\nWriting to a file')
with open ('data.txt', 'a') as data:
    data.write('\nadding some data')
with open ('data.txt') as data:
    print (data.read())
# read and append
print ('\n\nOpen file for read and append')
with open ('data.txt', 'a+') as data:
    data.write('\nappend to end')
```



## JSON

```py
# dump data
import json
print (json.dumps([1,'string','hello', True,'there']))
# serialise a list to a file
list01 = [10,20,30]
with open('data.json','w') as data:
    json.dump(list01,data)
# read back the file
with open ('data.json') as data: 
    print (data.read())
# this time read back the file into a list again
with open ('data.json') as data:
    list01 = json.load(data)
    print (list01)
```


## Get JSON

```py
import requests
r = requests.get('https://raw.githubusercontent.com/philanderson888/data/master/customers.json')
jsonOutput = r.json()
print (jsonOutput)
```





## Exceptions

Try..Except..Else..Finally

```py
print ('\n\nExceptions')
print ('\n\nThrow exception if number is invalid')
while True:
    try:
        # x = int(input("please enter a number:  "))
        x = 45
        print ('thank you')
        break 
    except ValueError:
        print ("invalid number - try again")
    except RuntimeError, TypeError, NameError, OSError
        pass
print ('\n\nCustom Exception')
try:
    raise Exception('print this','and this')
except Exception as customException:
    print(type(customException))
    print(customException.args)
    print(customException)
    x,y = customException.args
    print (f'{x:10}{y:10}')
print ('\n\nRaising a particular exception')
try: 
    raise NameError('this is a name error exception')
except NameError:
    print ('name error')
print ('\n\nalso')
try:
    raise ValueError 
except ValueError:
    print ('value error exception')
# try..except..else
print('\n\ntry..except..else')
try:
    pass
except:
    print('an exception happened')
else:
    print('no exception took place')
# try..except..finally
print ('\n\ntry..except..finally')
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('keyboard interrupt')
finally:
    print('finally')
```


## OOP

Multiple base classes allowed

Derived class can override any method

Method can call the base class method of the same name

By default all classes are public

By default all methods are virtual and can be overridden

Namespaces separate code

    Python built-in namespace surrounds all code

    Scope is the region of code inside a namspace

        Four scopes exist

            - inner scope
            - enclosing functions
            - current module's global names
            - namespace built-in names

Attributes are written object.attribute and may be read only or writable


## Class

```py
# classes
print('\n\nSimple Class')
class MyClass:
    # static variable
    variable=22
    # instance variable
    def __init__(self,name):
        self.name=name 
    def doThis(self):
        return ('doing something')
instance01 = MyClass('myname')
# static class variable
print(MyClass.variable)
# static class variable in all instances
print(instance01.variable)
# instance method
print(instance01.doThis())
# instance variable
print(instance01.name)

# list in class
print('classess with lists in the instance')
class MyClass:
    def __init__(self,name):
        self.name=name 
        self.my_array=[]
    def add_to_array(self,item):
        self.my_array.append(item)
instance02 = MyClass('bob') 
instance02.add_to_array('item 1')
instance02.add_to_array('item 2')
instance02.add_to_array('item 3')
print(instance02.my_array)

# inheritance
print('\n\nclass inheritance')
class Parent:
    def __init__(self,name):
        print('parent has a name which is inherited in child')
        self.name=name 
class Child(Parent):
    pass 
instance03=Child('bill')
print (f'child name is {instance03.name}')
```

## extending a method

all methods can be overridden

methods can be extended also

just call `Parent.method(self,arguments)

### built in methods

isinstance()

issubclass()

### multiple inheritance

class Child(Parent1,Parent2)

## private instance variables

private instance variables don't exist in python

convention uses _private_variable with an `underscore` at the start


## adding instance members

```py
class MyClass:
    pass
instance = MyClass()
instance.field01='some data'
```










## Web Scraping


```python
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

soup.findAll('a')

one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']

download_url = 'http://web.mta.info/developers/'+ link

urllib.request.urlretrieve(download_url, 'a')

time.sleep(1)
```

Complete working version (does download data!)

Taken from https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

```python
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    time.sleep(1) #pause the code for a sec
```
