print ('\n\nwhile loop')
a,b = 0,1
while a<10:
    print(a)
    a,b = b, a+b
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

# iterating
print('\n\niterating')
long_string = 'abcdef'
my_iterator = iter(long_string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))