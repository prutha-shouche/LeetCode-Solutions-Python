# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 69. Sqrt(x)


class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(0,x+1):
            square=i*i
            if square==x:
                return i
            elif square>x:
                return i-1
        return x

        
        

            
        
        
        
        
        