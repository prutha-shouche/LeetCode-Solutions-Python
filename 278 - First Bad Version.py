# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 278. First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while(l<r):
            mid=l+(r-l)//2
            if (not isBadVersion(mid)):
                l=mid+1
            else:
                r=mid
        return l