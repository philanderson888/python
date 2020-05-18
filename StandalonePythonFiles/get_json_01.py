import requests
r = requests.get('https://raw.githubusercontent.com/philanderson888/data/master/customers.json')
jsonOutput = r.json()
print (jsonOutput)


