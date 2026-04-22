+Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dictionary
>>> #dict{}
>>> a={"name":"amrutha","year":"2026","month":"4"}
>>> print(a)
{'name': 'amrutha', 'year': '2026', 'month': '4'}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['amrutha', '2026', '4'])
>>> a.items()
dict_items([('name', 'amrutha'), ('year', '2026'), ('month', '4')])
>>> a["year"]
'2026'
>>> a.update({"time":5})
>>> a
{'name': 'amrutha', 'year': '2026', 'month': '4', 'time': 5}
>>> # if more than one update then:
>>> a.update({"time":5,"min":15})
>>> a
{'name': 'amrutha', 'year': '2026', 'month': '4', 'time': 5, 'min': 15}
>>> b={'name': 'amrutha', 'year': '2026', 'month': '4'}
>>> b.setdefault("city","vja")
'vja'
>>> b
{'name': 'amrutha', 'year': '2026', 'month': '4', 'city': 'vja'}
>>> a.pop("year")
'2026'
>>> a
{'name': 'amrutha', 'month': '4', 'time': 5, 'min': 15}
>>> #to pop enter key
>>> a.popitem()
('min', 15)
a
{'name': 'amrutha', 'month': '4', 'time': 5}
a.copy()
{'name': 'amrutha', 'month': '4', 'time': 5}
a.get("city")
a.get("name")
'amrutha'
#get is to access
a.clear()
a
{}
b.update({"name":"amrutha"})
b
{'name': 'amrutha', 'year': '2026', 'month': '4', 'city': 'vja'}
a.update({"name":"amrutha"})
a
{'name': 'amrutha'}
#it doesn't allow duplicates
#keys should be different, if values are same also no problem
m={"name":"amrutha","year":"2026","month":"4","name":"amrutha}
   
SyntaxError: unterminated string literal (detected at line 1)
m={"name":"amrutha","year":"2026","month":"4","name":"amrutha"}
   
print(a)
   
{'name': 'amrutha'}
print(m)
   
{'name': 'amrutha', 'year': '2026', 'month': '4'}
n={"name":"amrutha","year":"2026","month":"4","name1":"amrutha"}
   
print(n)
   
{'name': 'amrutha', 'year': '2026', 'month': '4', 'name1': 'amrutha'}
a={"idnos":[10,20,30],"name":["amrutha","sarvani","tripura"]}
   
print(a)
   
{'idnos': [10, 20, 30], 'name': ['amrutha', 'sarvani', 'tripura']}
type(a)
   
<class 'dict'>
a.keys()
   
dict_keys(['idnos', 'name'])
a.values()
   
dict_values([[10, 20, 30], ['amrutha', 'sarvani', 'tripura']])
a.items()
   
dict_items([('idnos', [10, 20, 30]), ('name', ['amrutha', 'sarvani', 'tripura'])])
