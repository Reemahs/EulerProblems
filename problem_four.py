# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:48:24 2017

@author: Shameer Omar
Euler Problem: 4 - Largest Palindrome Product
"""

import numpy as np

def CheckNumDigits (number):
    numDigits = np.log10(number) + 1
    return int(numDigits);

def CheckPalindrome (number):
    reverse = str(number)[::-1]
    return number == int(reverse);

componentOne = 100
componentTwo = 100
palindromes = []

while (CheckNumDigits(componentOne) <= 3):
    componentTwo = 10;
    while(CheckNumDigits(componentTwo) <= 3):
        product = componentOne * componentTwo
        
        if (CheckPalindrome(product)):
            palindromes.append(product)
        
        componentTwo = componentTwo + 1
    componentOne = componentOne + 1

palindromes.sort()
largestPalindrome = int(palindromes[len(palindromes)-1])
print("The largest palindrome of a product of two 3-digit numbers is: " + repr(largestPalindrome))