# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1822. Sign of the Product of an Array

class Solution:
    def signFunc(self,prdt):
        if prdt<0:
            return -1
        elif prdt>0:
            return 1
        elif prdt==0:
            return 0
    def arraySign(self, nums: List[int]) -> int:
        prdt=1
        for i in range(len(nums)):
            prdt=prdt*nums[i]
        return self.signFunc(prdt)
    
            
        