# LIST:

value = [1, 2, "gupta", 4, 5]
# list is data type that allows multiple values and it can be different data types.
print(value)

#Indexing
print(value[0])  #1
print(value[3])   #4
print(value[-1])  #5
print(value[1:3]) #[2, 'gupta']
value.insert(3, "prasad")   #need to add the value in between the list.
print(value)   #[1, 2, 'gupta', 'prasad', 4, 5]
value.append("end")   #append in the last nay character.
print(value)  #[1, 2, 'gupta', 'prasad', 4, 5, 'end']

# Updates the value in the list.
value[2] = "GUPTA"
print(value)  #[1, 2, 'GUPTA', 'prasad', 4, 5, 'end']

#delete the value in the list.
del value[0]
print(value)  #[2, 'GUPTA', 'prasad', 4, 5, 'end']


#TUPLE: same as lIST data type but immutable i.e. updation is not possible.

# val = (1, 2, "Gupta", 5.4) # it will showing error in the o/p bcz it's immutable.

# print(val[1])
# val[2]="GUPTA"
# print(val)


#DICTIONARY: IT'S a key and value pair form, enclosed in {}.
dic = {"a": 2, 4: "bcd", "c" : "hello"}

print(dic[4])
print(dic["c"])

dict = {}
dict["first_name"] = "gupta"
dict["last_name"] = "samal"
dict["gender"] = "male"

print(dict)
print(dict["last_name"], dict["gender"])



'''
Working with Lists:
1.Create a list named fruits that contains below five different fruit names (strings).
- apple", "banana", "cherry", "date", "elderberry"
2.Print the first and last elements of the list.
3.Use slicing to print the second and third fruits from the list.

Expected Result:
First fruit: apple
Last fruit: elderberry
Fruits from index 1 to 2: ['banana', 'cherry']
'''

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("first_fruit:" , fruits[0])
print("last_fruit:" , fruits[-1])
print("Fruits from index 1 to 2:",fruits[1:3])

'''
Exploring Tuples:
1.Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.

- "Rahul", 25, 5.9

2.Print the second element of the tuple.

Expected Result:
Age: 25
'''

person = ("rahul",25,5.9)
print(person[1])


'''
Understanding Dictionaries:
1.Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.

    "make": "Toyota",

    "model": "Camry",

    "year": 2020,

    "color": "Blue"
2.Print the value associated with the model key.
3.Add a new key called owner and assign it the name "Rahul".
4.Print the entire dictionary.

Expected Result:
Car model: Camry
Updated car dictionary: {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Rahul'}
'''

car = {"make": "Toyota",

       "model": "Camry",

       "year": 2020,

       "color": "Blue"}

print("Car model:", car["model"])
car["owner"] = "rahul"
print("Updated car dictionary:", car)

print(car)