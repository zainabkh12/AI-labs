# While loop (Fixed version)
x = 1
while x < 6:
    print("Hello geeks")
    x += 1  # Increment x by 1 each time

# Single statement while block
count = 0
while count == 0: print("Hello Geek (single line while)"); count += 1

# For Loop - Iterating over list
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# For Loop - Iterating over tuple
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# For Loop - Iterating over string
s = "Geeks"
for i in s:
    print(i)

# Iterating by index
my_list = ["geeks", "for", "geeks"]
for index in range(len(my_list)):
    print(my_list[index])

# Continue Statement 
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter:', letter)

# Simple function
def my_function():
    print("Hello from a function")

my_function()

# Function with parameters
a = 8
def my_function_with_param(x):
    y = x + 1
    return y

print(my_function_with_param(a))

# Default parameter value
def my_fun(country="Pakistan"):
    print("I am from", country)

my_fun()  # Uses default value
my_fun("Norway")  # Uses provided value

# List as parameter
def my_fun_list(fruits):
    for x in fruits:
        print(x)

fruitss = ['banana', 'apple', 'mango']
my_fun_list(fruitss)

# Return value from function
def multiply_by_five(x):
    return 5 * x

print(multiply_by_five(3))
print(multiply_by_five(5))
print(multiply_by_five(9))

# Keyword arguments
def my_children(child3, child2, child1):
    print("The youngest child is " + child3)

my_children(child1="Emil", child2="Tobias", child3="Linus")

# Creating a class and object
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# __init__ function and method in class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(" My name is", self.name)

p1 = Person("Alishba", 19)
print("Name:", p1.name)
print("Age:", p1.age)
p1.myfunc()
