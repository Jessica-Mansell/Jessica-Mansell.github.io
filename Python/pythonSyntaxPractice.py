print("Hello World")

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
#This is a comment.
print("Hello, World!")

#This is a multi-
#line comment
#because there is no other way

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

# Case senstive
a = 4
A = "Sally"
#A will not overwrite a

print(A)
print(a)

#all of the below are totally legal variable naming conventions
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case example:
myVariableName = "John"

#Pascal Case example:
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#multiple values to variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables(remember whitespace!)
x = "awesome"
print("Python is " + x)

#another way
x = "Python is "
y = "awesome"
z = x + y
print(z)

#example of the + character working as a mathematical operator
x = 5
y = 10
print(x + y)

#Global Variables - created outside of a function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
