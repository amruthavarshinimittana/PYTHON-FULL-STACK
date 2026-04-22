Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,7.8,"hi",6=9j,True,False}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a={3,7.8,"hi",6+9j,True,False}
print(a)
{False, True, (6+9j), 3, 7.8, 'hi'}
a={5,6,7,8,9,10}
a.add(10)
a
{5, 6, 7, 8, 9, 10}
#issubset()
a1,2,3,4,5,6}
SyntaxError: unmatched '}'
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False
b.issuperset(a)
False
a.issuperset(b)
True
#union
a={3,4,5,6,7}
b={5,6,7,8,9,10}
a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
#inntersection()
a={2,3,4,5,6,7,8,9}
b={6,8,9,10}
a.intersection(b)
{8, 9, 6}
a={2,3,4,5,6,7,8,9}
b={6,8,9,10}
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.difference(b)
{1, 2, 3}
b.difference(a)
{8, 7}
a={1,3,4,5,7,6}
b={5,6,7,8,9,10}
a.update(b)
a
{1, 3, 4, 5, 6, 7, 8, 9, 10}
b
{5, 6, 7, 8, 9, 10}
b.update(a)
b
{1, 3, 4, 5, 6, 7, 8, 9, 10}
#symmetric difference
a={2,3,4,5,6,7,8,9}
b={6,8,9,10}
SyntaxError: multiple statements found while compiling a single statement
a={3,4,5,6,7,8,9,10}
b={5,6,7,8,9,10,11,12}
a.symmetric_difference(b)
{3, 4, 11, 12}
b.symmetric_difference(a)
{3, 4, 11, 12}
a={11,12,13,14,15,16}
b={7,8,9,10,11,12,13}
a.difference_update(b)
a
{16, 14, 15}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12, 13}
a={2,3,4,5,6,7,8,9,10}
b={4,5,6,7,8,9,10,11}
a.intersection_update(b)
a
{4, 5, 6, 7, 8, 9, 10}
b.intersection_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
a={3,4,5,6,7,8,}
b={1,3,2,4,7,}
a.symmetric_difference_update
<built-in method symmetric_difference_update of set object at 0x000002675D29F060>
a.symmetric_difference_update(b)
a
{1, 2, 5, 6, 8}
b.symmetric_difference_update(a)
>>> b
{3, 4, 5, 6, 7, 8}
>>> #sets pop
>>> a={1,2,3,4,5}
>>> a.pop()
1
>>> a.remove(3)
>>> a
{2, 4, 5}
>>> #discard
>>> a={1,2,3,4}
>>> a.discard(1)
>>> a
{2, 3, 4}
>>> a.copy()
{2, 3, 4}
>>> b=a.copy()
>>> b
{2, 3, 4}
>>> a={7,8,9,0}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b
set()
>>> b.add(30)
>>> b
{30}
>>> a={5,6,7,8}
>>> b={1,2,3,4,5}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
