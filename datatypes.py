Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=4
type(a)
<class 'int'>
b=7.8
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e="""amrutha"""
>>> type(e)
<class 'str'>
>>> d=6+9j
>>> type(d)
<class 'complex'>
>>> g=true
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    g=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> print(g)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(g)
NameError: name 'g' is not defined
>>> g=true
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    g=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=true
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=2+8j
>>> type(a)
<class 'complex'>
>>> a=True
>>> type(a)
<class 'bool'>
