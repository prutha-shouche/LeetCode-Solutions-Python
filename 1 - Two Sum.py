# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i]+nums[j]
                if a == target:
                    return [i,j]
        #approach 2 (optimized) 
        # a = dict() #0
        # for i in range(len(nums)):
        #     num = nums[i] #2
        #     complement = target - num #7
        #     if num in a:
        #         return [a[num], i] 
        #     else:
        #         a[complement] = i #7,0
            
            
            
         


        
        
        