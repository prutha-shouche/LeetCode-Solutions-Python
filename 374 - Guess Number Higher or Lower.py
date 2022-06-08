# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        mid=(l+r)//2
        while(l<=r):
            mid=(l+r)//2
            result=guess(mid)
            if result==0:
                return mid
            elif result==-1:
                r=mid-1
            else: 
                if result==1:
                    l=mid+1
       
        
                
            
            
        