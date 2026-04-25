#list comprehension:
#syntax:a=[expr for var in collection/range]
'''a=["python","java","dsa"]
a=[i.upper() for i in a]
print(a)'''


'''a=["hyd","vzg","vja"]
a=[i.capitalize() for i in a]
print(a)'''

'''a=[1,2,4,5,6,8,12,13]
a=[i**2 for i in a]
print(a)'''

'''a=[1,2,4,5,6,8,12,13]
a=[i*i for i in a]
print(a)'''

'''a=[1,2,4,5,6,8,12,13]
a=[pow(i,2) for i in a]
print(a)'''



'''n=[ i for i in range(16) if i%2==0]
print(n)'''

'''fruits=["apple","banana","mango","grapes","kiwi"]
fruits=[ i for i in fruits if "a" in i]
print(fruits)'''

'''fruits=["apple","banana","mango","grapes","kiwi"]
fruits=[ i for i in fruits if not "a" in i]
print(fruits)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension

#21(0,20)
#odd numbers mul by 5 and even numbers squares)
'''n=[i*i if i%2==0 else i*5 for i in range(21)]
print(n)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
print(c)'''


'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

















































