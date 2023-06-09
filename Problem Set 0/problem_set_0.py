# Assignment:
# Write a program that does the following in order:
#   1. Asks the user to enter a number “x”
#   2. Asks the user to enter a number “y”
#   3. Prints out number “x”, raised to the power “y”.
#   4. Prints out the log (base 2) of “x”.
# Use Spyder to create your program, and save your code in a file named ‘ps0.py’. An example
# of an interaction with your program is shown below. The words printed in blue are ones the
# computer should print, based on your commands, while the words in black are an example of
# a user's input. The colors are simply here to help you distinguish the two components
# Enter number x: 2
# Enter number y: 3
# X**y = 8
# log(x) = 1

import numpy

x=float(input("Enter a number x:"))
y=float(input("Enter a number y:"))

print(x**y)
print(numpy.log2(x))

#input gives a prompt in the terminal and returns the user input as a string. Float tries to cast to a number. Calculations are straight foward. 