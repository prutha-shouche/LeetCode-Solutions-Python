# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(0,n):
            a.append(nums[i]*nums[i])
        a.sort()
        return a
            
        
        

    
        
                
            
            
        