#function: a function  is a block of organised, reusable code and that is used to perform a single or multiple tasks.
#Python gives in built function  like print,you can make your one function also. These are called user defined functions
#A function block begins with  keyboard def followed by the function and parenthesis (())


'''a=10
b=20
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)'''

#functions:
'''
def calculate(a,b):
    print("the sum is",a+b)
    print("the difference is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''
    
'''
def calculate(a,b):
    print("the integer division is",a//b)
    print("the remainder is",a%b)
    print("the power is",a**b)
calculate(20,10)
calculate(28,4)
calculate(10,2)'''

#print vs return: print just shows the human user output in a console(place where op displays)
#return is a keyword and is used to terminate the function and gives back a value from the function
'''
def add(a,b):
    print(a+b)
add(4,5)'''    

    
'''
while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''
def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''

#print vs return

'''
def sub(a,b):
    return a-b
print(sub(2,9))'''


'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''    

    

'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,5))'''



#split bill


'''
def splitbill():
    total_amount=int(input("enter the total bill"))              
    members=int(input("enter the members"))
    per_person=(total_amount//members)            
    return per_person
print(splitbill())'''



'''
def splitbill():
    total_amount=int(input("enter the total bill"))              
    members=int(input("enter the members"))
    per_person=(total_amount//members)            
    print(f"the bill is {per_person}")
    print("the bill is {}".format(per_person))
splitbill()'''


'''
def splitbill():
    total_amount=int(input("enter the total bill"))              
    members=int(input("enter the members"))
    per_person=(total_amount//members)            
    print(f"the bill is {total_amount//members}")
    print("the bill is {}".format(total_amount//members))
splitbill()'''


'''
def operation():
        a=int(input("enter the a value:"))
        b=int(input("enter the b value:"))
        c=int(input("choose option:\n1.add\n2.sub\n3.mul"))

        if c==1:
            print("the sum is:",(a+b))
        elif c==2:
            print("the sub is:",(a-b))
        elif c==3:
            print("the mul is:",(a*b))
        else:
        print("invalid")
        
    operation()'''
    
'''
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    c=int(input("choose option:\n1.add\n2.sub\n3.mul"))
    if c==1:
       add()
    elif c==2:
       sub()
    elif c==3:
       mul()
    else:
        print("invalid")'''



#railway ticket:
'''
while True:
    def calculate_ticket():
        ticket = 1000
        gender=input("Enter your gender:")
        age=int(input("Enter your age:"))
        if gender.lower() == "male":
            if age > 60:
                fare = ticket - (ticket * 30 / 100)
                print("Senior Citizen Male")
                print("Ticket Price =", fare)
            else:
                print("Normal Male")
                print("Ticket Price =", ticket)

        elif gender.lower() == "female":
            if age > 60:
                fare = ticket - (ticket * 50 / 100)
                print("Senior Citizen Female")
                print("Ticket Price =", fare)
            else:
                fare = ticket - (ticket * 30 / 100)
                print("Female")
                print("Ticket Price =", fare)

        else:
            print("Invalid Gender")

    calculate_ticket()'''


#keyword and positional arguements
'''
def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id="id",name="name",mailid="mailid")
Details(id="id",name="name",mailid="mailid")'''    


'''
def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="gayatri",mailid="g@gmail.com")
Details(id=30,name="bhanu",mailid="bhanu@gmail.com")
Details(40,"tripura","t@gmail.com")
Details("amrutha","a@gmail.com",50)
Details(name="sarvani",mailid="s@gmail.com",id=60)'''



#default arguements
'''
def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("sugar",200)'''    

    

'''
def grocery(item="rice",price=500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''

'''
def grocery(item,price=500):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("ghee")'''


'''
def grocery(item="dal",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(200)'''

#cake,price,qty:

'''
def bakery(cake,price,qty):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %d" %qty)
bakery("chocolate cake",800,1)'''



'''
def bakery(cake,price,qty=1):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %d" %qty)
bakery()'''

'''
def bakery(cake="choco cake",price=800,qty=1):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %d" %qty)
bakery()'''


# * arguements-> * is used to unpack the elements
'''
a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''
b=(1,2,3,4,5)
print(b)
print(*b)'''

'''c={5,6,7,8,9}
print(c)
print(*c)'''

'''
d={"year":2026,"month":4}
print(d)
print(*d)'''#only keys will be printed


'''
a="codegnan"
print(a)
print(*a)'''#will print with spaces btwn letters


'''
a,b,c=2,3,4,6,7,8
print(a)
print(b)
print(c)'''#value error

'''
a,b,c=2,3,4,5,6,7,8,9,10,11,12
print(*a)
print(b)
print(c)'''#more than expected



'''
a,b,c="cod"
print(a)
print(b)
print(c)'''

'''
a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''


#body mass index:
'''
def bmi():

     height=float(input("enter your height in m's:"))
     weight=float(input("enter your weight in kg's:"))

     body_mass_index=(weight)/((height**2))
     print(body_mass_index) 

     if body_mass_index <18.5:
         print("under weight")
     elif body_mass_index >=18.5 and body_mass_index<=24.5 :
         print("healthy weight")
     elif body_mass_index >24.5 and body_mass_index<=29.5:
         print("over weight")
     else:
         print("obesity")
bmi()'''



#VARIABLE LENGTH ARGUEMENTS:
#THEY ARE AUTO-MATICALLY STORED IN TUPLES AND WE USE STAR ARGUEMENTS
'''
def check(*a):
     print(a)
     print(type(a))

check()
b=(2,3,4,5,6,7)
check(*b)


c={4,5,6,7,8}
check(*c)



d={"name":"pooja","year":2026}
check(*d)'''

'''
def check1(*a):
     d=2#creating a variable
     print(a)
     print(type(a))
     for i in a:
          if type(i) in (int,float):
              d=d+i

              print(d)
check1()
check1(2,3,4,5)
check1(2,3,4,5.6,6.2)
check1(1,2,3.4,"pooja")'''


#kwargs(**)
'''
def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''
    

'''
def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''


#both * and ** usage:
'''
def final(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+1
        print(d)
    for i,j in b.items():
        print("key is" ,i)
        print("value is",j)
final()
data=(2,3,4,5.3,3.5)
final(*data)
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
final(**details)
final(*data,**details)'''

#global and local variables:

#variables inside and outside the function are called global and local variables
#a variable is defined above a function and is accessible to entire global space is called a global variable
#variable defined inside a function is called local variable

#first case of global variable
a=5
'''
def check():
    print("inside value is:",a)
check()
print("outside value is",a)'''

#second case of global variable
'''
a=7
def check1():
    a=5
    a=a**2
    print("inside value is:",a)
check1()
print("outside value is:",a)'''

#third case of both global and local variables
'''
a=2
b=9
def check2():
    a=4
    print("insde value is :",a)
    a=10
    print("updated value is :",a+5)
    b=12#local variable
    b=b+a
    print("b value is ",b)
check2()
print("value of a is :",a)
print("value of a is :",b)'''



#usage of global keyword:
'''when the user wants to access the global variable inside thefunction directly and carry forward the the updated
value even outside the func the we need to use global keyword'''


'''
a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is ",b)'''
























    































































