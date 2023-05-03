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
    odds=inputs*check
    return np.max(odds)

print(largest_odd(1,3,5,7,2,4,10))
print(largest_odd(2,4,8))

#Lessons here... I am not good at working with python stuff like tuples/lists. Without numpy and vector operations I am lost...