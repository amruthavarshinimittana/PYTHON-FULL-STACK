Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print
<built-in function print>
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment operators
\
a=5
b=6
print(b+=a)
SyntaxError: invalid syntax
b+=a
b
11
print(b)
11
b
11
b-=3
b
8
print(b)
8
b*=a
b
40
b//=5
b
8
b/=3
b
2.6666666666666665
b%=4
b
2.6666666666666665
b**4
50.56790123456789
#comparision operators
a=6
b=8
a<b
True
a>b
False
a<=b
True
a>=b
False
b<=a
False
b<=a
False
a!=b
True
a!=b
True
b!=a
True
a==b
False
b==a
False
#logical operators
(and or not)
SyntaxError: invalid syntax
a=7
b=11
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or b!=a
True
a<b not a>b
SyntaxError: invalid syntax
a<b not b>a
SyntaxError: invalid syntax
not a<b
False
not True
False
not False
True
#identify operators
a=5
if type(a) is int:
    print("it is int")

    
it is int
b=6.7
if type (b) is int:



    print("not int")

    

if type(b) is not int:
    print(not int)
    print("not int")

    
False
not int
#membership operator
a=2,3,4,5,6,7,8
if 6 in a :
    print(6)

    
6
if 11 in a:
    print(11)

    
#bitwise operators
    
bin(9)
'0b1001'
a=10
b=20
>>> a&b
0
>>> bin(9)
'0b1001'
>>> bin(10)
'0b1010'
>>> a=4
>>> b=8
>>> bin(4)
'0b100'
>>> bin(8)
'0b1000'
>>> a/b
0.5
>>> a|b
12
>>> a~b
SyntaxError: invalid syntax
>>> a=6
>>> ~a
-7
>>> a=9
>>> b=7
>>> ^
SyntaxError: invalid syntax
>>> ^a
SyntaxError: invalid syntax
>>> a^b
14
>>> a=2
>>> a<<4
32
>>> a=6
>>> a>>2
1
