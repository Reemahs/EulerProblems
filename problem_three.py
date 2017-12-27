# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:49:42 2017

@author: Shameer Omar
Euler Problem: 3 - Largest Prime Factor
"""

originalDividend = 600851475143
dividend = originalDividend
divisor = 2
factors = []

while divisor * divisor <= dividend:
    if dividend % divisor:                  
        divisor += 1
    else:
        dividend //= divisor
        factors.append(divisor)
        
if dividend > 1:
    factors.append(dividend)
    
largestFactor = int(factors[len(factors)-1])
print("The largest prime factor of " + repr(originalDividend) + " is " + repr(largestFactor))