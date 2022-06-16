# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Approach 1
        return (sorted(list(s))==sorted(list(t)))
    
        #Approach 2
        #Counter() => returns the count of each element in the container 
        return Counter(s)==Counter(t)
    
        #Approach 3
        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
        
        
      
        
        
            
                    
        
    
        
        

            
        
        
        
        
        