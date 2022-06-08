# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            else:
                if numbers[i]+numbers[j]>target:
                    j=j-1
                else:
                    i=i+1
    
        