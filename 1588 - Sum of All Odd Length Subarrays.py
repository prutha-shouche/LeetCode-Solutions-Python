# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1588. Sum of All Odd Length Subarrays


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1,2):
                total=total+sum(arr[i:j])
        return total
        
        
        
        