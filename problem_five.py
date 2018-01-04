# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:43:05 2017

@author: Shameer Omar
Euler Problem - 5
"""
import numpy as np

parameter = int(20)
answer = int(1)

loopCounter = int(0)
check = True
limit = int(np.floor(np.sqrt(parameter)))

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]

while primeNumbers[loopCounter] <= parameter:
    exponent = int(1)
    
    if check:
        if primeNumbers[loopCounter] <= limit:
            exponent = np.floor(np.log(parameter)/np.log(primeNumbers[loopCounter]))
        else:
            check = False
        
    answer = answer * (pow(primeNumbers[loopCounter], exponent))
    loopCounter += 1

    