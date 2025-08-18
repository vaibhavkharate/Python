'''     

>>> userscore = input("Give me a score value: ")
Give me a score value: 200
>>> userscore
'200'
>>> userscore / 2
Traceback (most recent call last):
  File "<python-input-58>", line 1, in <module>
    userscore / 2
    ~~~~~~~~~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> userscore_in_int = int(userscore)
>>> userscore_in_int
200


'''