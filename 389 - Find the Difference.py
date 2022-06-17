# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t)-Counter(s))[0]
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        