# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:43:05 2017

@author: Shameer Omar
Euler Problem - 5
"""

# This function checks if the number provided can be completly divided by the 
def CheckEvenDivisible (number, divisor):
    remainder = number % divisor
    return remainder == 0

# This function sets the intial list to 
def SetList (listSize):
    newList = []
    
    for index in range(listSize):
        newList.append(False)
    
    return newList

def CheckListTrue (testList):
    return all(item == True for item in testList)

divisorRange = range(1, 21)
lowestNumber = max(divisorRange)*100
testList = SetList(max(divisorRange))

while (CheckListTrue(testList) != True):
    for divisor in divisorRange:        
        testList[divisor - 1] = CheckEvenDivisible(lowestNumber, divisor)
    
    if (CheckListTrue(testList)):
        break
    else:
        lowestNumber = lowestNumber + 20