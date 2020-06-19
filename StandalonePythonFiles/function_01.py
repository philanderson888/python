# functions
print('functions')

# declare
def doThis(n):
    print (n)
def alsoDoThis(n):
    print(n)
    return n

# call
doThis(100)

# return void
print('\n\nreturning nothing')
print(doThis(200)) 

# return data
print('\n\nreturning something')
print(alsoDoThis(300))
print('\n\nFunction with default values')
def doThat(n=1000):
    print (n)
doThat()
doThat(2)

# named parameters
print('\n\nCalling Named Parameters')
def doThis(a,b=1,c=2,d=3):
    print(f'a,b,c,d is {a,b,c,d}')
doThis(a=1) 

