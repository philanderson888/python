# classes
print('\n\nSimple Class')
class MyClass:
    # static variable
    variable=22
    # instance variable
    def __init__(self,name):
        self.name=name 
    def doThis(self):
        return ('doing something')
instance01 = MyClass('myname')
# static class variable
print(MyClass.variable)
# static class variable in all instances
print(instance01.variable)
# instance method
print(instance01.doThis())
# instance variable
print(instance01.name)

# list in class
print('classess with lists in the instance')
class MyClass:
    def __init__(self,name):
        self.name=name 
        self.my_array=[]
    def add_to_array(self,item):
        self.my_array.append(item)
instance02 = MyClass('bob') 
instance02.add_to_array('item 1')
instance02.add_to_array('item 2')
instance02.add_to_array('item 3')
print(instance02.my_array)

# inheritance
print('\n\nclass inheritance')
class Parent:
    def __init__(self,name):
        print('parent has a name which is inherited in child')
        self.name=name 
class Child(Parent):
    pass 
instance03=Child('bill')
print (f'child name is {instance03.name}')

# extending a class
print ('\n\nextending a class')
class MyClassForExtending:
    variable='hi'
instance04 = MyClassForExtending()
instance04.field01='some data'
print (instance04.field01)
