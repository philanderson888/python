# Learn Python

## Introduction

This is a learning repository for learning python.

In this repository are single, standalone files which each intoduce a small piece of learning about python.

Happy learning!

- [Learn Python](#learn-python)
  - [Introduction](#introduction)
  - [Upgrading pip Library Manager To Latest Version](#upgrading-pip-library-manager-to-latest-version)
  - [Installing libraries](#installing-libraries)
  - [Simple Commands](#simple-commands)
    - [Hello World](#hello-world)
    - [Printing To The Screen](#printing-to-the-screen)
    - [variables](#variables)
    - [if statement](#if-statement)
  - [Get JSON](#get-json)
  - [Web Scraping](#web-scraping)

## Upgrading pip Library Manager To Latest Version

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

### Printing To The Screen

```python
print('this was my first ever python application')
```

### [variables](variables.py)

```python
variable = 'this is a variable'
print(f'this is a python statement with a {variable}')
```

### [if statement](if_01.py)

```py
print("Hello World")
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
