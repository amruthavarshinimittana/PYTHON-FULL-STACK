Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #variables
>>> print(5+4)
9
>>> a+3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a+3
NameError: name 'a' is not defined
>>> a=3
>>> b=7
>>> print(a+b)
10
>>> b=6
>>> print b=6
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> x=30
>>> print(x)
30
>>> 10a=40
SyntaxError: invalid decimal literal
>>> a10=40
>>> print(a10)
40
>>> @60
... name=amrutha""mittana
SyntaxError: invalid syntax
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> name="amrutha""mittana"
>>> print(name)
amruthamittana
if=30
SyntaxError: invalid syntax
elif=30
SyntaxError: invalid syntax
_=3
print(_)
3
a=6,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=7;b=3
print(a+b)
10
first_name="amrutha"

print(first_name)
amrutha
del firstname
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del firstname
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
del first_name
print(first_name)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(first_name)
NameError: name 'first_name' is not defined
