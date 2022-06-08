# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr=set(nums) #set only gives unique values of the list
        nums.sort()
        if nums!=sorted(arr): 
            return True
        else:
            return False
        
#sort() function modifies and sorts nums list
#sorted() function creates a new list containing sorted version of the list
                
                
        