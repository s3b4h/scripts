Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help
In this section you learned that:

Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)

***********************************************************************

Summary: Positive/Negative Indexes, Slicing
In this section you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'

****************************************************************************8

Conditionals

Bonus Code: Using "and" and "or" in a Conditional
You learned to check for one single condition:

x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")
You can also check if two conditions are met at the same time using an and operator:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
That will return Yes since x == 1 and y ==1 are both True.

You can also check if one of two conditions are met using an or operator:

x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

#####

Summary: Functions and Conditionals
In this section you learned to:

Define a function:

def cube_volume(a):
    return a * a * a
Write a conditional block:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
Write a conditional block of multiple conditions:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
Output is Yes since both x and y are 1.

Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
Output is Yes since x is 1.

Check if a value is of a certain type with:

isinstance("abc", str)
isinstance([1, 2, 3], list)
or

type("abc") == str
type([1, 2, 3]) == lst

#####################################################################################

Summary: Processing User Input
In this section you learned that:

A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")
The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.

You can also format strings with (Python 3 only):

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.


#############################################

For Loop Over a Function
Note that using loops you can call any function multiple times, even your own functions. Let's suppose we defined this function:

def celsius_to_kelvin(cels):
    return cels + 273.15
That is a function that gets a number as input, adds 273.15 to it and returns the result. A for loop allows us to execute that function over a list of numbers:

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
The output of that would be:

282.25
281.95
3.0

So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

That's just something to keep in mind.



##########################################

Bonus Code: Dictionary Loop and String Formatting
You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


###############################################

Summary: Loops
In this section you learned that:

For loops are useful for executing a command over a large number of items.

You can create a for loop like so:

for letter in 'abc':
    print(letter.upper())
Output:

A
B
C

The name after for (e.g. letter) is just a variable name



You can loop over dictionary keys:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
Output:

John Smith
Marry Simpsons

You can loop over dictionary values:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
Output:

+37682929928
+423998200919

You can loop over dictionary items:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
Output: 

('John Smith', '+37682929928')

('Marry Simpons', '+423998200919')



While loops will run as long as a condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.

#########################################################


Summary: List Comprehensions
In this section you learned that:

A list comprehension is an expression that creates a list by iterating over another container.

A basic list comprehension:

[i*2 for i in [1, 5, 10]]
Output: [2, 10, 20]

List comprehension with if condition:

[i*2 for i in [1, -2, 10] if i>0]
Output: [2, 20]

List comprehension with an if and else condition:

[i*2 if i>0 else 0 for i in [1, -2, 10]]
Output: [2, 0, 20]

