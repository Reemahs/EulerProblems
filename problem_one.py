# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:49:15 2017

@author: Shameer Omar
@purpose: Solution to Euler Problem 1
"""

sum = 0

for loopCounter in range (0, 1000):
    if ((loopCounter%3 == 0) & (loopCounter%5 == 0)):
        print (repr(loopCounter) + ' is a multiple of 3 and 5.')
        sum = sum + loopCounter
    elif (loopCounter%5 == 0):
        print (repr(loopCounter) + ' is a multiple of 5.')
        sum = sum + loopCounter
    elif (loopCounter%3 == 0):
        print (repr(loopCounter) + ' is a multiple of 3.')
        sum = sum + loopCounter
    else:
        print (repr(loopCounter) + ' is not a multiple of 3 or 5.')
        
print ('Sum of multiples of 3 and 5 for numbers below 1000 is: ' + repr(sum))