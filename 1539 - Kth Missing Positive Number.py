# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1539. Kth Missing Positive Number


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[]
        i=1
        while len(a)<k:
            if i not in arr:
                a.append(i)
            i=i+1
        return a[k-1]
                
        
        

            
        
        
        
        
        