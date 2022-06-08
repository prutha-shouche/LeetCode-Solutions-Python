# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                return mid
        return -1
                
        