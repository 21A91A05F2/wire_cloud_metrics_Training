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

# import math as m
# print(m.sqrt(49))


# working with the dictoinaries:

# Key-value pair:

# Accessing of the key-value pair:

# student = {"name":"shiva","age":23}
# print(student["name"])
# for v,k in student.items():
#     print("key vlaue Pair:",v,k)

# for i in student.keys():
#     print("Key value pair:",i)

# for i in student.values():
#     print("Values:",i)


# num = (1,2,3,4,5,5)
# print(num)
# # print(type(num))
# num.add(1)
# print(num)

#file manipulation:

# string methods:

# s = " Om namashivaya "
# print(s.upper())
# print(s.lower())
# print(s.strip())
# print(s.replace("Om","OM"))

#string concatenation and formating:

# name = "Alice"
# age = 22
# print("My name is"+" "+ name+" " +"and I am"+" "+ str(age)+" "+"years old")
# print(f"My name is {name} and I am {age} years old.")


#spliting and joining strings:

# s = "Python is fun"
# w = s.split() #list of the sentence 
# print(w)
# # print(" ".join(w))
# print("@".join(w))

# #file handling in python:
# f = open("example.txt","w")
# f.write("Hello, I am sireesha.")
# f.close()

# with open("example1.txt","w") as file:
#     file.write("Hello world!")


# Reading of the file:
# f = open("example.txt","r")
# c= f.read()
# print(c)
# f.close()

# with open("example.txt","r") as f:
#     print(f.read())

# c) writing of the file and appending:

# with open("example.txt","a+") as f:
#     f.write("Appending the new data")
#     f.seek(0)  # for moving of the pointer to the start or the index they mentioned
#     print(f.read())

# with open("example.txt","r") as f:
#     print(f.read())

#reasing of the each line by line in the python:

# with open("example.txt","r") as file:
#     for line in file:
#         print(line.strip(),'\n')

# for accesing and printing in new line by using the "."
# with open("example.txt","r") as f:
#     for line in f:
#         s = line.split('.')
#         for i in s:
#             i = i.strip()
#             if i:
#                 print(i)


#handling Errors with Try and except:
# try:
#     with open("example2.txt","r") as f:
# #         print(f.open())
# # except FileNotFoundError:
# #     print("Please check the file name and try again")




# #File Handling using the try and except:

# try:
#     n = int(input())
#     print(n**2)
# except ValueError:
#     print("Invalid input")
# except Exception as e:
#     #here e except that will catch the object of the error and that will display the obj catch in the exception and it will display it .
#     print(f"Unexpected error: {e}")

#  input: siri
# output:  Unexpected error: invalid literal for int() with base 10: 'siri'


# # Python Deburger:

# import pdb
# def faulty_function(x):
#     pdb.set_trace()
#     return x/0

# faulty_function(10)
# #n -> Excurte next line
# #p -> print variable in next line
# #q -> quiting Deberging


# Logging insted of print():

# Logging provides better error tracking and debugging

# import logging
# logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         logging.error("Division by Zero is not allowed.")
#         return None

# print(divide(10,0))

#Pandas: used for the handling and analyzing structured data(tables, CSV files and adatabases).
#Numpy : used for the efficient numerical computations with arrays and mathematical functions.

import json

json_data = '{"name" : "Alice", "Age" : 25}'

python_data = json.loads(json_data)

# for index, value in python_data.items():
#     print(index , value)

print(*python_data.items())