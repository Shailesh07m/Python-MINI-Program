# Write a function that prints “Hello World”.
# def greet():
#     print("Hello World")
# greet()
from itertools import count


#Write a function that takes a number and prints whether it is even or odd.
# def evenorodd(num):
#     if num%2==0:
#         print('Even')
#     else:
#         print('Odd')
#
# evenorodd(8)

#Write a function that takes two numbers and returns their sum.
# def add(a,b):
#     return a+b
# print(add(3,4))

#Write a function that takes a string and returns its length.
# def length(string):
#     return len(string)
# print(length("hello"))

#Write a function that prints numbers from 1 to N
# def printt(n):
#     for i in range(1,n+1):
#         print(i)
#
#
# printt(5)

#Write a function add(a, b) that returns addition.
# def add(a,b):
#     z=a+b
#     return z
# print(add(19,4))

#rite a function area_rectangle(length, breadth) and print the area.
# def rec_area(length,breadth):
#     area = (length*breadth)
#     return area
# print(rec_area(89,5))


#Write a function power(base, exp) to calculate power.
# def power(x,y):
#     return x**y
# print(power(2,3))

# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(maximum(3,4))
# def maximumm(a,b):
#     return max(a,b)
# print(maximumm(3,4))

#rite a function full_name(first, last) that prints full name
# def fullname(fisrt,last):
#     return fisrt+" "+last
# print(fullname("Harry","Kukar"))
# print(fullname("Kukuar","harry"))

# #rite a function greet(name="Guest") that prints a greeting.
# def greeting(tittle,time,name="guest"):
#     print(f"{tittle} {time} {name}")
#
# greeting("Mr.","Good Morning")

#rite a function simple_interest(p, r=5, t=1) and return interest.
# def simple_interest(p,r=5,t=1):
#     si=(p*r*t)/100
#     return si
# print(simple_interest(100000))

#rite a function power(num, exp=2) (default square).
# def power(x,y=2):
#     return x**y
# print(power(3))


#Write a function print_line(char="*", times=10).
# def pattern(char="*",times=10):
#     for i in range(times):
#         print(char*i,end="\n")
#     print()
#
# def patternn(char="*",times=10):
#     for i in range(times):
#         print(char*times,end="\n")
#     print()
# pattern()
# patternn()

# def grert(tittle, first, last):
#     return f"Hello {tittle} {first} {last}"
#
#
# print(grert(tittle="Mr.", first="Nitin", last="Ambani"))
# print(grert(last="Ambani", tittle="Mr.", first="Nitin"))
# print(grert(tittle="Mr.", first="Harry", last="Puttar"))
#
# # write an function student(name,age,marks) and call it using keywords
#
# def student(name, age, marks):
#     print(f"Name:{name} Age:{age} marks={marks}")
#
#
# student(name="Pooooo", age=89, marks=34)
#
#
# # write a function logiin(username,password) and call using keywords
# def logiin(username, password):
#     print("Username :", username)
#     print("Password :", password)
#
#
# logiin(username="NallaPaji009", password="Lassinebhundphaddi")
#
#
# # write an function to calculate area using keywords argument only
# def area(pi, radius):
#     return pi * radius * radius
#
#
# print(f"{area(pi=3.14159, radius=5):.2f}")

#Write a function that takes any number of values and prints them.
# def value(*args):
#     for a in args:
#         print(a,end=" "+"\n")
#
#
# value(1, 2, 3, 4)

#Write a function that returns the sum of all numbers using *args.
# def summ(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
# print(summ(1,2,3,4,5,6))
# def sume(*args):
#     return sum(args)
# print(sume(1,2,3,4,5,6))


#Write a function that finds the maximum number from *args.
# def maximum(*args):
#     maxim=0
#     for i in args:
#         if i>maxim:
#           maxim=i
#     return maxim
# print(maximum(1,2,3,4,98,6,7,8,9))
#
# def maximum2(*numbers):
#     return max(numbers)
# print(maximum2(1,2,3,4,98,6,7,838,9))

#Write a function that counts how many numbers were passed.
# def countt(*num):
#     co=0
#     for i in num:
#         co+=1
#     return co
# print(countt(1,2,3,4,5))
#
# def coun(*num):
#     return len(num)
# print(coun(1,2,3,4,5,8))
#


#Write a function that prints all key–value pairs from **kwargs.
# def key_value(**info):
#     for key,value in info.items():
#         print(f"{key}: {value}")
#
# key_value(Name="Shailesh",age=19,gender="male")


# Write a function that displays student details using **kwargs.
# def student(**info):
#     for key, value in info.items():
#         print(f'{key}: {value}')
#
# student(Name="Shailesh",Classs="S.Y.BBA(CA)",grade="A",age=19,rollno=4527)

#Write a function that counts how many keyword arguments were passed.

# def count_arg(**info):
#     return len(info)
# result=count_arg(Name="Nitin",age=30)
# print('Numebr of argument Passed is ',result)

# Write a function to check if "name" exists in kwargs.
# def check(**info):
#     if info.get("name"):
#         print('Name is Present in Arguments')
#     else:
#         print('Name is not present in Arguments')
#
# check(age=20, name='hi',marks=90)

#Write a function that uses:

# positional + default + *args

# def greet(timee,*args,tittle="Mr."):
#     print(f"Good {timee} {tittle} ",end="")
#     for a in args:
#         print(a,end=" ")

# greet("Morning",'Nitin','Uday','Sumit')

#Write a function that accepts:

# a, b=10, *args

# def accept(a,*args,b=10):
#     print(f"{a} {b} ",end="")
#     for i in args:
#         print(i,end=" ")
#
# accept(28,10,20,30,4080,3289,72723,3727,3772,993,9032)
#

#Write a function that accepts:

# name, *marks, grade="A"
# def result(name,*marks,grade='A'):
#     print(f"Name :{name }",end='\n')
#     print('Marks Obtained :')
#     for m in marks:
#         print(m)
#     print(f'Grade :{grade}')
#     print('----------------------')
#
# result('Nitin',98,95,92,89,88)
# result('Sumit',78,85,89,66,53,grade='B')

# Write a function that accepts:
#
# *args, **kwargs
#
#
# and prints both.

# def arbitary(*single,**double):
#     print('Args Down Here:')
#     for i in single:
#         print(i,end=" ")
#     print()
#     print('Kwargs Down Here:')
#     for key,val in double.items():
#         print(key,val)
#
# arbitary(1,2,4,4,4,3,2,32,3,age=34,lennn=9300)

# Write a function that returns square of a number.
# def sqrt(a):
#     return a**2
# print(sqrt(5))

# Write a function that returns both sum and product
# def sum_pro(a,b):
#     s=a+b
#     pr=a*b
#     return pr , s
# summ,tota=sum_pro(3,4)
# print('sum : ',summ)
# print('total : ',tota)

# ite a function that returns True if number is prime.
# import math
#
#
# def is_prime(n):
#     # 1. Handle small numbers
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#
#     # 2. Eliminate multiples of 2 and 3
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#
#     # 3. Check from 5 up to sqrt(n)
#     # We skip even numbers and multiples of 3
#     limit = int(math.sqrt(n))
#     for i in range(5, limit + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#
#     return True
# print(is_prime(7))

#Write a f(unction that returns the reverse of a string.
# def strrev(string):
#     return string[::-1]
# print(strrev(input("Enter a string: ")))

# Write a function that contains another function to add two numbers.
# def double_fun():
#     a=int(input("enter a number"))
#     b=int(input("enter another number"))
#     def add(a,b):
#         return a+b
#     print('Sum of Number :',add(a,b))
#
# double_fun()

#rite a function that checks even/odd using inner function.
# def num(n):
#     def even(n):
#         if n % 2 == 0:
#             print('Even')
#         else:
#             print('Odd')
#     even(n)
#
# num(6)

# Write a recursive function to find factorial.

# def factorial(n):
#     if n==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# Write a recursive function to find sum of digits.
# def sumof_digit(n):
#
#     if n==0:
#         return 0
#     last_digit = n % 10
#
#     return  last_digit+ sumof_digit(n//10)
# print(sumof_digit(123))

# Write a recursive function to print numbers from 1 to N.
# def print_num(n):
#     if n==0:
#         return
#
#     print_num(n-1)
#     print(n)
#
#
# print(print_num(10))

# write an recursive function for reversing a string
# def reverse_string(s):
#     if s == "":
#         return s
#     return reverse_string(s[1:]) + s[0]
#
# print(reverse_string("abc"))

# Write a function to generate OTP of N digits (default 4).
# import random as r
# def otp():
#     num=[]
#     for i in range(4):
#         n=r.randint(0,9)
#         num.append(str(n))
#     return "".join(num)
# print(otp())

#rite a function that accepts marks of students and returns average.
# print('Pass 6 Subject Marks to Find Average Between (1 to 100):')
# def average(*marks):
#     obtained=sum(marks)
#     total=600
#     return obtained/total * 100
# print(f'{average(65,54,65,78,65,98):.2f}')

# Write a function to calculate bill with default tax.
# def cal_bill(price,tax=0.18):
#     tax_amount=price*tax
#     total=price+tax_amount
#     return total
# print(cal_bill(100))

# Write a function that accepts shopping items using **kwargs and prints bill.
# print('Enter Your Product and its Price')
# def shopping_list(**listt):
#     total=sum(listt.values())
#     print('   Item                         Price')
#     for key,value in listt.items():
#         print(f"{key }                             {value}")
#     print('Total Amt is ₹',total)
# shopping_list(Salt=20,Oil=135,Sugar=40,Biscuits=78,rice=1600)
#
# Write a function that:
#
# Accepts any number of values
#
# Separates numbers and strings
#
# # Returns them in two different lists

# def separate(*args):
#     numbers = []
#     strings = []
#
#     for item in args:
#         if isinstance(item, (int, float)):
#             numbers.append(item)
#         elif isinstance(item, str):
#             strings.append(item)
#
#     return numbers, strings
