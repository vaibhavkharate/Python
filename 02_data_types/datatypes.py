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


'''
# dictionaries

# Dictionaries are mutable data types that store key-value pairs.

>>> chai_types = {"Masala":"Spicy", "Ginger":"Zesty", "\
Green": "Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'


>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}


>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key, value in chai_types.items():
...     print(key, value)
... 
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types:
...     print("I have Masala Chai")
... 
I have Masala Chai
>>> print (len(chai_types))
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}



>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"]= "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')


>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy = chai_types.copy()



>>> tea_shop = {
... "chai": {"Masala": "Spicy", "Ginger": "Zesty"},     
... "Tea": {"Green": "Mild", "Black": "Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'

>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}


 '''



''''# Tuples
# Tuples are immutable data types that store ordered collections of items.
# They are defined using parentheses ().
# Tuples can contain mixed data types, including other tuples.
# Tuples are often used to group related data together, such as coordinates or RGB color values.
# Tuples can be unpacked into variables, allowing for easy access to individual elements.
# Tuples can be used as keys in dictionaries, unlike lists.
# Tuples can be iterated over, allowing for easy access to each element in the tuple.
# Tuples can be concatenated with other tuples to create new tuples.
# Tuples can be sliced to create new tuples with a subset of elements.



# Tuples are immutable, meaning their elements cannot be changed after creation.
# This immutability makes tuples suitable for use as keys in dictionaries and elements in sets.
# Tuples can be created using parentheses () or the tuple() constructor.

>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> len(tea_types)
3


>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')     
>>> if "Green" in all_tea:
...     print("I have green Tea")                       
...     
I have green Tea
>>> more_tea = ("Herbal", "Earl Grey", "Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herb")
0
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolang) = tea_types
>>> black
'Black'
>>> type(tea_types)
<class 'tuple'> 


'''