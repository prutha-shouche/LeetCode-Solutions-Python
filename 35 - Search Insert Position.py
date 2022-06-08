# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        l=0
        r=len(nums)
        mid=(l+r)//2
        while(l<r):
            x=nums[mid]
            if target==x:
                return mid
            elif target>x:
                l=mid+1
            else:
                r=mid
            mid=(l+r)//2
        return mid
            
                
            
            
        