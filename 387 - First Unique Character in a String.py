# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 387. First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in dict.fromkeys(s):
            if s.count(i)==1:
                return s.index(i)
        else:
            return -1
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        