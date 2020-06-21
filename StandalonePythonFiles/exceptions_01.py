print ('\n\nExceptions')
print ('\n\nThrow exception if number is invalid')
while True:
    try:
        # x = int(input("please enter a number:  "))
        x = 45
        print ('thank you')
        break 
    except ValueError:
        print ("invalid number - try again")
    except RuntimeError, TypeError, NameError, OSError
        pass
print ('\n\nCustom Exception')
try:
    raise Exception('print this','and this')
except Exception as customException:
    print(type(customException))
    print(customException.args)
    print(customException)
    x,y = customException.args
    print (f'{x:10}{y:10}')
print ('\n\nRaising a particular exception')
try: 
    raise NameError('this is a name error exception')
except NameError:
    print ('name error')
print ('\n\nalso')
try:
    raise ValueError 
except ValueError:
    print ('value error exception')
# try..except..else
print('\n\ntry..except..else')
try:
    pass
except:
    print('an exception happened')
else:
    print('no exception took place')
# try..except..finally
print ('\n\ntry..except..finally')
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('keyboard interrupt')
finally:
    print('finally')


