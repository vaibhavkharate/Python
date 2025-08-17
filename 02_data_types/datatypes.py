# Mutable DataTypes
# Mutable data types can be changed after creation.
# Examples include lists, dictionaries, and sets.

# Immutable DataTypes
# Immutable data types cannot be changed after creation.
# Examples include integers, floats, strings, and tuples.





# strings

# following are the some methods that can be used with strings:
    

''' 
    chai = "Masala Chai"

    chai.upper()  # Converts to uppercase
    chai.lower()  # Converts to lowercase  
    chai.strip()  # Removes leading and trailing whitespace

chai2 = "Lemon, ginger, Mint, Masala"
print(chai.split(","))
['Lemon', ' ginger', ' Mint', ' Masala']


>>> chai = "Lemon, ginger, Mint, Masala"
>>> print(chai.split(","))
['Lemon', ' ginger', ' Mint', ' Masala']


>>> chai = "Masala chai"
>>> print(chai.find("chai"))
7
>>> print(chai.find("Chai"))
-1
>>> chai = "Masala Chai Chai Chai Chai"
>>> print(chai.count("Chai"))
4

>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} Chai"
>>> order
'I ordered {} cups of {} Chai'  // # This is a string with placeholders
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala Chai



>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety))
Lemon Masala Ginger
>>> print(", ".join(chai_variety))
Lemon, Masala, Ginger
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger

>>> chai = "Masala chai"
>>> chai
'Masala chai'
>>> print(len(chai))
11
>>> chai
'Masala chai'
>>> for letter in chai:
...     print(letter)
...     
M
a
s
a
l
a

c
h
a
i



>> chai = "He Said, \"Masala chai is awesome\""
>>> chai
'He Said, "Masala chai is awesome"'
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> chai
'c:\\user\\pwd'

>>> chai = "Masala Chai"
>>> print ("Masala" in chai)
True
>>> print ("Masalaa" in chai)
False


 '''


'''''# lists

>>> tea_varities = ["Black", "Green", "Oolang", "White"\
]
>>> tea_varities
['Black', 'Green', 'Oolang', 'White']
>>> print (tea_varities)
['Black', 'Green', 'Oolang', 'White']
>>> print (tea_varities[0])
Black
>>> print (tea_varities[2])
Oolang
>>> print (tea_varities[:3])
['Black', 'Green', 'Oolang']
>>> tea_varities[3] = "Herbal"
>>> print (tea_varities)
['Black', 'Green', 'Oolang', 'Herbal']

>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolang', 'Herbal']
>>> tea_varities[1:3] = ["Green", "White"]
>>> tea_varities
['Black', 'Green', 'White', 'Herbal']


>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1] = ["Test", "Test"]
>>> tea_varities
['Black', 'Test', 'Test', 'Green', 'White', 'Herbal']   
>>> tea_varities[1:2]
['Test']
>>> tea_varities[1:3]
['Test', 'Test']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'Green', 'White', 'Herbal']


>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> for tea in tea_varities:
...     print(tea)                                      
...     
Black
Green
White
Herbal
>>> for tea in tea_varities:
...     print(tea, end="-")
... 
>>> k-Green-White-Herbal-


>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'Green', 'White', 'Herbal', 'Oolong']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
I have Oolong tea

>>> tea_varities.pop()
'Oolong'
>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> tea_varities.remove("Green")
>>> tea_varities
['Black', 'White', 'Herbal']
>>> tea_varities.insert(1, "Green")
>>> tea_varities
['Black', 'Green', 'White', 'Herbal']
>>> tea_varities_copy = tea_varities.copy()   # Creates a shallow copy of the list i.e. a new list with the same elements


>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_nums = [y**3 for y in range(8)]
>>> cube_nums
[0, 1, 8, 27, 64, 125, 216, 343]

'''