
#i = 5

#pi=3.14

#Area= i *3.14

#print("The area of a circle is: ",Area)

#name = input("What is your name: ")
#print (name)

# n1= int(input("Enter the first number: "))
# n2= int(input("Enter the Second number: "))

# Sum = n1 + n2

# print("The sum is: ", Sum)

# Operators in Python
# Arithmetics operators
# addition
# x=5
# result =x + 10
# print(result)

# Subtraction
# x=5
# result =x - 10
# print(result)
# Quotient
# from math import remainder


# x=5
# quotient =x //2
# remainder = x % 2
# print("The quotient is : " , quotient ,"and" ,"the remaider is: " , remainder)
# fee = 4535

# discount = 10

# discount_amount = (discount /100) * fee

# discounted_fee = fee - discount_amount
# print("The fee after discount is : " , discounted_fee)

# from tokenize import Double
# from turtle import distance


# distance_km = 850

# distance_mile = float(distance_km * 0.621371)

# print("The distance in miles is: " , distance_mile)

# Comparison operators
# < Less than
# > Greater than
# == Equal
# != Not equal
# >= Greater than or equal to
# <= Less than or equal to
# 
# Boolean
# True or False
# n=5
# print(n<10)


# Logical Operators
# and True if both operands are True
# or True if either of the operands is True
# not True if the operand is False

# age= 22
# gpa= 3.8

# result = age >= 18 and gpa  > 3.6
# print(result)

# # Decision Making
# Marks = int(input("Enter your marks: "))
# if Marks >= 40:
#     print("You passed the exams , Congratulation")
# elif Marks > 30:
#     print("You failed the unit, take a reseat")

# else:
#     print("You failed the unit, take a repeat")
    
# While Loop
# from itertools import count


# count = 0
# while count <= 5:
#     print(count)
#     count = count + 1

# Multiplication Table

# number = int(input("Enter a number: "))

# count = 1
# while count <= 10:
#     product = count * number
#     print (number,"x",count,"=",product)
#     count = count + 1

# From 10 to 1
# number = int(input("Enter a number: "))
# count = 10
# while count >= 1:
#     product = number* count
#     print (number,"x",count,"=",product)
#     count = count -1

# break and continue    
# for items in range (1,6):
#     if items == 4:
#         break
#     print(items)

# while True:
#     number= float(input("Enter a number: "))
#     if number<0:
#         break
#     print("You entered: " , number)

# continue
# for i in range(5):
#     number= float(input("Enter a number: "))
#     if number < 0:
#         continue
#     print(number)


# from tkinter import PROJECTING


# languages= ["Python","Java","C","Swift","C++"]
# for languages in languages:
#     if languages == "Swift" or languages == "C++" :
#         continue
#     print(languages)

# For Loop
# A sequence in python is a collection of data

# text = "Python"

# for character in text:
#   print(character)

# language = ["German","English","Spanish"]

# for language in language:
#     print(language)

# range in For Loop

# for count in range (1,6):
#     print(count)


# number= int(input("Enter an integer: "))

# for count in range(1,11):
#     product = number *count
#     print(number, "x", count ,"=" ,product)


# from unittest import result

# sum= 0
# for count in range (1,101):
#     sum= sum + count
#     print(sum)

# Pass Statement

number = 5.5

if number > 0.0:
    pass 

# Function in Python
# Group of related statement that perform a  certain task
# def greet():
#     print("Hello")
#     print("How do you do")

# greet()
# Python argument
# def greet(name):
#     print("Hello",name)
#     print("How do you do?")
# greet("Jack")   


# def sum(n1,n2):
#     result= n1 + n2
#     print("The sum is: ", result)

# n1= 5.5
# n2= 6.7
# sum(n1, n2)

# return in python
# def sum(n1,n2):
#     result= n1 + n2
#     return result

# n1= 5.5
# n2= 6.7
# result=sum(n1, n2)
# print("The sum is: ", result)

# Length

# marks = [55,60,69,40,50]

# length = len(marks)
# print("The length is :",length)

# marks_sum = sum(marks)
# print("The sum of the marks is: " ,marks_sum)

# Function to find average marks

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subject= len(marks)
    average_marks= sum_of_marks / total_subject
    return average_marks

# Calculate the grade 
def compute_grade(average_marks):
    if average_marks > 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [55,60,69,40,50]
average_marks = find_average_marks(marks)
print ("Your average marks is : " ,average_marks)

grade = compute_grade(average_marks)
print("Your grade is: " ,grade)