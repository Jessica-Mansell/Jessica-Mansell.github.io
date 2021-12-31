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

#Global Keyword - If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#Numeric types in Python
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#int examples
x = 1
y = 35656446457444
z = -12145555

print(type(x))
print(type(y))
print(type(z))

#float examples
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#moar floats
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#converting one type to another
x = 1
y = 2.8
z = 1j

#convert from int to float
a = float(x)

#convert from float to int
b = int(y)

#convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

#Strings literal
print("Hello")
print('Hello')

#Assign string to a variable
a = "Hello"
print(a)

#Multiline Strings with three double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are arrays.Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
a = "Hello World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)

#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#check string; To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#or use it in an if statement
txt = "The best things in are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

#Slicing strings or You can return a range of characters by using the slice syntax. below example gets characters from 2-5
b = "Hello World!"
print(b[2:5])

#Get the characters from the start to position 5
b = "Hello, World!"
print(b[:5])

#Slice to the end
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#modifying Strings with built in python methods
#Example of turning to upper case
a = "Hello, World!"
print(a.upper())

#turning to lower case
a = "Hello, World!"
print(a.lower())

#removing whitespace
a = " Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))
