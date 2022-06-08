# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm
        curarray=nums[0]
        maxarr=nums[0]
        for i in range(1,len(nums)):
            curarray=max(nums[i], curarray+nums[i])
            maxarr=max(curarray, maxarr)
        return maxarr
        
        