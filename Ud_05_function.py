#In python, function is a group of related statements that perform a specific task.
# NOTE: def is a identifier,(:) is the identifier after declar the function name.


def Greetme(name):
    print("Good Morning " + name)
    #function call

def Addintegers(a, b):
    print(a+b)
    #or, this type we can write the code.
    return a+b

Greetme("Gupta Prasad")

print(Addintegers(2,3))

'''
Practice using if-else statements.

1.Write a program that assigns a greeting to a variable.
2.Use an if statement to check if the greeting is "Hello".
3.If it matches, print "Hello there!" and "How can I assist you today?".
4.If it does not match, print "Greetings!".
5.After the if-else block, print "Program has completed."

Expected Output:

If greeting is "Hello":

Hello there!
How can I assist you today?
Program has completed.
If greeting is not "Hello":

Greetings!
Program has completed.
'''

greeting = "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")

print("Program has completed")

'''
Number Comparison:

1.Create a variable b and assign it a number 15.
2.Write an if statement to check if b is greater than 10.
3.If true, print "Number is greater than 10".
4.If false, print "Number is 10 or less".
5.Print "Comparison code is completed" at the end.

Expected Output:

For b = 15:
Number is greater than 10
Comparison code is completed.

For b = 5:
Number is 10 or less
Comparison code is completed.
'''

b = 15
if b > 10:
    print("number is greater than 10")
else:
    print("number is 10 or less")

b = 5
if b > 10:
    print("number is less than 10")
else:
    print("number is 10 or less")

print("Comparison code is completed")


'''
Doubling Numbers with For Loop
1.Create a list of numbers: [1, 4, 7, 10].
2.Use a for loop to iterate through the list.
3.Inside the loop, print each number multiplied by 3.

Expected Output:
3
12
21
30
'''

li = [1, 4, 7, 10]
for i in li:
    print(i * 3)

'''
Customized Greeting Based on Time of Day
1.Create a variable user and assign the value 16.

2.Use if-elif-else statements to print:

"Good Morning" if the hour is between 5 and 11,

"Good Afternoon" if the hour is between 12 and 17,

"Good Evening" if the hour is between 18 and 21,

"Good Night" for all other hours.

3.Print "Greeting code has completed."

Expected Output:

For input 10:
Good Morning
Greeting code has completed.

For input 15:
Good Afternoon
Greeting code has completed.    
'''

user = 16
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")

print("Greeting code has completed.")














