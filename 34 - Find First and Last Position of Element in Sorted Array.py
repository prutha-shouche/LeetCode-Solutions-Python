# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        temp=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                temp.append(i)
            else:
                continue
        n=len(temp)
        if n==0:
            return [-1,-1]
        else:
            return [temp[0],temp[n-1]]
#         
            
        