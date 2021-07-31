# declare a function using the lambda syntax
print('\n\nsimple lambda with one input')
doThis = lambda input : input + 10
print(doThis(15))

print('\n\nsimple lambda with two inputs')
doThat = lambda a,b : a*b 
print(doThat(10,20))

# lambda in a function
print('\n\nuse a multiplier with a lambda')
def alsoDoThis(fixedMultiplier):
    return lambda b,c : fixedMultiplier*b*c 
functionMultiply=alsoDoThis(3)
print(functionMultiply(10,2))