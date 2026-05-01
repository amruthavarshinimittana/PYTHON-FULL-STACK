#generators
#no tuple comprehension in above cases if we remove thoose braces and keep parenthesis then the outcome is generator

'''a=[i for i in range(16)]
print(a)
print(type(a))'''
'''
a=[i for i in range(16)]
print(a)
'''
'''print(*a)
print(type(a))'''


#print(list(a))
#print(tuple(a))
'''print(set(a))'''


'''a generator is also a function which can be used as an iterator(loop) by producing group of values,where we use
yield keyord'''
#yield vs retuen
'''retuern terminates the func where as yield can pass the func and go on with every successive iteration'''

'''
a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))  '''  

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        #yield a
print(*check(a,b))'''    



#yield vs return example:
'''def mygen():
    return "python"
    return "java"
    return "ds"
print(*mygen())'''


'''
def mygen():
    #return "python"
    #return "java"
    #return "ds"
    return "python","java","ds"
print(*mygen())'''


def mygen():
    yield "apple"
    yield "mango"
    yield "grapes"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration













