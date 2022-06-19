# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 03:06:14 2022

@author: pruth
"""
#Leetcode 1346. Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #Approach 2 - O(N)
        num=set()
        for i in arr:
            if i*2 in num or i/2 in num:
                return True
            num.add(i)
        return False
            
        #Approach 1- time comp - O(N^2)
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if arr[i]==2*arr[j] and i!=j:
        #             return 1
                
        

                
                
                
        
        
            
        
            
        
        
        

            
        
        
        
        
        