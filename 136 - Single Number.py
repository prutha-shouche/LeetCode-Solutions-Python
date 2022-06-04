# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #set is a data structure that only stores one occurence of the number
        #2*(a+b+c)-(2a+2b+c)=c
        return 2*sum(set(nums))-sum(nums)
        
        
            
        