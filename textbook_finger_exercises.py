import numpy as np #because I like math

#Finger exercise the first, pg 18:

# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

def largest_odd(*args):
    #how to check odd/even... mod %
    # x%2 is 0 if x is even, 1 if odd
    inputs=np.array(args)
    check=inputs%2
    if not np.any(check):
        print('all inputs are even')
        return
    odds=inputs*check
    return np.max(odds)

print(largest_odd(1,3,5,7,2,4,10))
print(largest_odd(2,4,8))

#Lessons here... I am not good at working with python stuff like tuples/lists. Without numpy and vector operations I am lost...


#Finger exercise the second, pg. 24

# Replace the comment in the following code with a while loop:
#numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# #concatenate X to toPrint numXs times
# print(toPrint)

# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# k=0
# #concatenate X to toPrint numXs times

# while k+1<=numXs:
#     toPrint=toPrint+'X'
#     k=k+1
# print(toPrint)

#Finger exercise #3:
# Write a program that asks the user to input 10 integers, 
# and then prints the largest odd number that was entered. 
# If no odd number was entered, it should print a message to that effect

# inputString=input("Input integers separated by spaces \n e.g. 1 2 3 5 ...")

# integers=[int(I) for I in inputString.split(' ')]

# largest_input_odd=largest_odd(*integers)
# print(largest_input_odd)

#Annoying that I have to remake the list to cast to int


#Finger exercise #4:
# Write  a  program  that  asks  the  user  to  enter  an  integer  
# and  prints two integers, rootand pwr, such that 
# 0 < pwr < 6
# and root**pwris equal to the integer entered by the user. 
# If no such pair of integers exists, it should print a message to that effect

#I'm going to solve by exhaustive enumeration
# / guess and check since that was the topic at this point in the textbook

integer=int(input("Enter an integer and recieve a root and power such that: \n root^power is your input integer where the power is in [1,5]: "))



for root in range(abs(integer)+1):
    for p in range(1,6):
        if root**p==abs(integer):
            power=p
            break
    else:
        continue
    break
if integer < 0 and power%2!=0:
    root=-root
if root**power!=integer:
    print("No such pair of integers exists such that a^b=input integer where b is in [1,5]")
else:
    print( f'Your input {integer} is {root} raised to {power}')


