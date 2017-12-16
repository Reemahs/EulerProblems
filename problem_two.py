# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:19:33 2017

@author: Shameer Omar
@purpose: Solution to Euler Problem 2
"""

fibList = list([1, 1])
loopCounter = 0
evenSum     = 0

if ((int(fibList[0]) % 2) == 0):
    evenSum = evenSum + int(fibList[0])

if ((int(fibList[1]) % 2) == 0):
    evenSum = evenSum + int(fibList[1])

while(fibList[len(fibList) - 1] < 3500000):
    lastFib = fibList[loopCounter] + fibList[loopCounter + 1]
    fibList.append(lastFib)
    
    if((lastFib % 2) == 0):
        evenSum = evenSum + lastFib
    
    loopCounter = loopCounter + 1
    
lastFib = int(fibList[len(fibList) - 1])
print('The last fibanacci value is: ' + repr(lastFib))
print('The sum of the even fibanacci numbers under four million is: ' + repr(evenSum))