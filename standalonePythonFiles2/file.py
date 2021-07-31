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