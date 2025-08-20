import time
print("Hello, World!")
username = "JohnDoe"
print(f"Welcome, {username}!")



'''
>>> f = open('first.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("Hello, World!")\n'
>>> 
>>> f.readline()
'\n'
>>> f.readline()
'username = "JohnDoe"\n'
>>> f.readline()
'print(f"Welcome, {username}!")'
>>> f.readline()
''
>>> f = open('first.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("Hello, World!")\n'
>>> f.__next__()
'username = "JohnDoe"\n'
>>> f.__next__()
'print(f"Welcome, {username}!")'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration



>>> for line in open('first.py'):
...     print(line, end=" ")
... 
import time
 print("Hello, World!")
 username = "JohnDoe"
>>> nt(f"Welcome, {username}!")


>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')                             
...     
 for line in open('first.py'):
...     print(line, end=" ")
...
import time
 print("Hello, World!")
 username = "JohnDoe"
>>> nt(f"Welcome, {username}!")


>>> test = "hari"
>>> if not test:
...     print("chai")
... 
>>> test = ""
>>> if not test:
...     print("chai")
... 
chai


>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x000001E9BC26ADA0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x000001E9BC26ADA0>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-34>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration

>>> f = open('first.py')
>>> iter(f) is f # the iter function returns the iterator object itself
True
>>> iter(f) is f.__iter__()
True


>>> myNewList = [1, 2, 3]
>>> iter(myNewList) is myNewList
False 


>>> D = {'a':1, 'b':2}
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x000001E9BC7C8900>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<python-input-46>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration


>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-56>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration

'''