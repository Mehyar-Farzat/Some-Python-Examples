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
