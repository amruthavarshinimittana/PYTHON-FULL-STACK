Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int(8)
int(8)
8
int(0.9)
0
int("ammu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("ammu")
ValueError: invalid literal for int() with base 10: 'ammu'
int(2+7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(2+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(3)
3.0
float(9.0)
9.0
float("ammu")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("ammu")
ValueError: could not convert string to float: 'ammu'
float(2+3j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(2+3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(1)
'1'
str(5.8)
'5.8'
str("hlo")
'hlo'
>>> str(5+7j)
'(5+7j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> complex(10)
(10+0j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex("ammu")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex("ammu")
ValueError: complex() arg is a malformed string
>>> bool(1)
True
>>> bool(1.3)
True
>>> bool("hi")
True
>>> bool(3+2j)
True
>>> bool(true)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> bool(True)
True
>>> bool(False)
False
