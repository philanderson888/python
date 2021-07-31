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

# get json from the web
print ('\n\nGet JSON from the web')
import requests
r = requests.get('https://raw.githubusercontent.com/philanderson888/data/master/customers.json')
jsonOutput = r.json()
print (jsonOutput)