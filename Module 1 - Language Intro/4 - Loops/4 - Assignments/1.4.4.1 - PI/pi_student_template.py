import math
from ctypes import c_int16
from ftplib import parse150
from stringprep import b1_set

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""
def square(x) : return x*x
# modify these lines to correct set the variable values
a = 1
b = 1/math.sqrt(2)
t = 0.25
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """
    ### YOUR CODE HERE ###

    a1 = (a+b) / 2
    b1 = math.sqrt(a*b)
    p1 = 2 * p
    t1 = t - (p * (square(a1-a)))

    a=a1
    b=b1
    p=p1
    t=t1

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""
# modify this line below to estimate PI
pi_estimate = (square(a1+b1))/(4*t1)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
