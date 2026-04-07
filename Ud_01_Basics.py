print("Hello")

# This is the comment type in python.
# Shortcut for executing file: ctrl + shift + f10

# Variable
a= 3
print(a)

# 'a' is the variable, '=' is operator, '3' is value i.e integer.


# Single variable execution
str = "Hello World"
print(str)

# Multiple variable execution
b,c,d=6,7.9,"great"

# print ("value is" +b) -- this is not correct format

print("{} {}".format("value is ", b ))
# for the different type of data types execution in a single line.


# whice types of Data Types:
print(type(b))
print(type(c))
print(type(d))


'''
Understand how to manipulate strings and print them.
1.Create a variable named greeting and assign it the string "Welcome to Python Programming".

2.Print the greeting variable.

3.Modify the string to include your instructor name "Rahul!". For example, "Welcome to Python Programming, [Instructor Name]!" and print the modified string.

Expected Result:
Welcome to Python Programming
Welcome to Python Programming, Rahul!
'''

greeting =  "Welcome to Python Programming"
print(greeting)
greeting = greeting + ", Rahul!"
print(greeting)


'''
Variable Assignment and Types:
1.Create three variables: age, height, and favorite_color. Assign them values 25, 5.9, blue:

age: an integer (e.g., 25)
height: a float (e.g., 5.9)
favorite_color: a string (e.g., "blue")

2.Use the print function to display each variable and its type using the type() function.

Expected Result:
Age: 25 | Type: <class 'int'>
Height: 5.9 | Type: <class 'float'>
Favorite Color: blue | Type: <class 'str'>
'''

age = 25
height = 5.9
favorite_color = "blue"

print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("favorite_color:", favorite_color, "|type:",type(favorite_color))