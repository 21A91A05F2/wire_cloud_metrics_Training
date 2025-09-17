# # if Statement
# age = 18

# if age >= 18:
#     print("Your are eligible to vote.")

# #if-else statement:

# age = 16 
# if age >= 18:
#     print("You can vote.")
# else:
#     print("You cannot vote yest.")

# if-elif-else statement:

# score = int(input())
# if score >= 90:
#     print("Grade: A")
# elif score >= 75:
#     print("Grade : B")
# else:
#     print("Grade : C")


# Loops in python:

# for loop: iterating over a sequence.

 

# While loop : Repeates as long as a condition is True

# c  = int(input())
# while c <= 5:
#     print(f"Count {c}")
#     c += 1
# else:
#     print(f"Greater thean the expected value")


# Break and Continue:
#Break for the stoping of the execution 
#Continue is for the skiping of the current iteration

# #Nested Loops:
# #A loop inside another loop.
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(f"i = {i}, j = {j}")



#Functions:

# Defining and calling a Function:
# def greet():
#     print("Hai, I am siri!")
# greet()

#Function with Parameters:

# def greet(name):
#     print("Hello", name)

# greet("Raj")

#Function with Return Value:
# def add(a,b):
#     return  a+b

# r = add(10,12)
# print("Sum: ",r)


# Default and Keyword Arguments:

# def greet(name ="siri"):
#     print("Hello", name)

# greet()     #uses default value
# greet("Sai") #uses provided value 


#Modules:

# 1)Importing Modules:
# build in moudles:
# import math
# print(math.sqrt(16))

#Creating Custom Module:
# access by creating one file and importit in another file and access it 

# #Importing only specific functions
# like from math import sqrt, pi
# only this two will import

#using Aliases (as keyword)

import math as m
print(m.sqrt(49))



