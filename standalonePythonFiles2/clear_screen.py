import os
# for windows 
if os.name == 'nt': 
    os.system('cls')  # For Windows
    print ('we are on Windows')
# for mac and linux(here, os.name is 'posix') 
else: 
    os.system('clear')  # For Linux/OS X    
    print ('we are on Linux')   