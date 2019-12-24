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

variable = 'this is a variable'

print('this was my first ever python application')
print(f'this is a python statement with a {variable}')

