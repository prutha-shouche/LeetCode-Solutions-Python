# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        #The bin() method converts a specified integer number to its binary representation and returns it.
        #The count() method returns the number of times a specified value appears in the string.
        return str(bin(n)).count('1')
        
        #Approach 2
#         count=0
#         while(n>0):
#             lastdigit=n%2
#             #print(lastdigit)
#             n=n//2
#             if lastdigit == 1:
#                 count=count+1
#             # n=n//2
#         return count
            
            
        
        
        
            
            
         


        
        
        