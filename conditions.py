#conditions
#if comparision by using comparision operators
#<,>,<=,>=,!=,==
'''a=2
b=4
if a<b:
    print("it is less")'''

'''a=2
b=4
if a>b:
    print("it is less")'''

'''a=5
b=10
if a<=b:
    print("true")'''

'''a=7
b=11
if b>=a:
    print("greater")'''
'''a=2
b=4
if a!=b:
    print("it is not equal")'''
'''a=10
b=10
if a==b:
    print("it is equal")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a="python"
if a!="java":
    print("true")'''

'''a="python"
if a=="python":
    print("true")'''

'''a=input("name")
if a=="pooja":
    print("true")'''

#if condition by using logical operators
#and,or,not
'''a=9
b=12
if a<b and b>a:
    print("true")'''


'''a=9
b=12
if a<=b and b>=a:
    print("true")'''

'''a=20
b=30
if a!=b and b==a:
    print("true")'''

'''a=9
b=12
if a!=b or b==a:
    print("true")'''

'''a=6
b=9
if not a<b:
    print("it is less")'''

'''a=6
b=9
if not a>b:
    print("it is less")'''
#identify
#is ,is not
'''a=8
if type(a) is int:
    print("it is int")'''
    
'''a=8
if type(a) is not int:
    print("it is int")'''

'''a=int(input("enter the value:"))
if type(a) is int:
    print("true")'''


#membership
#in not in
'''a=[3,4,5,6,7,8,9]
if 7 in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 7 not in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 10 not in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9,10]
b=int(input("a value"))
if b in a:
    print("true")'''


#if-else conditions by using comparision

'''a=5
b=10
if a<b:
    print("less")
else:
    print("true")'''



'''a=5
b=10
if a==b:
    print("true")
else:
    print("false")'''



'''a=5
b=10
if a!=b:
    print("true")
else:
    print("false")'''

#if else conditions by using logicals
    
'''a=9
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''


'''a=9
b=12
if a!=b and b==a:
    print("true")
else:
    print("false")'''

'''a=15
b=20
if not a<b and b>a:
    print("true")
else:
    print("false")'''

    
#if else condition by using identify operators

'''a=9
if type(a) is int:
    print("it is int")
else:
    print("false")'''

'''a=9
if type(a) is not int:
    print("it is int")
else:
    print("false")'''

'''a=12.9
if type(a) is int:
    print("it is int")
else:
    print("false")'''


#membership (if else)
'''a=[10,20,30,40,50]
if 10 in a:
    print("true")
else:
    print("false")'''

'''a=[10,20,23,40,50]
if 23 not in a:
    print("true")
else:
    print("false")'''


#if elif condition by using comparision

'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")'''


'''a=2
b=4
if a==b:
    print("less")
elif b>a:
    print("greater")'''


'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
elif b==a:
    print("false")'''


# if elif using comparision
'''a=2
b=4
if a<b and b<a:
    print("less")
elif b<a or a>b:
    print("greater")
elif not a==b or a<b:
    print("true")'''


#membership in not in
'''a=[1,2,3,4]
b=[4,5,6]
if a in b:
    print("yes")
elif a not in b:
    print("false")'''

'''a=[21,45,67]
if 63 in a:
    print("yes")
elif 63 not in a:
    print("no")'''


#if elif else
'''a=8
b=9
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''
#and or not logical
'''a=8
b=9
if a<b and a>b :
    print("less")
elif b>a or a>b:
    print("greater")
elif not a!=b:
    print("not equal")
else:
    print("true")'''
#identify
'''a=8
b=9
if type(a) is int:
    print("less")
elif type(a)is not float:
    print("greater")
else:
    print("true")'''



#multiple if condition(comparision)
'''a=3
b=9
if a<b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''
    
#(logical)
'''a=56
b=45
if a>b and b<a:
    print("true")
if a==b or b!=a:
    print("yes")'''

#identify
'''a=56
b=45.6
if type(a) is int:
    print("true")
if type(b) is not int:
    print("yes")'''    


'''a=56
if type(a) is int:
    print("true")
if type(a)is not float:
    print("yes")'''    


#membership in not in

'''a=[1,[2,4,6]]
b=[2,4,6]
if b in a:
    print("yes,it is")
if a not in b:
    print("condition satisfied")'''


'''a=[1,2,4,6]
if 2 in a:
    print("yes,it is")
if 5 not in b:
    print("condition satisfied")'''

#nested if
'''a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")'''
        
'''a=10
b=15
if a>b:
    print("less")
    if b>a:
        print("greater")'''


'''a=5
b=10
if a>b:
    print("less")
    if b==a:
        print("greater")'''


'''a=5
b=10
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")'''

'''a=5
b=10
if a>b:
    print("less")
    if b>a:
        print("greater")
else:
    print("true")'''


'''a=5
b=10
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''
   


'''a=7
b=12
if a<b:
    print("less")
    if a==b:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("true")
else:
    print("false")'''









