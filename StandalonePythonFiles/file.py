# where is current working directory
import os
print (os.getcwd())
with open('StandalonePythonFiles/data.txt') as data_file:
    data = data_file.read()
    print (data)