# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """  
        return s.reverse()
    
    
        #approach 2
        #    l = len(s) 
        # for i in s[::-1]:
        #     s.append(i)
        # s[0:] = s[l:]    


        
        
        