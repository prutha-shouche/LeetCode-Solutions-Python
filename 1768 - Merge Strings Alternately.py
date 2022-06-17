# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        n=l
        i=0
        word=[]
        while(l!=0):
            word.append(word1[i]+word2[i])
            i=i+1
            l=l-1
        if len(word1)<len(word2):
            word+=word2[n:] 
        else:
            word+=word1[n:] 
        return "".join(word)
                
                
        
            
                    
        
    
        
        

            
        
        
        
        
        