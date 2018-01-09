# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:43:05 2017

@author: Shameer Omar
Euler Problem - 5
Description - This problem solves the smallest positive number that can be evenly divisable by all of the numbers between 1 and 20.
"""
import numpy as np

parameter = int(20)																		#Define the maximum number that the smallest possible number has to be a multiple of.
answer = int(1)																			#Set the initial value of the anser to one. This will help later in the loop

loopCounter = int(0)																	#This is a coutner to determine how many times the a loop has occured.
check = True																			#Condition to check if a factor (1 to 20) is required more than once. This value will never be larger than the largest factor. See next line.
limit = int(np.floor(np.sqrt(parameter)))												#Remove any decial values. 

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]												#We will only be requiring the prime numbers between 1 and 20. This is due to the fact that any ommitted numbers can be created from a combination of these numbers.

while primeNumbers[loopCounter] <= parameter:											#Continue while there are prime numbers to evaluate
    exponent = int(1)																	#Reset the exponent for each prime to one.
    
    if check:
        if primeNumbers[loopCounter] <= limit:											#Only prime numbers less than the limit can be used multiple times 
            exponent = np.floor(np.log(parameter)/np.log(primeNumbers[loopCounter]))	#Find out how many times a certain prime number is multiplied to make up the largest facter.
        else:
            check = False													
        
    answer = answer * (pow(primeNumbers[loopCounter], exponent))						#When check is false this will be equivlent to a * b * c...
    loopCounter += 1