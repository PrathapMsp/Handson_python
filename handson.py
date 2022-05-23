
#Activity-1

print ('hello world'); #1

a = int(input("enter first number"))
b = int(input("enter second number"))
c = a+b
print (c) #2

import math
x = math.sqrt(25)
print(x) #3

base = int(input("enter the base"))
height = int(input("enter the height"))
area = 0.5*(base*height)
print(area) #4

import cmath
a = int(input("enter the value for a"))
b = int(input("enter the value for b"))
c = int(input("enter the value for c"))
q = (b**2) - (4*a*c)
print(q)
a1 = (-b - cmath.sqrt(q))/(2 * a)
a2 = (-b + cmath.sqrt(q))/(2 * a)
print ("the roots are",a1,"and",a2) #5

a=int(input("enter the value for a"))
b=int(input("enter the value for b"))

print("before swapping a=",a,"b=",b)
a,b=b,a
print(print("after swapping a=",a,"b=",b) #6

import random
print(random.randint(7,17)) #7
      
km = float(input("Enter the value for kilometers"))
cfact = 0.621371
miles = km*cfact
print(miles) #8

c1 = float(input("Enter the Temperature value in degree Celsius: " ))
f1 = (c1 * 1.8) + 32
print('The %.2f degree Celsius is equal to %.2f Fahrenheit' %(c1, f1)) #9

print("Hello", end=" ")
print("Have a nice day") #10


#Activity-2


num = int(input("Enter the number"))
if(num>0):
    print("The given number is Positive")
elif(num<0):
    print("The given number is Negative")
else:
    print("The given number is Zero") #1
    
      
num = int(input("Enter the number"))
if(num%2==0):
    print("The given number is Even")

else:
    print("The given number is odd") #2


Year = int(input("Enter the number: ")) 
  
if((Year % 400 == 0) or  (Year % 100 != 0) and  (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
   
else:  
    print ("Given Year is not a leap Year") #3 
    

a = int(input("Enter the value for a"))
b = int(input("Enter the value for b"))
c = int(input("Enter the value for c"))
if(a>b) and (a>c):
    print("a is greater number")

elif(b>a) and (b>c):
    print("b is  greater number")
else:
    print("c is greater number") #4


num =int(input("enter the number"))
         
for i in range(2,num):
    if num%i==0:
        print('the given number',num,'is not a prime number')
        break

else:
     print('the given number',num,'is a prime number')  #5

    
start = int(input("enter the starting number"))
stop = int(input("enter the finishing number"))         

for num in range(start,stop):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num) #6


import math
y = math.factorial(7)
print(y) #7


number = int(input ("Enter the number for  multiplication table: "))  
print ("The Multiplication Table of ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count) #8


n = int(input ("How long you need the sequence to go? "))  
n1 = 0  
n2 = 1  
count = 0  

if n<= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
 
elif n == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(n1)  

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count <n:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count +=1  #9

import math
num = int(input("enter the number"))
num1=int(input("enter the number"))
print (math.pow(num,num1)) #16
        

   









