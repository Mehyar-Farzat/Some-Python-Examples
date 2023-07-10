
# Example 1: Add Two Numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2
# Display the sum
print((f'The sum of {num1} and {num2} is {sum}'))

# output
The sum of 1.5 and 6.3 is 7.8
--------------------------------------------------
# Example 2: Add Two Numbers With User Input

# Store input numbers
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Add two numbers
sum = num1 + num2

# Display the sum
print((f'The sum of {num1} and {num2} is {sum}'))

# output
Enter first number: 5
Enter second number: 6
The sum of 5 and 6 is 11
---------------------------------------------------
# Python Program to Swap Two Variables

# Using a temporary variable:

x = 5
y = 10

x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

swap = x
x = y
y = swap

print(f'The value of x after swapping is: {x}')
print(f'The value of y after swapping is: {y}')

# output
The value of x after swapping: 10
The value of y after swapping: 5

# Without Using Temporary Variable :

x = 5
y = 10

x, y = y, x
print('x =', x)
print('y =', y)

# output
x = 10
y = 5
-------------------------------------------------
# Check if a Number is Positive, Negative or 0
# Using if...elif...else

x = int(input('Enter a number '))
if x > 0:
        print('Positive number')
        
elif x == 0:
    print('Zero')
else:
    print('Negative number')
-------------------------------------------------
# calc the area of circle by radius

radius = int(input('Enter a value of radius: '))
area = radius * radius * 3.14159
print('The area of the circle', radius ,'is', area)
-------------------------------------------------
# print the letters of the entered text
# one under the other on Python?

word = 'FREEDOM'
for char in word:
        print(char)
--------------------------------------------------

# let’s ask the user about their choice of cinema or theater.
# You have to pay 10 dollars to watch movies and 5 dollars for theater.
# We think that students get 50% discount.
# If the student is discounted; If he is not a student,
# let’s write a document that calculates the non-discounted
# amount and prints it.

selection = input(' Hello, press (1) for Cinema, (2) for Theater ')
student = input('Are you student (Y/N) ')
price = 0
if selection == '1':
        price = 10
elif selection == '2':
        price = 5

if student == 'Y' or student == 'y':
        price = price / 2

print(f'The fee you have to pay is : {price}')
----------------------------------------------------------

# calculate the increased salary of the worker whose salary
# and raise rate is entered

newsalary = 0
salary = int(input("enter new salary : "))
rais = input("salary rais rate(%) : ")
newsalary = int(salary)+(int(salary)*int(rais)/100)
print("increased salary :",newsalary)
----------------------------------------------------------

# Print Monthly Calendar using calender module
import calender
yy = 2023
mm = 8
print(calender.month(yy,mm))

August 2023
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

# Print Whole Year Calendar

import calender
print(calender.calender (2023))

2023

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
-----------------------------------------------------------------------

# Print the Current Time and Date

import datetime

current_time = datetime.datetime.now()

print("Current Time =", current_time)

print(f'Current Time ',current_time.strftime("%H:%M:%S"))
--------------------------------------------------

# Create Olympic Logo using turtle modules

import turtle

turtle.color('blue')
turtle.penup()
turtle.goto(-110 , -25)
turtle.pendown()
turtle.width(5)
turtle.circle(45)

turtle.color('black')
turtle.penup()
turtle.goto(0 , -25)
turtle.pendown()
turtle.circle(45)
turtle.width(5)

turtle.color('red')
turtle.penup()
turtle.goto(110 , -25)
turtle.pendown()
turtle.circle(45)
turtle.width(5)

turtle.color('yellow')
turtle.penup()
turtle.goto(-55 , -75)
turtle.pendown()
turtle.circle(45)
turtle.width(5)

turtle.color('green')
turtle.penup()
turtle.goto( 55 , -75)
turtle.pendown()
turtle.circle(45)
turtle.width(5)

turtle.done()
-----------------------------------------------
# Turtle star

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
------------------------------------------------
# creat a sample Calculation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter first number : '))
        num2 = float(input('enter second number : '))
    else:
        print('invalid input. Please enter a correct choice.')

    if choice == '1' :
        print(num1 , '+' , num2 , '=' , add(num1 , num2))

    elif choice == '2':
        print(num1 , '-' , num2 , '=' , subtract(num1 , num2))

    elif choice == '3':
        print(num1 , '*' , num2 , '=' , multiply(num1 , num2))

    elif choice == '4':
        print(num1, '/' , num2 , '=' , divide(num1 ,num2))

    next_step = input('Do you want to calculate agine? (yes or no): ')

    if next_step == 'no':
        break
    
else:
    print('Invalid Number')
--------------------------------------------------------------------------

even_numbers = []
odd_numbers = []

for i in range (1 ,101 ):
    if i % 2 == 0 :
        even_numbers.append(i)
        
    else:
        odd_numbers.append(i)

even_list = (even_numbers)
odd_list = (odd_numbers)

print(even_list)
print(odd_list)
        
----------------------------------------------------------    

even_numbers = [i for i in range(1, 101) if i % 2 == 0]
odd_numbers = [i for i in range(1, 101) if i % 2 != 0]

even_list = (even_numbers)
odd_list = (odd_numbers)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

---------------------------------------------------------

numbers = range(1, 101)
even_numbers = []
odd_numbers = []
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])
    i += 1

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
-----------------------------------------------


names = ['Ahmed', 'Ali', 'Adam', 'Mustafa']
length = []

for name in names:
    length.append(len(name))

print(length)

-------------------------------------------------
names = ['Ahmed' , 'Ali' , 'Adam' , 'Mustafa']
length = [len(name) for name in names]
print(length)


-------------------------------------------------


names = ['Ahmed', 'Ali', 'Adam', 'Mustafa']
length = []

i = 0
while i < len(names):
    length.append(len(names[i]))
    i += 1

print(length)



# Write a program to accept a number from a user
# and calculate the sum of all numbers from 1 to a given number

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num + 1):
    sum += i

print("The sum of all numbers from 1 to", num, "is", sum)
-----------------------------------------------
# Given two integer numbers return their product only if the product is
# equal to or lower than 1000,else return their sum.

def mul_sum(num1 , num2):
        product = num1 * num2
        if product <= 1000 :
                return product
        else:
                return num1 + num2

result = mul_sum()
print(result)
----------------------------------------------
# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

previous = 0
for i in range(1, 11):
    current = i
    total = current + previous
    print(total)
    previous = current
-------------------------------------------------
# print the area of Triangle

def tri_area(base , height):
    return (base * height)/2

area = int(tri_area(3 ,2))
print(f'the area is :{area}')
-----------------------------------------
# given age in years and get age in days

def calc_age(age):
    return age * 365

result = calc_age(30)
print(result)

--------------------------------------------
# convet hours to seconds

def how_many_seconds(hours):
    return hours * 3600

seconds = how_many_seconds(2)
print(seconds)
--------------------------------------------
# convert string to int

def string_to_intiger(string):
    return int(string)

result = string_to_intiger('1000')
print(result)


-------------------------------------------

# a farmer is asking you to tell him how many legs can be counted
# among all his animals. The farmer breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for
# each species. You have to implement a function that returns the total number of legs of all the animals.

leg1 = int(input('Enter number of chickens : '))
leg2 = int(input('Enter number  of cows : '))
leg3 = int(input('Enter number  of pigs : '))

def animals(chickens, cows, pigs):
    return chickens * 2 + cows * 4 + pigs * 4

result = animals(2, 3, 5)
print(result)

----------------------------------------------------
# get first element and put it in list

def get_first_value(numbers):
    
    return [numbers[0]]


mylist = [1,2,3]
result = get_first_value(mylist)
print (result)
-----------------------------------------------------






