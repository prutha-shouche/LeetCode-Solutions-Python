# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #approach 1
        # n=len(nums)+1
        # for i in range(0,n):
        #     if i not in nums:
        #         return i
       
        #approach 2
        #find total sum of given array -arrsum
        #find sum when it would have all numbers in array - n(n+1)/2 - actualsum
        # actualsum-arrsum
        n=len(nums)
        actualsum=(n*(n+1))/2
        arrsum=sum(nums)
        return int(actualsum-arrsum)