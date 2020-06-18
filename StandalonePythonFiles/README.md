# Learn Python

## Contents

- [Learn Python](#learn-python)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Background](#background)
  - [pip Library Manager](#pip-library-manager)
  - [Installing libraries](#installing-libraries)
  - [Simple Commands](#simple-commands)
    - [Hello World](#hello-world)
    - [Comments](#comments)
    - [Printing To The Screen](#printing-to-the-screen)
    - [Ending a program](#ending-a-program)
  - [variables](#variables)
    - [declaring](#declaring)
    - [integers](#integers)
    - [floats](#floats)
    - [Decimal](#decimal)
    - [Fractions](#fractions)
    - [input](#input)
    - [if statement](#if-statement)
    - [division and modulus operator](#division-and-modulus-operator)
    - [powers](#powers)
    - [tabulating output](#tabulating-output)
    - [Not Escaping \](#not-escaping-)
    - [Strings Are Arrays](#strings-are-arrays)
    - [Strings are immutable](#strings-are-immutable)
    - [String length](#string-length)
  - [Lists](#lists)
  - [coding](#coding)
    - [while](#while)
    - [fibonnaci](#fibonnaci)
    - [for](#for)
    - [range](#range)
    - [pass](#pass)
    - [function](#function)
  - [Get JSON](#get-json)
  - [Web Scraping](#web-scraping)

## Introduction

This is a learning repository for learning python.

In this repository are single, standalone files which each intoduce a small piece of learning about python.

Happy learning!

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
# nested lists
list03=[list01,list02]
print(list03)
```

## coding

### while

```py
print ('\n\nwhile loop')
a,b = 0,1
while a<10:
    print(a)
    a,b = b, a+b

print('\n\nbreak out of a loop')
counter=0
while True:
    print (counter)
    counter+=1
    if(counter>5):
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
print ('\n\nfor loop')
myArray = [10,20,30]
for item in myArray:
    print(item)
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

### in

```py
myString='h'
longString = 'hello'
if myString in longString:
    print('true')
else    
    print('false')
```

## Get JSON

```py
import requests
r = requests.get('https://raw.githubusercontent.com/philanderson888/data/master/customers.json')
jsonOutput = r.json()
print (jsonOutput)
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
