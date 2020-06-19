# import only system from os 
from os import system, name 

# for windows 
if name == 'nt': 
    print ('we are on Windows')

# for mac and linux(here, os.name is 'posix') 
else: 
    print ('we are on Linux')