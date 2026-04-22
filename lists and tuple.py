Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[4,6.7,"pooja",7+9j,True,False]
print(a)
[4, 6.7, 'pooja', (7+9j), True, False]
type(a)
<class 'list'>
b=9.0
type(b)
<class 'float'>
c=[9.0]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("ml")
a
['python', 'java', 'c', 'c++', 'ml']
a.append(["ds","ai"])
a
['python', 'java', 'c', 'c++', 'ml', ['ds', 'ai']]
a.extend(["html","css"])
a
['python', 'java', 'c', 'c++', 'ml', ['ds', 'ai'], 'html', 'css']
a=["vja","hyd"]
a.insert(1,"vzg")
a
['vja', 'vzg', 'hyd']
a[2]
'hyd'
a=["python","java","c","c++"]
a.index("java")
1
a.copy()
['python', 'java', 'c', 'c++']
a.clear()
a
[]
b=[]
b.append("amrutha")
b
['amrutha']
a=["amrutha","tripura","sarvani","gayatri","bhanu"]
a.sort()
a
['amrutha', 'bhanu', 'gayatri', 'sarvani', 'tripura']
b=[9,7,2,4,7,]
b.sort()
b
[2, 4, 7, 7, 9]
b.reverse()
b
[9, 7, 7, 4, 2]
KeyboardInterrupt
>>> a=["amrutha","tripura","sarvani","gayatri","bhanu"]
>>> a.pop()
'bhanu'
>>> a
['amrutha', 'tripura', 'sarvani', 'gayatri']
>>> a.pop(1)
'tripura'
>>> a
['amrutha', 'sarvani', 'gayatri']
>>> #remove()
>>> a=["chocolate","sweets"]
>>> a.remove("sweets")
>>> a
['chocolate']
>>> a.count("chocolates")
0
>>> b=["python"]
>>> len(b)
1
>>> KeyboardInterrupt
>>> b="python"
>>> len(b)
6
>>> #tuple()
>>> a=(3,4.5,"python",8+9j,True,False)
>>> print(a)
(3, 4.5, 'python', (8+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count("python")
1
>>> len(a)
6
>>> a.index(True)
4
