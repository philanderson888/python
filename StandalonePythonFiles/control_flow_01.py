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
print('\n\nbreak out of a loop')
counter=0
while True:
    print (counter)
    counter+=1
    if(counter>5):
        break 