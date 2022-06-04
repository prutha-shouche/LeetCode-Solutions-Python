# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""

#LeetCode Question 11 - Container with most water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0
        while(l<r):
            breadth=r-l
            length=min(height[l],height[r])
            area=length*breadth
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1
            max_area=max(max_area,area)
        return max_area
            
        