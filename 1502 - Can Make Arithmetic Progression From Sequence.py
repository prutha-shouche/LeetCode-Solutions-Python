# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1502. Can Make Arithmetic Progression From Sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a=set() #will store only unique values
        for i in range(0,len(arr)-1):
            a.add(arr[i]-arr[i+1])
        if len(a)==1:
            return True
        else:
            return False
            
        
            
        
        