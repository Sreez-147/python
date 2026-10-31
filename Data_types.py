# numeric data types
number = 100
percentage = 9.4
c = 2+3j
print(number,type(number))
print(percentage,type(percentage))
print(c,type(c))

# sequence data types
s = "sree"
lst = [10,20,30]
t = (1,2,3,4)
print(type(s),type(lst),type(t))

# boolean data types
# True / False
boole1 = True
boole2 = False
print(type(boole1))
print(boole1+boole2)

# Mapping data types
d = {"name":"codegnan","location":"hyd","branch":4}
print(d,type(d))

# sets data types
s = {1,2,3,4}
print(s,type(s))

# empty data types
lst1 = [] # list() 
t1 = () # tuple()
str1 = "" # str()
d1 = {} # dict()
s1 = set() 
print(lst1,type(lst1))
print(t1,type(t1))
print(str1,type(str1))
print(d1,type(d1))
print(s1,type(s1))
print(type(str()))

# explicit type casting
n = input()
print(n,type(n))
n2 = int(n)
print(n2,type(n2))

# implicit type casting
n1 = 100
n2 = 6.5
print(n1,type(n1))
print(n2,type(n2))
n3 = n1 + n2
print(n3,type(n3)) 

# type converstion 
num = int(input())
s = input()
list1 = list(map(int,input().split(",")))
tuple1 = tuple(map(int,input().split()))
set1 = set(map(int,input().split()))
print(num)
print(s)
print(list1)
print(tuple1)
print(set1)