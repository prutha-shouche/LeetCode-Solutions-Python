# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for num in nums:
            if num!=0:
                nums[j]=num
                j=j+1
        for n in range(j, len(nums)):
            nums[n]=0
            
#         n = len(nums)
#         temp[]
#         for i in range(0,n):
#             if nums[i]!=0:
#                 temp.add(nums[i])
                
#         m=len(temp)
#         for i in range(m,n):
#             temp.add(0)
