# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #approach 1
        arr= collections.Counter(nums) #A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
        for i in arr:
            if arr[i]==1:
                return i
        
        
        
        #approach 2
        #set is a data structure that only stores one occurence of the number
        #2*(a+b+c)-(2a+2b+c)=c
        return 2*sum(set(nums))-sum(nums)
        
        
            
        
