Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
b="amrutha varshini"
len(b)
16
c=""
len(c)
0
d=" "
len(d)
1

#count()
#no of repeated words count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count(e)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(e)
NameError: name 'e' is not defined
a.count("e")
3
a.count(" ")
3
b= "amrutha varshini"
b.count("i")
2
#find a string
a="codegnan"
a.find("c")
0
a.find("n")
5
b.find("k")
-1
#escape sequences
#\n new line or next line
#\t tab space(4 to8 spaces)
a="name\nmobileno\tmailid\naddress
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno\tmailid\naddress"
print(a)
name
mobileno	mailid
address
b="Name:Amrutha\nMobileNumber:9866587299\nMailid:amruthavarshinimittana@gmail.com\nplace:vijayawada"
print(b)
Name:Amrutha
MobileNumber:9866587299
Mailid:amruthavarshinimittana@gmail.com
place:vijayawada
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
#upper()
a="code"
a.upper()
'CODE'
a.lower()
'code'
a.capitalize
<built-in method capitalize of str object at 0x00007FFD44241C58>
a.capitalize()
'Code'
b="i am in class"
b.capitalize()
'I am in class'
b.title()
'I Am In Class'
a="python"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
a.isendswith("n")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.isendswith("n")
AttributeError: 'str' object has no attribute 'isendswith'. Did you mean: 'endswith'?
a.endswith("n")
True
a.startswith("p")
True
b=amrutha varshini 1234
SyntaxError: invalid syntax
b="amrutha varshini 1234"
b.isalpha()
False
b="amrutha varshini"
b.isalpha()
False
#due to space, it is false
f="ammu@12345"
f.isalnum()
False
#split()
a="I AM LEARNIG PYTHON FULLSTACK"
a.split()
['I', 'AM', 'LEARNIG', 'PYTHON', 'FULLSTACK']
#joint
a.joint()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.joint()
AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
#join
a="ilovechicken"
" ".join(a)
'i l o v e c h i c k e n'
a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'
#strip()
#lstrip(),rstrip()
a="         ammu      "
a.strip()
'ammu'
a.lstrip()
'ammu      '
a.rstrip()
'         ammu'
#concatenation
a="python"
b=
SyntaxError: invalid syntax
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
print((a+" "+b).title())
Python Course
print((a+" "+b.capitalize())


print((a+" "+b).capitalize())
      
SyntaxError: '(' was never closed
print((a+" "+b).capitalize())
      
Python course
#formatting(add additional string)
      
a=2
      
b=3
      
print("THE SUM IS:",a+b)
      
THE SUM IS: 5
city=VISHAKAPATNAM
      
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    city=VISHAKAPATNAM
NameError: name 'VISHAKAPATNAM' is not defined
CITY= "VIZAG"
      
print("city is",city)
      
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print("city is",city)
NameError: name 'city' is not defined
print("city is",CITY)
      
city is VIZAG
#FORMAT
      
#format()
      
a="motu"
...       
>>> b="patlu"
...       
>>> print("hello {}{}.format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {}{}".format(a,b))
...       
hello motupatlu
>>> print("hello {} {}".format(a,b))
...       
hello motu patlu
>>> print("hello {} hello{}".format(a,b))
...       
hello motu hellopatlu
>>> print("hello {} hello {}".format(a,b))
...       
hello motu hello patlu
>>> #fstring
...       
>>> a="amrutha"
...       
... b="varshini"
...       
SyntaxError: multiple statements found while compiling a single statement
>>> d="amrutha"
...       
>>> e="varshini"
...       
>>> print(f"hello {a}{b}")
...       
hello motupatlu
>>> print(f"hello {d}{e}")
...       
hello amruthavarshini
