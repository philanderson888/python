print('functions')
# declare
def doThis(n):
    print (n)
def alsoDoThis(n):
    print(n)
    return n
# call
doThis(100)
print('\n\nreturning nothing')
print(doThis(200)) 
print('\n\nreturning something')
print(alsoDoThis(300))
print('\n\nFunction with default values')
def doThat(n=1000):
    print (n)
doThat()
doThat(2)
print ('\n\nusing the "in" keyword')
myString='h'
longString = 'hello'
if myString in longString:
    print('true')
else:  
    print('false')
print('named parameters')
