# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1523. Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n=(high+1)-low
        if low%2==0:
            return (n//2)
        else:
            return (high-low)//2+1

    
        
                
            
            
        