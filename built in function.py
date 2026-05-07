#built-in functions:

'''
a=3
b=5
print(a,b)'''

'''a=(3,4,5)
print(sum(a))'''

'''a=(45,23)
print(sorted(a))
'''

'''a={1,2,3}
print(type(a))'''

'''
a=(2,3,4)
print(min(a))
print(max(a))
print(len(a))
'''

#1.fromkeys()
''''
a="codegnan"
print(a)
print(type(a))
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))


b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"amrutha")
print(b)


b["g"]="python"
print(b)'''





#2.eval()....accepts any data type(int,str,complex,float)
'''
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
'''
while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b)'''
'''
while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''





#3.zip()-> we can combine multiple collections into one collection
'''
a=[10,20,30]
names=["sarvani","amrutha","tripura"]
print(a+names)'''


#wrong...should mention datatype:
'''b=zip(a,names)
print(b)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)


b=dict(zip(a,names))
print(b)'''






#4.ennumerate()-> we can give counter to the collection
'''
names=["tripura","amrutha","sarvani","venkatesh"]
for i in range(len(names)):
        print(i,names[i])'''
'''
b=dict(enumerate(names))
print(b)
b=dict(enumerate(names,100))
print(b)
'''


#5.ASCII
#chr(),ord()     character and order:
'''
n=input("enter name")
for i in n:
    print(i,ord(i))
'''

#annonymous functions(nameless functions):
'''they are nameless funcs and we use a keyword called lambda to create annonymous function'''

#write a function to caclculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)    
    
def f():
    x=int(input("value"))
    print(2*x+5)
f()    
          
'''
#syntax
#a=lambda arg:expr
'''
a=lambda x:2*x+5
print(a(5))


a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))
'''

'''
a=int(input("a value"))
b=int(input("b value"))
c=lambda x,y:x-2*y+5
print(c(a,b))

a=3
b=2
c=lambda x,y:x-2*y+5
print(c(3,2))
'''

'''
a="codegnan"
#CODEGNAN
c=lambda a:a.upper()
print(c(a))

b="python course"
a=lambda b:b.title()
print(a(b))'''
'''
a=input("enter your first name:")
b=input("enter your last name:")
c=lambda a,b:((a+" "+b).title())
print(c(a,b))'''

'''
a,b=[x for x in input("enter names").split(",")]
c=lambda a,b:((a+" "+b).title())
print(c(a,b))'''

'''
#filter()
a=[2,5,6,7,9,8,10]
b=list(filter(lambda a:a%2==0,a))
print(b)


#to remove empty
a=[(),{},None," ",set(),7,7+3j,"python",True,False]
b=list(filter(None,a))
print(b)'''


#map() each object from a collection forms a new collection
'''
a=[2,3,5,7,9,10,11,13,15]
b=[2,1,2,4,5,6,7,8,9]
c=list(map(max,a,b))
d=list(map(min,a,b))
print(c)
print(d)'''


'''a=input("data1")
b=input("data2")
print(a+b)

a,b=input("enter the names").split(",")
print(a+b)

a,b=[x for x in input("names").split(",")]
print(a+b)

a=int(input("a value"))
b=int(input("b value"))
print(a+b)

a,b=[int(x) for x in input("values").split(",")]
print(a+b)


a,b=map(str,input("enter values").split(","))
print(a+b)


a,b=map(int,input("enter values").split(","))
print(a+b)

a=list(map(int,input("enter values").split(","))
print(a)
print(type(a))       


a=tuple(map(int,input("enter values").split(","))
print(a)
print(type(a))   


a=set(map(int,input("enter values").split(","))
print(a)
print(type(a))  ''' 

'''
a=set(map(int,input("enter values").split(","))
print(a)
print(type(a))   



a=list(map(eval,input("enter values").split(","))
print(a)
print(type(a))'''


'''
d = dict(map(lambda x: x.split(':'), input().split()))
print(d)
print(type(d))'''

'''
a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''


'''
a=int(input("enter the keys  and value pairs"))
b=dict((lambda:(input("keys"),input("values")))()for _ in range(a))
print(b)'''





























































































