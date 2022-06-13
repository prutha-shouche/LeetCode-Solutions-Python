# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 189. Rotate Array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        
        

            
        
        
        
        
        